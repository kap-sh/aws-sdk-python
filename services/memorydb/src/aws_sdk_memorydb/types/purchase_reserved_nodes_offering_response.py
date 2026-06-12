"""Generated from Smithy shape ``com.amazonaws.memorydb#PurchaseReservedNodesOfferingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.reserved_node


class PurchaseReservedNodesOfferingResponse(TypedDict):
    reserved_node: NotRequired["aws_sdk_memorydb.types.reserved_node.ReservedNode"]
    """<p>Represents the output of a <code>PurchaseReservedNodesOffering</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PurchaseReservedNodesOfferingResponse) -> dict:
    out: dict = {}
    if "reserved_node" in value:
        import aws_sdk_memorydb.types.reserved_node

        out["ReservedNode"] = (
            aws_sdk_memorydb.types.reserved_node.serialize_aws_json_1_1(
                value["reserved_node"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PurchaseReservedNodesOfferingResponse:
    out: PurchaseReservedNodesOfferingResponse = {}  # type: ignore[typeddict-item]
    if "ReservedNode" in data:
        import aws_sdk_memorydb.types.reserved_node

        out["reserved_node"] = (
            aws_sdk_memorydb.types.reserved_node.deserialize_aws_json_1_1(
                data["ReservedNode"]
            )
        )
    return out
