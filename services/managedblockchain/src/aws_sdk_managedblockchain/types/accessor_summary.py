"""Generated from Smithy shape ``com.amazonaws.managedblockchain#AccessorSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.accessor_network_type
    import aws_sdk_managedblockchain.types.accessor_status
    import aws_sdk_managedblockchain.types.accessor_type
    import aws_sdk_managedblockchain.types.arn_string
    import aws_sdk_managedblockchain.types.resource_id_string
    import aws_sdk_managedblockchain.types.timestamp


class AccessorSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the accessor.</p>"""
    type: NotRequired["aws_sdk_managedblockchain.types.accessor_type.AccessorType"]
    """<p>The type of the accessor.</p> <note> <p>Currently accessor type is restricted to <code>BILLING_TOKEN</code>.</p> </note>"""
    status: NotRequired[
        "aws_sdk_managedblockchain.types.accessor_status.AccessorStatus"
    ]
    """<p>The current status of the accessor.</p>"""
    creation_date: NotRequired["aws_sdk_managedblockchain.types.timestamp.Timestamp"]
    """<p>The creation date and time of the accessor.</p>"""
    arn: NotRequired["aws_sdk_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the accessor. For more information about ARNs and their format, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    network_type: NotRequired[
        "aws_sdk_managedblockchain.types.accessor_network_type.AccessorNetworkType"
    ]
    """<p>The blockchain network that the Accessor token is created for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessorSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import aws_sdk_managedblockchain.types.accessor_type

        out["Type"] = aws_sdk_managedblockchain.types.accessor_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import aws_sdk_managedblockchain.types.accessor_status

        out["Status"] = aws_sdk_managedblockchain.types.accessor_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import aws_sdk_managedblockchain.types.timestamp

        out["CreationDate"] = aws_sdk_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "network_type" in value:
        import aws_sdk_managedblockchain.types.accessor_network_type

        out["NetworkType"] = (
            aws_sdk_managedblockchain.types.accessor_network_type.serialize_json(
                value["network_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccessorSummary:
    out: AccessorSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import aws_sdk_managedblockchain.types.accessor_type

        out["type"] = aws_sdk_managedblockchain.types.accessor_type.deserialize_json(
            data["Type"]
        )
    if "Status" in data:
        import aws_sdk_managedblockchain.types.accessor_status

        out["status"] = (
            aws_sdk_managedblockchain.types.accessor_status.deserialize_json(
                data["Status"]
            )
        )
    if "CreationDate" in data:
        import aws_sdk_managedblockchain.types.timestamp

        out["creation_date"] = (
            aws_sdk_managedblockchain.types.timestamp.deserialize_json(
                data["CreationDate"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "NetworkType" in data:
        import aws_sdk_managedblockchain.types.accessor_network_type

        out["network_type"] = (
            aws_sdk_managedblockchain.types.accessor_network_type.deserialize_json(
                data["NetworkType"]
            )
        )
    return out
