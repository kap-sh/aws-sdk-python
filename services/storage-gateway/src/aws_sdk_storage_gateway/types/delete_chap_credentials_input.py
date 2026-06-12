"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteChapCredentialsInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.iqn_name
    import aws_sdk_storage_gateway.types.target_arn


class DeleteChapCredentialsInput(TypedDict):
    target_arn: "aws_sdk_storage_gateway.types.target_arn.TargetARN"
    """<p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return to retrieve the TargetARN for specified VolumeARN.</p>"""
    initiator_name: "aws_sdk_storage_gateway.types.iqn_name.IqnName"
    """<p>The iSCSI initiator that connects to the target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteChapCredentialsInput) -> dict:
    out: dict = {}
    out["TargetARN"] = value["target_arn"]
    out["InitiatorName"] = value["initiator_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteChapCredentialsInput:
    out: DeleteChapCredentialsInput = {}  # type: ignore[typeddict-item]
    if "TargetARN" in data:
        out["target_arn"] = data["TargetARN"]
    else:
        raise DeserializationError("DeleteChapCredentialsInput.target_arn required")
    if "InitiatorName" in data:
        out["initiator_name"] = data["InitiatorName"]
    else:
        raise DeserializationError("DeleteChapCredentialsInput.initiator_name required")
    return out
