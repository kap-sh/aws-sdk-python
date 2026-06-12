"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationRole``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.impersonation_role_id
    import aws_sdk_workmail.types.impersonation_role_name
    import aws_sdk_workmail.types.impersonation_role_type
    import aws_sdk_workmail.types.timestamp


class ImpersonationRole(TypedDict):
    impersonation_role_id: NotRequired[
        "aws_sdk_workmail.types.impersonation_role_id.ImpersonationRoleId"
    ]
    """<p>The identifier of the impersonation role.</p>"""
    name: NotRequired[
        "aws_sdk_workmail.types.impersonation_role_name.ImpersonationRoleName"
    ]
    """<p>The impersonation role name.</p>"""
    type: NotRequired[
        "aws_sdk_workmail.types.impersonation_role_type.ImpersonationRoleType"
    ]
    """<p>The impersonation role type.</p>"""
    date_created: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date when the impersonation role was created.</p>"""
    date_modified: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date when the impersonation role was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationRole) -> dict:
    out: dict = {}
    if "impersonation_role_id" in value:
        out["ImpersonationRoleId"] = value["impersonation_role_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_workmail.types.impersonation_role_type

        out["Type"] = (
            aws_sdk_workmail.types.impersonation_role_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "date_created" in value:
        import aws_sdk_workmail.types.timestamp

        out["DateCreated"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_created"]
        )
    if "date_modified" in value:
        import aws_sdk_workmail.types.timestamp

        out["DateModified"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_modified"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImpersonationRole:
    out: ImpersonationRole = {}  # type: ignore[typeddict-item]
    if "ImpersonationRoleId" in data:
        out["impersonation_role_id"] = data["ImpersonationRoleId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_workmail.types.impersonation_role_type

        out["type"] = (
            aws_sdk_workmail.types.impersonation_role_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "DateCreated" in data:
        import aws_sdk_workmail.types.timestamp

        out["date_created"] = aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateCreated"]
        )
    if "DateModified" in data:
        import aws_sdk_workmail.types.timestamp

        out["date_modified"] = (
            aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
                data["DateModified"]
            )
        )
    return out
