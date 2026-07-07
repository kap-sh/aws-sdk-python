"""Generated from Smithy shape ``com.amazonaws.memorydb#PurchaseReservedNodesOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.tag_list


class PurchaseReservedNodesOfferingRequest(TypedDict, closed=True):
    reserved_nodes_offering_id: "aws_sdk_memorydb.types.string.String"
    """<p>The ID of the reserved node offering to purchase.</p>"""
    reservation_id: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>A customer-specified identifier to track this reservation.</p>"""
    node_count: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The number of node instances to reserve.</p>"""
    tags: NotRequired["aws_sdk_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PurchaseReservedNodesOfferingRequest) -> dict:
    out: dict = {}
    out["ReservedNodesOfferingId"] = value["reserved_nodes_offering_id"]
    if "reservation_id" in value:
        out["ReservationId"] = value["reservation_id"]
    if "node_count" in value:
        out["NodeCount"] = value["node_count"]
    if "tags" in value:
        import aws_sdk_memorydb.types.tag_list

        out["Tags"] = aws_sdk_memorydb.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PurchaseReservedNodesOfferingRequest:
    out: PurchaseReservedNodesOfferingRequest = {}  # type: ignore[typeddict-item]
    if "ReservedNodesOfferingId" in data:
        out["reserved_nodes_offering_id"] = data["ReservedNodesOfferingId"]
    else:
        raise DeserializationError(
            "PurchaseReservedNodesOfferingRequest.reserved_nodes_offering_id required"
        )
    if "ReservationId" in data:
        out["reservation_id"] = data["ReservationId"]
    if "NodeCount" in data:
        out["node_count"] = data["NodeCount"]
    if "Tags" in data:
        import aws_sdk_memorydb.types.tag_list

        out["tags"] = aws_sdk_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
