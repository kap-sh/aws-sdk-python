"""Generated from Smithy shape ``com.amazonaws.emrserverless#JobRunExecutionIamPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.policy_arn_list
    import capo_emr_serverless.types.policy_document


class JobRunExecutionIamPolicy(TypedDict, closed=True):
    policy: NotRequired["capo_emr_serverless.types.policy_document.PolicyDocument"]
    """<p>An IAM inline policy to use as an execution IAM policy.</p>"""
    policy_arns: NotRequired["capo_emr_serverless.types.policy_arn_list.PolicyArnList"]
    """<p>A list of Amazon Resource Names (ARNs) to use as an execution IAM policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobRunExecutionIamPolicy) -> dict:
    out: dict = {}
    if "policy" in value:
        out["policy"] = value["policy"]
    if "policy_arns" in value:
        import capo_emr_serverless.types.policy_arn_list

        out["policyArns"] = capo_emr_serverless.types.policy_arn_list.serialize_json(
            value["policy_arns"]
        )
    return out


def deserialize_json(data: dict) -> JobRunExecutionIamPolicy:
    out: JobRunExecutionIamPolicy = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    if "policyArns" in data:
        import capo_emr_serverless.types.policy_arn_list

        out["policy_arns"] = capo_emr_serverless.types.policy_arn_list.deserialize_json(
            data["policyArns"]
        )
    return out
