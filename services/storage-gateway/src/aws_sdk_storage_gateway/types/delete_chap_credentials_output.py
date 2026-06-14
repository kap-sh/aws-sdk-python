"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteChapCredentialsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.iqn_name
    import aws_sdk_storage_gateway.types.target_arn


class DeleteChapCredentialsOutput(TypedDict):
    target_arn: NotRequired["aws_sdk_storage_gateway.types.target_arn.TargetARN"]
    """<p>The Amazon Resource Name (ARN) of the target.</p>"""
    initiator_name: NotRequired["aws_sdk_storage_gateway.types.iqn_name.IqnName"]
    """<p>The iSCSI initiator that connects to the target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteChapCredentialsOutput) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["TargetARN"] = value["target_arn"]
    if "initiator_name" in value:
        out["InitiatorName"] = value["initiator_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteChapCredentialsOutput:
    out: DeleteChapCredentialsOutput = {}  # type: ignore[typeddict-item]
    if "TargetARN" in data:
        out["target_arn"] = data["TargetARN"]
    if "InitiatorName" in data:
        out["initiator_name"] = data["InitiatorName"]
    return out
