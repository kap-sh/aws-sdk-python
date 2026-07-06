"""Generated from Smithy shape ``com.amazonaws.managedblockchain#UpdateNodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.node_log_publishing_configuration
    import aws_sdk_managedblockchain.types.resource_id_string


class UpdateNodeInput(TypedDict, closed=True):
    network_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network that the node is on.</p>"""
    member_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the member that owns the node.</p> <p>Applies only to Hyperledger Fabric.</p>"""
    node_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the node.</p>"""
    log_publishing_configuration: NotRequired[
        "aws_sdk_managedblockchain.types.node_log_publishing_configuration.NodeLogPublishingConfiguration"
    ]
    """<p>Configuration properties for publishing to Amazon CloudWatch Logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNodeInput) -> dict:
    out: dict = {}
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    if "log_publishing_configuration" in value:
        import aws_sdk_managedblockchain.types.node_log_publishing_configuration

        out["LogPublishingConfiguration"] = (
            aws_sdk_managedblockchain.types.node_log_publishing_configuration.serialize_json(
                value["log_publishing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateNodeInput:
    out: UpdateNodeInput = {}  # type: ignore[typeddict-item]
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    if "LogPublishingConfiguration" in data:
        import aws_sdk_managedblockchain.types.node_log_publishing_configuration

        out["log_publishing_configuration"] = (
            aws_sdk_managedblockchain.types.node_log_publishing_configuration.deserialize_json(
                data["LogPublishingConfiguration"]
            )
        )
    return out
