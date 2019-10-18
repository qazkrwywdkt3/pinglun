from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article


# Create your views here.

def hello_world(request):
    return HttpResponse('啦啦啦 范笑莹小可爱')


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title: %s,brief_content: %s,content: %s,' \
                 'article_id: %s,publish_date: %s' % (title,
                                                      brief_content,
                                                      content,
                                                      article_id,
                                                      publish_date
                                                      )

    return HttpResponse(return_str)


def get_index_page(request):
    all_article = Article.objects.all()
    return render(request, "blog/index.html",
                  {
                      'article_list': all_article
                  }
                  )


def get_detail_page(request,article_id):
    all_article = Article.objects.all()
    curr_article = None
    presious_index = 0
    next_index = 0
    presious_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            presious_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            presious_index = index - 1
            next_index = index
        else:
            presious_index = index - 1
            next_index = index + 1

        if article.article_id == article_id:
            curr_article = article
            presious_article = all_article[presious_index]
            next_article = all_article[next_index]
            break

    curr_article = Article.objects.all()[0]
    return render(request, 'blog/detail.html',
                  {
                      'curr_article':curr_article,
                      'presious_article':presious_article,
                      'next_article':next_article
                  }
                  )
