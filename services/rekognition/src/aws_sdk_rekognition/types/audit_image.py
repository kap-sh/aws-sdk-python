"""Generated from Smithy shape ``com.amazonaws.rekognition#AuditImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.bounding_box
    import aws_sdk_rekognition.types.liveness_image_blob
    import aws_sdk_rekognition.types.s3_object


class AuditImage(TypedDict, closed=True):
    bytes: NotRequired[
        "aws_sdk_rekognition.types.liveness_image_blob.LivenessImageBlob"
    ]
    """<p>The Base64-encoded bytes representing an image selected from the Face Liveness video and returned for audit purposes.</p>"""
    s3_object: NotRequired["aws_sdk_rekognition.types.s3_object.S3Object"]
    bounding_box: NotRequired["aws_sdk_rekognition.types.bounding_box.BoundingBox"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuditImage) -> dict:
    out: dict = {}
    if "bytes" in value:
        import aws_sdk_rekognition.types.liveness_image_blob

        out["Bytes"] = (
            aws_sdk_rekognition.types.liveness_image_blob.serialize_aws_json_1_1(
                value["bytes"]
            )
        )
    if "s3_object" in value:
        import aws_sdk_rekognition.types.s3_object

        out["S3Object"] = aws_sdk_rekognition.types.s3_object.serialize_aws_json_1_1(
            value["s3_object"]
        )
    if "bounding_box" in value:
        import aws_sdk_rekognition.types.bounding_box

        out["BoundingBox"] = (
            aws_sdk_rekognition.types.bounding_box.serialize_aws_json_1_1(
                value["bounding_box"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuditImage:
    out: AuditImage = {}  # type: ignore[typeddict-item]
    if "Bytes" in data:
        import aws_sdk_rekognition.types.liveness_image_blob

        out["bytes"] = (
            aws_sdk_rekognition.types.liveness_image_blob.deserialize_aws_json_1_1(
                data["Bytes"]
            )
        )
    if "S3Object" in data:
        import aws_sdk_rekognition.types.s3_object

        out["s3_object"] = aws_sdk_rekognition.types.s3_object.deserialize_aws_json_1_1(
            data["S3Object"]
        )
    if "BoundingBox" in data:
        import aws_sdk_rekognition.types.bounding_box

        out["bounding_box"] = (
            aws_sdk_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    return out
