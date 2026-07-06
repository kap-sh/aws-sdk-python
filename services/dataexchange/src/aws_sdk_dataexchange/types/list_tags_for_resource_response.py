"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.map_of__string


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_dataexchange.types.map_of__string.MapOf__string"]
    """<p>A label that consists of a customer-defined key and an optional value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_dataexchange.types.map_of__string

        out["tags"] = aws_sdk_dataexchange.types.map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_dataexchange.types.map_of__string

        out["tags"] = aws_sdk_dataexchange.types.map_of__string.deserialize_json(
            data["tags"]
        )
    return out
