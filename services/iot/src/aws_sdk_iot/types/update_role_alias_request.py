"""Generated from Smithy shape ``com.amazonaws.iot#UpdateRoleAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.credential_duration_seconds
    import aws_sdk_iot.types.role_alias
    import aws_sdk_iot.types.role_arn


class UpdateRoleAliasRequest(TypedDict, closed=True):
    role_alias: "aws_sdk_iot.types.role_alias.RoleAlias"
    """<p>The role alias to update.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The role ARN.</p>"""
    credential_duration_seconds: NotRequired[
        "aws_sdk_iot.types.credential_duration_seconds.CredentialDurationSeconds"
    ]
    """<p>The number of seconds the credential will be valid.</p> <p>This value must be less than or equal to the maximum session duration of the IAM role that the role alias references.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoleAliasRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "credential_duration_seconds" in value:
        out["credentialDurationSeconds"] = value["credential_duration_seconds"]
    return out


def deserialize_json(data: dict) -> UpdateRoleAliasRequest:
    out: UpdateRoleAliasRequest = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "credentialDurationSeconds" in data:
        out["credential_duration_seconds"] = data["credentialDurationSeconds"]
    return out
