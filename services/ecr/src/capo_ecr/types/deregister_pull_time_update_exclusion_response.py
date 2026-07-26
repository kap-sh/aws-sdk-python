"""Generated from Smithy shape ``com.amazonaws.ecr#DeregisterPullTimeUpdateExclusionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.principal_arn


class DeregisterPullTimeUpdateExclusionResponse(TypedDict, closed=True):
    principal_arn: NotRequired["capo_ecr.types.principal_arn.PrincipalArn"]
    """<p>The ARN of the IAM principal that was removed from the pull time update exclusion list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterPullTimeUpdateExclusionResponse) -> dict:
    out: dict = {}
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterPullTimeUpdateExclusionResponse:
    out: DeregisterPullTimeUpdateExclusionResponse = {}  # type: ignore[typeddict-item]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    return out
