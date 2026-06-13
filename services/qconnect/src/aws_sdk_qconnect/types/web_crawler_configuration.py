"""Generated from Smithy shape ``com.amazonaws.qconnect#WebCrawlerConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.url_configuration
    import aws_sdk_qconnect.types.url_filter_list
    import aws_sdk_qconnect.types.web_crawler_limits
    import aws_sdk_qconnect.types.web_scope_type


class WebCrawlerConfiguration(TypedDict):
    url_configuration: "aws_sdk_qconnect.types.url_configuration.UrlConfiguration"
    """<p>The configuration of the URL/URLs for the web content that you want to crawl. You should be authorized to crawl the URLs.</p>"""
    crawler_limits: NotRequired[
        "aws_sdk_qconnect.types.web_crawler_limits.WebCrawlerLimits"
    ]
    """<p>The configuration of crawl limits for the web URLs.</p>"""
    inclusion_filters: NotRequired[
        "aws_sdk_qconnect.types.url_filter_list.UrlFilterList"
    ]
    """<p>A list of one or more inclusion regular expression patterns to include certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.</p>"""
    exclusion_filters: NotRequired[
        "aws_sdk_qconnect.types.url_filter_list.UrlFilterList"
    ]
    """<p>A list of one or more exclusion regular expression patterns to exclude certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.</p>"""
    scope: NotRequired["aws_sdk_qconnect.types.web_scope_type.WebScopeType"]
    """<p>The scope of what is crawled for your URLs. You can choose to crawl only web pages that belong to the same host or primary domain. For example, only web pages that contain the seed URL <code>https://docs.aws.amazon.com/bedrock/latest/userguide/</code> and no other domains. You can choose to include sub domains in addition to the host or primary domain. For example, web pages that contain <code>aws.amazon.com</code> can also include sub domain <code>docs.aws.amazon.com</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebCrawlerConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.url_configuration

    out["urlConfiguration"] = aws_sdk_qconnect.types.url_configuration.serialize_json(
        value["url_configuration"]
    )
    if "crawler_limits" in value:
        import aws_sdk_qconnect.types.web_crawler_limits

        out["crawlerLimits"] = aws_sdk_qconnect.types.web_crawler_limits.serialize_json(
            value["crawler_limits"]
        )
    if "inclusion_filters" in value:
        import aws_sdk_qconnect.types.url_filter_list

        out["inclusionFilters"] = aws_sdk_qconnect.types.url_filter_list.serialize_json(
            value["inclusion_filters"]
        )
    if "exclusion_filters" in value:
        import aws_sdk_qconnect.types.url_filter_list

        out["exclusionFilters"] = aws_sdk_qconnect.types.url_filter_list.serialize_json(
            value["exclusion_filters"]
        )
    if "scope" in value:
        out["scope"] = value["scope"]
    return out


def deserialize_json(data: dict) -> WebCrawlerConfiguration:
    out: WebCrawlerConfiguration = {}  # type: ignore[typeddict-item]
    if "urlConfiguration" in data:
        import aws_sdk_qconnect.types.url_configuration

        out["url_configuration"] = (
            aws_sdk_qconnect.types.url_configuration.deserialize_json(
                data["urlConfiguration"]
            )
        )
    else:
        raise DeserializationError("WebCrawlerConfiguration.url_configuration required")
    if "crawlerLimits" in data:
        import aws_sdk_qconnect.types.web_crawler_limits

        out["crawler_limits"] = (
            aws_sdk_qconnect.types.web_crawler_limits.deserialize_json(
                data["crawlerLimits"]
            )
        )
    if "inclusionFilters" in data:
        import aws_sdk_qconnect.types.url_filter_list

        out["inclusion_filters"] = (
            aws_sdk_qconnect.types.url_filter_list.deserialize_json(
                data["inclusionFilters"]
            )
        )
    if "exclusionFilters" in data:
        import aws_sdk_qconnect.types.url_filter_list

        out["exclusion_filters"] = (
            aws_sdk_qconnect.types.url_filter_list.deserialize_json(
                data["exclusionFilters"]
            )
        )
    if "scope" in data:
        out["scope"] = data["scope"]
    return out
