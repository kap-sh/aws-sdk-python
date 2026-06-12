"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.arn_string
    import aws_sdk_managedblockchain.types.description_string
    import aws_sdk_managedblockchain.types.framework
    import aws_sdk_managedblockchain.types.framework_version_string
    import aws_sdk_managedblockchain.types.name_string
    import aws_sdk_managedblockchain.types.network_status
    import aws_sdk_managedblockchain.types.resource_id_string
    import aws_sdk_managedblockchain.types.timestamp


class NetworkSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the network.</p>"""
    name: NotRequired["aws_sdk_managedblockchain.types.name_string.NameString"]
    """<p>The name of the network.</p>"""
    description: NotRequired[
        "aws_sdk_managedblockchain.types.description_string.DescriptionString"
    ]
    """<p>An optional description of the network.</p>"""
    framework: NotRequired["aws_sdk_managedblockchain.types.framework.Framework"]
    """<p>The blockchain framework that the network uses.</p>"""
    framework_version: NotRequired[
        "aws_sdk_managedblockchain.types.framework_version_string.FrameworkVersionString"
    ]
    """<p>The version of the blockchain framework that the network uses.</p>"""
    status: NotRequired["aws_sdk_managedblockchain.types.network_status.NetworkStatus"]
    """<p>The current status of the network.</p>"""
    creation_date: NotRequired["aws_sdk_managedblockchain.types.timestamp.Timestamp"]
    """<p>The date and time that the network was created.</p>"""
    arn: NotRequired["aws_sdk_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the network. For more information about ARNs and their format, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "framework" in value:
        import aws_sdk_managedblockchain.types.framework

        out["Framework"] = aws_sdk_managedblockchain.types.framework.serialize_json(
            value["framework"]
        )
    if "framework_version" in value:
        out["FrameworkVersion"] = value["framework_version"]
    if "status" in value:
        import aws_sdk_managedblockchain.types.network_status

        out["Status"] = aws_sdk_managedblockchain.types.network_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import aws_sdk_managedblockchain.types.timestamp

        out["CreationDate"] = aws_sdk_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> NetworkSummary:
    out: NetworkSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Framework" in data:
        import aws_sdk_managedblockchain.types.framework

        out["framework"] = aws_sdk_managedblockchain.types.framework.deserialize_json(
            data["Framework"]
        )
    if "FrameworkVersion" in data:
        out["framework_version"] = data["FrameworkVersion"]
    if "Status" in data:
        import aws_sdk_managedblockchain.types.network_status

        out["status"] = aws_sdk_managedblockchain.types.network_status.deserialize_json(
            data["Status"]
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
    return out
