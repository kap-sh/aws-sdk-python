"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_marketplace_catalog.types.resource_arn.ResourceARN"
    """<p>Required. The Amazon Resource Name (ARN) associated with the resource you want to list tags on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
