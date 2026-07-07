"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.evaluation_context_identifier


class EvaluationContext(TypedDict, closed=True):
    evaluation_context_identifier: NotRequired[
        "aws_sdk_config_service.types.evaluation_context_identifier.EvaluationContextIdentifier"
    ]
    """<p>A unique EvaluationContextIdentifier ID for an EvaluationContext.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationContext) -> dict:
    out: dict = {}
    if "evaluation_context_identifier" in value:
        out["EvaluationContextIdentifier"] = value["evaluation_context_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationContext:
    out: EvaluationContext = {}  # type: ignore[typeddict-item]
    if "EvaluationContextIdentifier" in data:
        out["evaluation_context_identifier"] = data["EvaluationContextIdentifier"]
    return out
