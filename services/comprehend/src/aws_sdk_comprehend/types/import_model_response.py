"""Generated from Smithy shape ``com.amazonaws.comprehend#ImportModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_model_arn


class ImportModelResponse(TypedDict):
    model_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the custom model being imported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportModelResponse) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportModelResponse:
    out: ImportModelResponse = {}  # type: ignore[typeddict-item]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    return out
