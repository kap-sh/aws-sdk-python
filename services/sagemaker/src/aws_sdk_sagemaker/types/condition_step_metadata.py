"""Generated from Smithy shape ``com.amazonaws.sagemaker#ConditionStepMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.condition_outcome


class ConditionStepMetadata(TypedDict):
    outcome: NotRequired["aws_sdk_sagemaker.types.condition_outcome.ConditionOutcome"]
    """<p>The outcome of the Condition step evaluation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionStepMetadata) -> dict:
    out: dict = {}
    if "outcome" in value:
        import aws_sdk_sagemaker.types.condition_outcome

        out["Outcome"] = (
            aws_sdk_sagemaker.types.condition_outcome.serialize_aws_json_1_1(
                value["outcome"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConditionStepMetadata:
    out: ConditionStepMetadata = {}  # type: ignore[typeddict-item]
    if "Outcome" in data:
        import aws_sdk_sagemaker.types.condition_outcome

        out["outcome"] = (
            aws_sdk_sagemaker.types.condition_outcome.deserialize_aws_json_1_1(
                data["Outcome"]
            )
        )
    return out
