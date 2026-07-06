"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.positive_int_object
    import aws_sdk_storage_gateway.types.resource_arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_storage_gateway.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the resource for which you want to list tags.</p>"""
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that indicates the position at which to begin returning the list of tags.</p>"""
    limit: NotRequired[
        "aws_sdk_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>Specifies that the list of tags returned be limited to the specified number of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("ListTagsForResourceInput.resource_arn required")
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
