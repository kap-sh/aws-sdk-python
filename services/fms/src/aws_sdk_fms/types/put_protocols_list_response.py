"""Generated from Smithy shape ``com.amazonaws.fms#PutProtocolsListResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.protocols_list_data
    import aws_sdk_fms.types.resource_arn


class PutProtocolsListResponse(TypedDict):
    protocols_list: NotRequired[
        "aws_sdk_fms.types.protocols_list_data.ProtocolsListData"
    ]
    """<p>The details of the Firewall Manager protocols list.</p>"""
    protocols_list_arn: NotRequired["aws_sdk_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the protocols list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutProtocolsListResponse) -> dict:
    out: dict = {}
    if "protocols_list" in value:
        import aws_sdk_fms.types.protocols_list_data

        out["ProtocolsList"] = (
            aws_sdk_fms.types.protocols_list_data.serialize_aws_json_1_1(
                value["protocols_list"]
            )
        )
    if "protocols_list_arn" in value:
        out["ProtocolsListArn"] = value["protocols_list_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutProtocolsListResponse:
    out: PutProtocolsListResponse = {}  # type: ignore[typeddict-item]
    if "ProtocolsList" in data:
        import aws_sdk_fms.types.protocols_list_data

        out["protocols_list"] = (
            aws_sdk_fms.types.protocols_list_data.deserialize_aws_json_1_1(
                data["ProtocolsList"]
            )
        )
    if "ProtocolsListArn" in data:
        out["protocols_list_arn"] = data["ProtocolsListArn"]
    return out
