"""Generated from Smithy shape ``com.amazonaws.ecr#ImageFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_failure_code
    import capo_ecr.types.image_failure_reason
    import capo_ecr.types.image_identifier


class ImageFailure(TypedDict, closed=True):
    image_id: NotRequired["capo_ecr.types.image_identifier.ImageIdentifier"]
    """<p>The image ID associated with the failure.</p>"""
    failure_code: NotRequired["capo_ecr.types.image_failure_code.ImageFailureCode"]
    """<p>The code associated with the failure.</p>"""
    failure_reason: NotRequired[
        "capo_ecr.types.image_failure_reason.ImageFailureReason"
    ]
    """<p>The reason for the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageFailure) -> dict:
    out: dict = {}
    if "image_id" in value:
        import capo_ecr.types.image_identifier

        out["imageId"] = capo_ecr.types.image_identifier.serialize_aws_json_1_1(
            value["image_id"]
        )
    if "failure_code" in value:
        import capo_ecr.types.image_failure_code

        out["failureCode"] = capo_ecr.types.image_failure_code.serialize_aws_json_1_1(
            value["failure_code"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageFailure:
    out: ImageFailure = {}  # type: ignore[typeddict-item]
    if data.get("imageId") is not None:
        import capo_ecr.types.image_identifier

        out["image_id"] = capo_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    if data.get("failureCode") is not None:
        import capo_ecr.types.image_failure_code

        out["failure_code"] = (
            capo_ecr.types.image_failure_code.deserialize_aws_json_1_1(
                data["failureCode"]
            )
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out
