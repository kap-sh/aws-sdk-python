"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateContextResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.context_arn


class CreateContextResponse(TypedDict):
    context_arn: NotRequired["aws_sdk_sagemaker.types.context_arn.ContextArn"]
    """<p>The Amazon Resource Name (ARN) of the context.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContextResponse) -> dict:
    out: dict = {}
    if "context_arn" in value:
        out["ContextArn"] = value["context_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContextResponse:
    out: CreateContextResponse = {}  # type: ignore[typeddict-item]
    if "ContextArn" in data:
        out["context_arn"] = data["ContextArn"]
    return out
