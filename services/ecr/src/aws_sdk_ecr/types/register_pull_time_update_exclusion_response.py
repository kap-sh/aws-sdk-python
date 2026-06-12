"""Generated from Smithy shape ``com.amazonaws.ecr#RegisterPullTimeUpdateExclusionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.creation_timestamp
    import aws_sdk_ecr.types.principal_arn


class RegisterPullTimeUpdateExclusionResponse(TypedDict):
    principal_arn: NotRequired["aws_sdk_ecr.types.principal_arn.PrincipalArn"]
    """<p>The ARN of the IAM principal that was added to the pull time update exclusion list.</p>"""
    created_at: NotRequired["aws_sdk_ecr.types.creation_timestamp.CreationTimestamp"]
    """<p>The date and time, expressed in standard JavaScript date format, when the exclusion was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterPullTimeUpdateExclusionResponse) -> dict:
    out: dict = {}
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    if "created_at" in value:
        import aws_sdk_ecr.types.creation_timestamp

        out["createdAt"] = aws_sdk_ecr.types.creation_timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterPullTimeUpdateExclusionResponse:
    out: RegisterPullTimeUpdateExclusionResponse = {}  # type: ignore[typeddict-item]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    if "createdAt" in data:
        import aws_sdk_ecr.types.creation_timestamp

        out["created_at"] = (
            aws_sdk_ecr.types.creation_timestamp.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    return out
