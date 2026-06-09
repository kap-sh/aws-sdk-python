"""Generated from Smithy shape ``com.amazonaws.eks#AssociateEncryptionConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.encryption_config_list
    import aws_sdk_eks.types.string


class AssociateEncryptionConfigRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    encryption_config: "aws_sdk_eks.types.encryption_config_list.EncryptionConfigList"
    """<p>The configuration you are using for encryption.</p>"""
    client_request_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateEncryptionConfigRequest) -> dict:
    out: dict = {}
    import aws_sdk_eks.types.encryption_config_list

    out["encryptionConfig"] = aws_sdk_eks.types.encryption_config_list.serialize_json(
        value["encryption_config"]
    )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> AssociateEncryptionConfigRequest:
    out: AssociateEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
    if "encryptionConfig" in data:
        import aws_sdk_eks.types.encryption_config_list

        out["encryption_config"] = (
            aws_sdk_eks.types.encryption_config_list.deserialize_json(
                data["encryptionConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateEncryptionConfigRequest.encryption_config required"
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
