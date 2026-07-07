"""Generated from Smithy shape ``com.amazonaws.pinpoint#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.tags_model


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags_model: NotRequired["aws_sdk_pinpoint.types.tags_model.TagsModel"]


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags_model" in value:
        import aws_sdk_pinpoint.types.tags_model

        out["TagsModel"] = aws_sdk_pinpoint.types.tags_model.serialize_json(
            value["tags_model"]
        )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "TagsModel" in data:
        import aws_sdk_pinpoint.types.tags_model

        out["tags_model"] = aws_sdk_pinpoint.types.tags_model.deserialize_json(
            data["TagsModel"]
        )
    return out
