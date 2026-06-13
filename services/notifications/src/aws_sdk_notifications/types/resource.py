"""Generated from Smithy shape ``com.amazonaws.notifications#Resource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_notifications.types.arn
    import aws_sdk_notifications.types.tags
    import aws_sdk_notifications.types.url


class Resource(TypedDict):
    id: NotRequired["str"]
    """<p>The unique identifier for the resource.</p> <p>At least one id or ARN is required.</p>"""
    arn: NotRequired["aws_sdk_notifications.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource. At least one id or ARN is required.</p>"""
    detail_url: NotRequired["aws_sdk_notifications.types.url.Url"]
    """<p>The URL to the resource's detail page. If a detail page URL is unavailable, it is the URL to an informational page that describes the resource's type.</p>"""
    tags: NotRequired["aws_sdk_notifications.types.tags.Tags"]
    """<p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "detail_url" in value:
        out["detailUrl"] = value["detail_url"]
    if "tags" in value:
        import aws_sdk_notifications.types.tags

        out["tags"] = aws_sdk_notifications.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "detailUrl" in data:
        out["detail_url"] = data["detailUrl"]
    if "tags" in data:
        import aws_sdk_notifications.types.tags

        out["tags"] = aws_sdk_notifications.types.tags.deserialize_json(data["tags"])
    return out
