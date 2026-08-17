"""Generated from Smithy shape ``com.amazonaws.sfn#TaskCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.long_arn


class TaskCredentials(TypedDict, closed=True):
    role_arn: NotRequired["capo_sfn.types.long_arn.LongArn"]
    """<p>The ARN of an IAM role that Step Functions assumes for the task. The role can allow cross-account access to resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskCredentials) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskCredentials:
    out: TaskCredentials = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out
