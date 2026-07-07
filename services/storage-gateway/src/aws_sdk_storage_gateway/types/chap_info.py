"""Generated from Smithy shape ``com.amazonaws.storagegateway#ChapInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.chap_secret
    import aws_sdk_storage_gateway.types.iqn_name
    import aws_sdk_storage_gateway.types.target_arn


class ChapInfo(TypedDict, closed=True):
    target_arn: NotRequired["aws_sdk_storage_gateway.types.target_arn.TargetARN"]
    """<p>The Amazon Resource Name (ARN) of the volume.</p> <p>Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).</p>"""
    secret_to_authenticate_initiator: NotRequired[
        "aws_sdk_storage_gateway.types.chap_secret.ChapSecret"
    ]
    """<p>The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.</p>"""
    initiator_name: NotRequired["aws_sdk_storage_gateway.types.iqn_name.IqnName"]
    """<p>The iSCSI initiator that connects to the target.</p>"""
    secret_to_authenticate_target: NotRequired[
        "aws_sdk_storage_gateway.types.chap_secret.ChapSecret"
    ]
    """<p>The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g., Windows client).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChapInfo) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["TargetARN"] = value["target_arn"]
    if "secret_to_authenticate_initiator" in value:
        out["SecretToAuthenticateInitiator"] = value["secret_to_authenticate_initiator"]
    if "initiator_name" in value:
        out["InitiatorName"] = value["initiator_name"]
    if "secret_to_authenticate_target" in value:
        out["SecretToAuthenticateTarget"] = value["secret_to_authenticate_target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ChapInfo:
    out: ChapInfo = {}  # type: ignore[typeddict-item]
    if "TargetARN" in data:
        out["target_arn"] = data["TargetARN"]
    if "SecretToAuthenticateInitiator" in data:
        out["secret_to_authenticate_initiator"] = data["SecretToAuthenticateInitiator"]
    if "InitiatorName" in data:
        out["initiator_name"] = data["InitiatorName"]
    if "SecretToAuthenticateTarget" in data:
        out["secret_to_authenticate_target"] = data["SecretToAuthenticateTarget"]
    return out
