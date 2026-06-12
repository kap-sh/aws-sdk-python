"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateChapCredentialsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.chap_secret
    import aws_sdk_storage_gateway.types.iqn_name
    import aws_sdk_storage_gateway.types.target_arn


class UpdateChapCredentialsInput(TypedDict):
    target_arn: "aws_sdk_storage_gateway.types.target_arn.TargetARN"
    """<p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return the TargetARN for specified VolumeARN.</p>"""
    secret_to_authenticate_initiator: (
        "aws_sdk_storage_gateway.types.chap_secret.ChapSecret"
    )
    """<p>The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.</p> <note> <p>The secret key must be between 12 and 16 bytes when encoded in UTF-8.</p> </note>"""
    initiator_name: "aws_sdk_storage_gateway.types.iqn_name.IqnName"
    """<p>The iSCSI initiator that connects to the target.</p>"""
    secret_to_authenticate_target: NotRequired[
        "aws_sdk_storage_gateway.types.chap_secret.ChapSecret"
    ]
    """<p>The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).</p> <p>Byte constraints: Minimum bytes of 12. Maximum bytes of 16.</p> <note> <p>The secret key must be between 12 and 16 bytes when encoded in UTF-8.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateChapCredentialsInput) -> dict:
    out: dict = {}
    out["TargetARN"] = value["target_arn"]
    out["SecretToAuthenticateInitiator"] = value["secret_to_authenticate_initiator"]
    out["InitiatorName"] = value["initiator_name"]
    if "secret_to_authenticate_target" in value:
        out["SecretToAuthenticateTarget"] = value["secret_to_authenticate_target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateChapCredentialsInput:
    out: UpdateChapCredentialsInput = {}  # type: ignore[typeddict-item]
    if "TargetARN" in data:
        out["target_arn"] = data["TargetARN"]
    else:
        raise DeserializationError("UpdateChapCredentialsInput.target_arn required")
    if "SecretToAuthenticateInitiator" in data:
        out["secret_to_authenticate_initiator"] = data["SecretToAuthenticateInitiator"]
    else:
        raise DeserializationError(
            "UpdateChapCredentialsInput.secret_to_authenticate_initiator required"
        )
    if "InitiatorName" in data:
        out["initiator_name"] = data["InitiatorName"]
    else:
        raise DeserializationError("UpdateChapCredentialsInput.initiator_name required")
    if "SecretToAuthenticateTarget" in data:
        out["secret_to_authenticate_target"] = data["SecretToAuthenticateTarget"]
    return out
