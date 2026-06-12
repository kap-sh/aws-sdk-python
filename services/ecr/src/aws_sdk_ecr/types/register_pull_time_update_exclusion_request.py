"""Generated from Smithy shape ``com.amazonaws.ecr#RegisterPullTimeUpdateExclusionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.principal_arn


class RegisterPullTimeUpdateExclusionRequest(TypedDict):
    principal_arn: "aws_sdk_ecr.types.principal_arn.PrincipalArn"
    """<p>The ARN of the IAM principal to exclude from having image pull times recorded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterPullTimeUpdateExclusionRequest) -> dict:
    out: dict = {}
    out["principalArn"] = value["principal_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterPullTimeUpdateExclusionRequest:
    out: RegisterPullTimeUpdateExclusionRequest = {}  # type: ignore[typeddict-item]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    else:
        raise DeserializationError(
            "RegisterPullTimeUpdateExclusionRequest.principal_arn required"
        )
    return out
