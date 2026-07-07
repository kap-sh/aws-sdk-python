"""Generated from Smithy shape ``com.amazonaws.iot#RoleAliasDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_account_id
    import aws_sdk_iot.types.credential_duration_seconds
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.role_alias
    import aws_sdk_iot.types.role_alias_arn
    import aws_sdk_iot.types.role_arn


class RoleAliasDescription(TypedDict, closed=True):
    role_alias: NotRequired["aws_sdk_iot.types.role_alias.RoleAlias"]
    """<p>The role alias.</p>"""
    role_alias_arn: NotRequired["aws_sdk_iot.types.role_alias_arn.RoleAliasArn"]
    """<p>The ARN of the role alias.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The role ARN.</p>"""
    owner: NotRequired["aws_sdk_iot.types.aws_account_id.AwsAccountId"]
    """<p>The role alias owner.</p>"""
    credential_duration_seconds: NotRequired[
        "aws_sdk_iot.types.credential_duration_seconds.CredentialDurationSeconds"
    ]
    """<p>The number of seconds for which the credential is valid.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The UNIX timestamp of when the role alias was created.</p>"""
    last_modified_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The UNIX timestamp of when the role alias was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoleAliasDescription) -> dict:
    out: dict = {}
    if "role_alias" in value:
        out["roleAlias"] = value["role_alias"]
    if "role_alias_arn" in value:
        out["roleAliasArn"] = value["role_alias_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "credential_duration_seconds" in value:
        out["credentialDurationSeconds"] = value["credential_duration_seconds"]
    if "creation_date" in value:
        import aws_sdk_iot.types.date_type

        out["creationDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_iot.types.date_type

        out["lastModifiedDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> RoleAliasDescription:
    out: RoleAliasDescription = {}  # type: ignore[typeddict-item]
    if "roleAlias" in data:
        out["role_alias"] = data["roleAlias"]
    if "roleAliasArn" in data:
        out["role_alias_arn"] = data["roleAliasArn"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "owner" in data:
        out["owner"] = data["owner"]
    if "credentialDurationSeconds" in data:
        out["credential_duration_seconds"] = data["credentialDurationSeconds"]
    if "creationDate" in data:
        import aws_sdk_iot.types.date_type

        out["creation_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import aws_sdk_iot.types.date_type

        out["last_modified_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastModifiedDate"]
        )
    return out
