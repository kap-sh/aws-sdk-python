"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkInferenceComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_resource_identifier


class AIBenchmarkInferenceComponent(TypedDict, closed=True):
    identifier: NotRequired[
        "aws_sdk_sagemaker.types.ai_resource_identifier.AIResourceIdentifier"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the inference component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkInferenceComponent) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AIBenchmarkInferenceComponent:
    out: AIBenchmarkInferenceComponent = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    return out
