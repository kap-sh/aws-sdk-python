"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#TagResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.tags


class TagResourceResult(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_codestar_notifications.types.tags.Tags"]
    """<p>The list of tags associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_codestar_notifications.types.tags

        out["Tags"] = aws_sdk_codestar_notifications.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> TagResourceResult:
    out: TagResourceResult = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_codestar_notifications.types.tags

        out["tags"] = aws_sdk_codestar_notifications.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
