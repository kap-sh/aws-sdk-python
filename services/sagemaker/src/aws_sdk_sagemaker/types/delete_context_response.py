"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteContextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.context_arn


class DeleteContextResponse(TypedDict, closed=True):
    context_arn: NotRequired["aws_sdk_sagemaker.types.context_arn.ContextArn"]
    """<p>The Amazon Resource Name (ARN) of the context.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteContextResponse) -> dict:
    out: dict = {}
    if "context_arn" in value:
        out["ContextArn"] = value["context_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteContextResponse:
    out: DeleteContextResponse = {}  # type: ignore[typeddict-item]
    if "ContextArn" in data:
        out["context_arn"] = data["ContextArn"]
    return out
