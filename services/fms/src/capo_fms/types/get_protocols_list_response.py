"""Generated from Smithy shape ``com.amazonaws.fms#GetProtocolsListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.protocols_list_data
    import capo_fms.types.resource_arn


class GetProtocolsListResponse(TypedDict, closed=True):
    protocols_list: NotRequired["capo_fms.types.protocols_list_data.ProtocolsListData"]
    """<p>Information about the specified Firewall Manager protocols list.</p>"""
    protocols_list_arn: NotRequired["capo_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the specified protocols list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProtocolsListResponse) -> dict:
    out: dict = {}
    if "protocols_list" in value:
        import capo_fms.types.protocols_list_data

        out["ProtocolsList"] = (
            capo_fms.types.protocols_list_data.serialize_aws_json_1_1(
                value["protocols_list"]
            )
        )
    if "protocols_list_arn" in value:
        out["ProtocolsListArn"] = value["protocols_list_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProtocolsListResponse:
    out: GetProtocolsListResponse = {}  # type: ignore[typeddict-item]
    if "ProtocolsList" in data:
        import capo_fms.types.protocols_list_data

        out["protocols_list"] = (
            capo_fms.types.protocols_list_data.deserialize_aws_json_1_1(
                data["ProtocolsList"]
            )
        )
    if "ProtocolsListArn" in data:
        out["protocols_list_arn"] = data["ProtocolsListArn"]
    return out
