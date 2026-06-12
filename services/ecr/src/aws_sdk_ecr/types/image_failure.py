"""Generated from Smithy shape ``com.amazonaws.ecr#ImageFailure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_failure_code
    import aws_sdk_ecr.types.image_failure_reason
    import aws_sdk_ecr.types.image_identifier


class ImageFailure(TypedDict):
    image_id: NotRequired["aws_sdk_ecr.types.image_identifier.ImageIdentifier"]
    """<p>The image ID associated with the failure.</p>"""
    failure_code: NotRequired["aws_sdk_ecr.types.image_failure_code.ImageFailureCode"]
    """<p>The code associated with the failure.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_ecr.types.image_failure_reason.ImageFailureReason"
    ]
    """<p>The reason for the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageFailure) -> dict:
    out: dict = {}
    if "image_id" in value:
        import aws_sdk_ecr.types.image_identifier

        out["imageId"] = aws_sdk_ecr.types.image_identifier.serialize_aws_json_1_1(
            value["image_id"]
        )
    if "failure_code" in value:
        import aws_sdk_ecr.types.image_failure_code

        out["failureCode"] = (
            aws_sdk_ecr.types.image_failure_code.serialize_aws_json_1_1(
                value["failure_code"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageFailure:
    out: ImageFailure = {}  # type: ignore[typeddict-item]
    if "imageId" in data:
        import aws_sdk_ecr.types.image_identifier

        out["image_id"] = aws_sdk_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    if "failureCode" in data:
        import aws_sdk_ecr.types.image_failure_code

        out["failure_code"] = (
            aws_sdk_ecr.types.image_failure_code.deserialize_aws_json_1_1(
                data["failureCode"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
