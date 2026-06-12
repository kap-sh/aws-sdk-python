"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateSecurityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.client_authentication
    import aws_sdk_kafka.types.encryption_info


class UpdateSecurityRequest(TypedDict):
    client_authentication: NotRequired[
        "aws_sdk_kafka.types.client_authentication.ClientAuthentication"
    ]
    """<p>Includes all client authentication related information.</p>"""
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The version of the MSK cluster to update. Cluster versions aren't simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.</p>"""
    encryption_info: NotRequired["aws_sdk_kafka.types.encryption_info.EncryptionInfo"]
    """<p>Includes all encryption-related information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSecurityRequest) -> dict:
    out: dict = {}
    if "client_authentication" in value:
        import aws_sdk_kafka.types.client_authentication

        out["clientAuthentication"] = (
            aws_sdk_kafka.types.client_authentication.serialize_json(
                value["client_authentication"]
            )
        )
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "encryption_info" in value:
        import aws_sdk_kafka.types.encryption_info

        out["encryptionInfo"] = aws_sdk_kafka.types.encryption_info.serialize_json(
            value["encryption_info"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSecurityRequest:
    out: UpdateSecurityRequest = {}  # type: ignore[typeddict-item]
    if "clientAuthentication" in data:
        import aws_sdk_kafka.types.client_authentication

        out["client_authentication"] = (
            aws_sdk_kafka.types.client_authentication.deserialize_json(
                data["clientAuthentication"]
            )
        )
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "encryptionInfo" in data:
        import aws_sdk_kafka.types.encryption_info

        out["encryption_info"] = aws_sdk_kafka.types.encryption_info.deserialize_json(
            data["encryptionInfo"]
        )
    return out
