"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.tags


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_route53globalresolver.types.tags.Tags"]
    """<p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_route53globalresolver.types.tags

        out["tags"] = aws_sdk_route53globalresolver.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_route53globalresolver.types.tags

        out["tags"] = aws_sdk_route53globalresolver.types.tags.deserialize_json(
            data["tags"]
        )
    return out
