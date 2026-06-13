"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateInferenceProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.inference_profile_arn
    import aws_sdk_bedrock.types.inference_profile_status


class CreateInferenceProfileResponse(TypedDict):
    inference_profile_arn: (
        "aws_sdk_bedrock.types.inference_profile_arn.InferenceProfileArn"
    )
    """<p>The ARN of the inference profile that you created.</p>"""
    status: NotRequired[
        "aws_sdk_bedrock.types.inference_profile_status.InferenceProfileStatus"
    ]
    """<p>The status of the inference profile. <code>ACTIVE</code> means that the inference profile is ready to be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInferenceProfileResponse) -> dict:
    out: dict = {}
    out["inferenceProfileArn"] = value["inference_profile_arn"]
    if "status" in value:
        import aws_sdk_bedrock.types.inference_profile_status

        out["status"] = aws_sdk_bedrock.types.inference_profile_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> CreateInferenceProfileResponse:
    out: CreateInferenceProfileResponse = {}  # type: ignore[typeddict-item]
    if "inferenceProfileArn" in data:
        out["inference_profile_arn"] = data["inferenceProfileArn"]
    else:
        raise DeserializationError(
            "CreateInferenceProfileResponse.inference_profile_arn required"
        )
    if "status" in data:
        import aws_sdk_bedrock.types.inference_profile_status

        out["status"] = aws_sdk_bedrock.types.inference_profile_status.deserialize_json(
            data["status"]
        )
    return out
