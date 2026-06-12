"""Generated from Smithy shape ``com.amazonaws.fms#ProtocolsListDataSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.list_id
    import aws_sdk_fms.types.protocols_list
    import aws_sdk_fms.types.resource_arn
    import aws_sdk_fms.types.resource_name


class ProtocolsListDataSummary(TypedDict):
    list_arn: NotRequired["aws_sdk_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the specified protocols list.</p>"""
    list_id: NotRequired["aws_sdk_fms.types.list_id.ListId"]
    """<p>The ID of the specified protocols list.</p>"""
    list_name: NotRequired["aws_sdk_fms.types.resource_name.ResourceName"]
    """<p>The name of the specified protocols list.</p>"""
    protocols_list: NotRequired["aws_sdk_fms.types.protocols_list.ProtocolsList"]
    """<p>An array of protocols in the Firewall Manager protocols list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtocolsListDataSummary) -> dict:
    out: dict = {}
    if "list_arn" in value:
        out["ListArn"] = value["list_arn"]
    if "list_id" in value:
        out["ListId"] = value["list_id"]
    if "list_name" in value:
        out["ListName"] = value["list_name"]
    if "protocols_list" in value:
        import aws_sdk_fms.types.protocols_list

        out["ProtocolsList"] = aws_sdk_fms.types.protocols_list.serialize_aws_json_1_1(
            value["protocols_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtocolsListDataSummary:
    out: ProtocolsListDataSummary = {}  # type: ignore[typeddict-item]
    if "ListArn" in data:
        out["list_arn"] = data["ListArn"]
    if "ListId" in data:
        out["list_id"] = data["ListId"]
    if "ListName" in data:
        out["list_name"] = data["ListName"]
    if "ProtocolsList" in data:
        import aws_sdk_fms.types.protocols_list

        out["protocols_list"] = (
            aws_sdk_fms.types.protocols_list.deserialize_aws_json_1_1(
                data["ProtocolsList"]
            )
        )
    return out
