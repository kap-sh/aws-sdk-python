"""Generated from Smithy shape ``com.amazonaws.workspacesweb#WebContentFilteringPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.blocked_categories
    import aws_sdk_workspaces_web.types.url_pattern_list


class WebContentFilteringPolicy(TypedDict):
    blocked_categories: NotRequired[
        "aws_sdk_workspaces_web.types.blocked_categories.BlockedCategories"
    ]
    """<p>Categories of websites that are blocked on the end user’s browsers.</p>"""
    allowed_urls: NotRequired[
        "aws_sdk_workspaces_web.types.url_pattern_list.UrlPatternList"
    ]
    """<p>URLs and domains that are always accessible to end users.</p>"""
    blocked_urls: NotRequired[
        "aws_sdk_workspaces_web.types.url_pattern_list.UrlPatternList"
    ]
    """<p>URLs and domains that end users cannot access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebContentFilteringPolicy) -> dict:
    out: dict = {}
    if "blocked_categories" in value:
        import aws_sdk_workspaces_web.types.blocked_categories

        out["blockedCategories"] = (
            aws_sdk_workspaces_web.types.blocked_categories.serialize_json(
                value["blocked_categories"]
            )
        )
    if "allowed_urls" in value:
        import aws_sdk_workspaces_web.types.url_pattern_list

        out["allowedUrls"] = (
            aws_sdk_workspaces_web.types.url_pattern_list.serialize_json(
                value["allowed_urls"]
            )
        )
    if "blocked_urls" in value:
        import aws_sdk_workspaces_web.types.url_pattern_list

        out["blockedUrls"] = (
            aws_sdk_workspaces_web.types.url_pattern_list.serialize_json(
                value["blocked_urls"]
            )
        )
    return out


def deserialize_json(data: dict) -> WebContentFilteringPolicy:
    out: WebContentFilteringPolicy = {}  # type: ignore[typeddict-item]
    if "blockedCategories" in data:
        import aws_sdk_workspaces_web.types.blocked_categories

        out["blocked_categories"] = (
            aws_sdk_workspaces_web.types.blocked_categories.deserialize_json(
                data["blockedCategories"]
            )
        )
    if "allowedUrls" in data:
        import aws_sdk_workspaces_web.types.url_pattern_list

        out["allowed_urls"] = (
            aws_sdk_workspaces_web.types.url_pattern_list.deserialize_json(
                data["allowedUrls"]
            )
        )
    if "blockedUrls" in data:
        import aws_sdk_workspaces_web.types.url_pattern_list

        out["blocked_urls"] = (
            aws_sdk_workspaces_web.types.url_pattern_list.deserialize_json(
                data["blockedUrls"]
            )
        )
    return out
