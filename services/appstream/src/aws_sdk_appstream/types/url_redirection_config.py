"""Generated from Smithy shape ``com.amazonaws.appstream#UrlRedirectionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.boolean_object
    import aws_sdk_appstream.types.url_pattern_list


class UrlRedirectionConfig(TypedDict):
    enabled: NotRequired["aws_sdk_appstream.types.boolean_object.BooleanObject"]
    """<p>Whether URL redirection is enabled for this direction.</p>"""
    allowed_urls: NotRequired["aws_sdk_appstream.types.url_pattern_list.UrlPatternList"]
    """<p>List of URL patterns that are allowed to be redirected. URLs matching these patterns will be redirected unless they also match a pattern in the denied list.</p>"""
    denied_urls: NotRequired["aws_sdk_appstream.types.url_pattern_list.UrlPatternList"]
    """<p>List of URL patterns that are denied from redirection. This list takes precedence over the allowed list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UrlRedirectionConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "allowed_urls" in value:
        import aws_sdk_appstream.types.url_pattern_list

        out["AllowedUrls"] = (
            aws_sdk_appstream.types.url_pattern_list.serialize_aws_json_1_1(
                value["allowed_urls"]
            )
        )
    if "denied_urls" in value:
        import aws_sdk_appstream.types.url_pattern_list

        out["DeniedUrls"] = (
            aws_sdk_appstream.types.url_pattern_list.serialize_aws_json_1_1(
                value["denied_urls"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UrlRedirectionConfig:
    out: UrlRedirectionConfig = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "AllowedUrls" in data:
        import aws_sdk_appstream.types.url_pattern_list

        out["allowed_urls"] = (
            aws_sdk_appstream.types.url_pattern_list.deserialize_aws_json_1_1(
                data["AllowedUrls"]
            )
        )
    if "DeniedUrls" in data:
        import aws_sdk_appstream.types.url_pattern_list

        out["denied_urls"] = (
            aws_sdk_appstream.types.url_pattern_list.deserialize_aws_json_1_1(
                data["DeniedUrls"]
            )
        )
    return out
