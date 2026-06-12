"""Generated from Smithy shape ``com.amazonaws.inspector#RegisterCrossAccountAccessRoleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn


class RegisterCrossAccountAccessRoleRequest(TypedDict):
    role_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the IAM role that grants Amazon Inspector access to AWS Services needed to perform security assessments. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterCrossAccountAccessRoleRequest) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterCrossAccountAccessRoleRequest:
    out: RegisterCrossAccountAccessRoleRequest = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "RegisterCrossAccountAccessRoleRequest.role_arn required"
        )
    return out
