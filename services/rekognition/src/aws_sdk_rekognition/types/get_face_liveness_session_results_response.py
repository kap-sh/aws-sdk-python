"""Generated from Smithy shape ``com.amazonaws.rekognition#GetFaceLivenessSessionResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.audit_image
    import aws_sdk_rekognition.types.audit_images
    import aws_sdk_rekognition.types.challenge
    import aws_sdk_rekognition.types.liveness_session_id
    import aws_sdk_rekognition.types.liveness_session_status
    import aws_sdk_rekognition.types.percent


class GetFaceLivenessSessionResultsResponse(TypedDict, closed=True):
    session_id: "aws_sdk_rekognition.types.liveness_session_id.LivenessSessionId"
    """<p>The sessionId for which this request was called.</p>"""
    status: "aws_sdk_rekognition.types.liveness_session_status.LivenessSessionStatus"
    """<p>Represents a status corresponding to the state of the session. Possible statuses are: CREATED, IN_PROGRESS, SUCCEEDED, FAILED, EXPIRED.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Probabalistic confidence score for if the person in the given video was live, represented as a float value between 0 to 100.</p>"""
    reference_image: NotRequired["aws_sdk_rekognition.types.audit_image.AuditImage"]
    """<p>A high-quality image from the Face Liveness video that can be used for face comparison or search. It includes a bounding box of the face and the Base64-encoded bytes that return an image. If the CreateFaceLivenessSession request included an OutputConfig argument, the image will be uploaded to an S3Object specified in the output configuration. In case the reference image is not returned, it's recommended to retry the Liveness check.</p>"""
    audit_images: NotRequired["aws_sdk_rekognition.types.audit_images.AuditImages"]
    """<p>A set of images from the Face Liveness video that can be used for audit purposes. It includes a bounding box of the face and the Base64-encoded bytes that return an image. If the CreateFaceLivenessSession request included an OutputConfig argument, the image will be uploaded to an S3Object specified in the output configuration. If no Amazon S3 bucket is defined, raw bytes are sent instead.</p>"""
    challenge: NotRequired["aws_sdk_rekognition.types.challenge.Challenge"]
    """<p>Contains information regarding the challenge type used for the Face Liveness check.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFaceLivenessSessionResultsResponse) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    import aws_sdk_rekognition.types.liveness_session_status

    out["Status"] = (
        aws_sdk_rekognition.types.liveness_session_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "reference_image" in value:
        import aws_sdk_rekognition.types.audit_image

        out["ReferenceImage"] = (
            aws_sdk_rekognition.types.audit_image.serialize_aws_json_1_1(
                value["reference_image"]
            )
        )
    if "audit_images" in value:
        import aws_sdk_rekognition.types.audit_images

        out["AuditImages"] = (
            aws_sdk_rekognition.types.audit_images.serialize_aws_json_1_1(
                value["audit_images"]
            )
        )
    if "challenge" in value:
        import aws_sdk_rekognition.types.challenge

        out["Challenge"] = aws_sdk_rekognition.types.challenge.serialize_aws_json_1_1(
            value["challenge"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFaceLivenessSessionResultsResponse:
    out: GetFaceLivenessSessionResultsResponse = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError(
            "GetFaceLivenessSessionResultsResponse.session_id required"
        )
    if "Status" in data:
        import aws_sdk_rekognition.types.liveness_session_status

        out["status"] = (
            aws_sdk_rekognition.types.liveness_session_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "GetFaceLivenessSessionResultsResponse.status required"
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "ReferenceImage" in data:
        import aws_sdk_rekognition.types.audit_image

        out["reference_image"] = (
            aws_sdk_rekognition.types.audit_image.deserialize_aws_json_1_1(
                data["ReferenceImage"]
            )
        )
    if "AuditImages" in data:
        import aws_sdk_rekognition.types.audit_images

        out["audit_images"] = (
            aws_sdk_rekognition.types.audit_images.deserialize_aws_json_1_1(
                data["AuditImages"]
            )
        )
    if "Challenge" in data:
        import aws_sdk_rekognition.types.challenge

        out["challenge"] = aws_sdk_rekognition.types.challenge.deserialize_aws_json_1_1(
            data["Challenge"]
        )
    return out
