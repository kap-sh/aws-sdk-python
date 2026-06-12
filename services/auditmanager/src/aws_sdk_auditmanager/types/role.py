"""Generated from Smithy shape ``com.amazonaws.auditmanager#Role``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.iam_arn
    import aws_sdk_auditmanager.types.role_type


class Role(TypedDict):
    role_type: "aws_sdk_auditmanager.types.role_type.RoleType"
    """<p> The type of customer persona. </p> <note> <p>In <code>CreateAssessment</code>, <code>roleType</code> can only be <code>PROCESS_OWNER</code>. </p> <p>In <code>UpdateSettings</code>, <code>roleType</code> can only be <code>PROCESS_OWNER</code>.</p> <p>In <code>BatchCreateDelegationByAssessment</code>, <code>roleType</code> can only be <code>RESOURCE_OWNER</code>.</p> </note>"""
    role_arn: "aws_sdk_auditmanager.types.iam_arn.IamArn"
    """<p> The Amazon Resource Name (ARN) of the IAM role. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Role) -> dict:
    out: dict = {}
    import aws_sdk_auditmanager.types.role_type

    out["roleType"] = aws_sdk_auditmanager.types.role_type.serialize_json(
        value["role_type"]
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> Role:
    out: Role = {}  # type: ignore[typeddict-item]
    if "roleType" in data:
        import aws_sdk_auditmanager.types.role_type

        out["role_type"] = aws_sdk_auditmanager.types.role_type.deserialize_json(
            data["roleType"]
        )
    else:
        raise DeserializationError("Role.role_type required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("Role.role_arn required")
    return out
