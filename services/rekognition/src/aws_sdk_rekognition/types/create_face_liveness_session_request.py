"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateFaceLivenessSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.client_request_token
    import aws_sdk_rekognition.types.create_face_liveness_session_request_settings
    import aws_sdk_rekognition.types.kms_key_id


class CreateFaceLivenessSessionRequest(TypedDict):
    kms_key_id: NotRequired["aws_sdk_rekognition.types.kms_key_id.KmsKeyId"]
    """<p> The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt audit images and reference images.</p>"""
    settings: NotRequired[
        "aws_sdk_rekognition.types.create_face_liveness_session_request_settings.CreateFaceLivenessSessionRequestSettings"
    ]
    """<p>A session settings object. It contains settings for the operation to be performed. For Face Liveness, it accepts <code>OutputConfig</code> and <code>AuditImagesLimit</code>.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token is used to recognize the Face Liveness request. If the same token is used with multiple <code>CreateFaceLivenessSession</code> requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFaceLivenessSessionRequest) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "settings" in value:
        import aws_sdk_rekognition.types.create_face_liveness_session_request_settings

        out["Settings"] = (
            aws_sdk_rekognition.types.create_face_liveness_session_request_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFaceLivenessSessionRequest:
    out: CreateFaceLivenessSessionRequest = {}  # type: ignore[typeddict-item]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "Settings" in data:
        import aws_sdk_rekognition.types.create_face_liveness_session_request_settings

        out["settings"] = (
            aws_sdk_rekognition.types.create_face_liveness_session_request_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
