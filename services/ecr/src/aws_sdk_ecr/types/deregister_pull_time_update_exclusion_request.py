"""Generated from Smithy shape ``com.amazonaws.ecr#DeregisterPullTimeUpdateExclusionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.principal_arn


class DeregisterPullTimeUpdateExclusionRequest(TypedDict, closed=True):
    principal_arn: "aws_sdk_ecr.types.principal_arn.PrincipalArn"
    """<p>The ARN of the IAM principal to remove from the pull time update exclusion list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterPullTimeUpdateExclusionRequest) -> dict:
    out: dict = {}
    out["principalArn"] = value["principal_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterPullTimeUpdateExclusionRequest:
    out: DeregisterPullTimeUpdateExclusionRequest = {}  # type: ignore[typeddict-item]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    else:
        raise DeserializationError(
            "DeregisterPullTimeUpdateExclusionRequest.principal_arn required"
        )
    return out
