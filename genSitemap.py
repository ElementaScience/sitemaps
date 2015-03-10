__author__ = 'dgreen'


class SiteMap:

    def __init__(self):
        pass

    def header(self):
        print """<?xml version="1.0" encoding="UTF-8"?>
    <urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">"""

    def footer(self):
        print """</urlset>"""

    def aURL(self, link, freq, priority = "0.5"):
        print "    <url> " + "<loc>" + link + "</loc>\n" \
              + "       <changefreq>"+freq+ "</changefreq>\n" \
              + "       <priority>"+priority+ "</priority>" + " </url>"

    def mainPage(self):
        self.aURL("http://elementascience.org", "hourly")

    def genMap(self, start, end):
        self.header()

        self.mainPage()

        items = range(7, 37) + [37] + [38] + [39] + [40] + [41]

        for i in items:
            self.aURL("""http://elementascience.org/article/info:doi/10.12952/journal.elementa.""" +
                      "{0:06d}".format(i), "monthly", "1")
            self.aURL("""http://elementascience.org/article/fetchObjectAttachment.action?uri=info:doi/10.12952/journal.elementa.""" + "{0:06d}".format(i) + """&amp;representation=PDF""",
                      "monthly",
                      "1")
            self.aURL("""http://elementascience.org/article/fetchObjectAttachment.action?uri=info:doi/10.12952/journal.elementa.""" + "{0:06d}".format(i) + """&amp;representation=XML""",
                      "monthly",
                      "1")
            self.aURL("""http://elementascience.org/article/fetchObjectAttachment.action?uri=info:doi/10.12952/journal.elementa.""" + "{0:06d}".format(i) + """&amp;representation=JSON""",
                      "monthly",
                      "1")
            self.aURL("""http://elementascience.org/article/fetchObjectAttachment.action?uri=info:doi/10.12952/journal.elementa.""" + "{0:06d}".format(i) + """&amp;representation=EPUB""",
                      "monthly",
                      "1")
            self.aURL("""http://elementascience.org/article/fetchObjectAttachment.action?uri=info:doi/10.12952/journal.elementa.""" + "{0:06d}".format(i) + """&amp;representation=MOBI""",
                      "monthly",
                      "1")
        self.footer()


if __name__ == '__main__':

    x = SiteMap()
    x.genMap(1,2)
