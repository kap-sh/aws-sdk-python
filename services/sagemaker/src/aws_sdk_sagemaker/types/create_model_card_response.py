"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelCardResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_card_arn


class CreateModelCardResponse(TypedDict):
    model_card_arn: NotRequired["aws_sdk_sagemaker.types.model_card_arn.ModelCardArn"]
    """<p>The Amazon Resource Name (ARN) of the successfully created model card.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelCardResponse) -> dict:
    out: dict = {}
    if "model_card_arn" in value:
        out["ModelCardArn"] = value["model_card_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelCardResponse:
    out: CreateModelCardResponse = {}  # type: ignore[typeddict-item]
    if "ModelCardArn" in data:
        out["model_card_arn"] = data["ModelCardArn"]
    return out
