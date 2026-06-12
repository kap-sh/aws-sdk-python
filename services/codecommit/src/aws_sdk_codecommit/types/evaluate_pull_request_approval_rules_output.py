"""Generated from Smithy shape ``com.amazonaws.codecommit#EvaluatePullRequestApprovalRulesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.evaluation


class EvaluatePullRequestApprovalRulesOutput(TypedDict):
    evaluation: "aws_sdk_codecommit.types.evaluation.Evaluation"
    """<p>The result of the evaluation, including the names of the rules whose conditions have been met (if any), the names of the rules whose conditions have not been met (if any), whether the pull request is in the approved state, and whether the pull request approval rule has been set aside by an override. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluatePullRequestApprovalRulesOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.evaluation

    out["evaluation"] = aws_sdk_codecommit.types.evaluation.serialize_aws_json_1_1(
        value["evaluation"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluatePullRequestApprovalRulesOutput:
    out: EvaluatePullRequestApprovalRulesOutput = {}  # type: ignore[typeddict-item]
    if "evaluation" in data:
        import aws_sdk_codecommit.types.evaluation

        out["evaluation"] = (
            aws_sdk_codecommit.types.evaluation.deserialize_aws_json_1_1(
                data["evaluation"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluatePullRequestApprovalRulesOutput.evaluation required"
        )
    return out
