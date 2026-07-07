"""Generated from Smithy shape ``com.amazonaws.workmail#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.email_address
    import aws_sdk_workmail.types.entity_state
    import aws_sdk_workmail.types.identity_provider_identity_store_id
    import aws_sdk_workmail.types.identity_provider_user_id
    import aws_sdk_workmail.types.string
    import aws_sdk_workmail.types.timestamp
    import aws_sdk_workmail.types.user_name
    import aws_sdk_workmail.types.user_role
    import aws_sdk_workmail.types.work_mail_identifier


class User(TypedDict, closed=True):
    id: NotRequired["aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier"]
    """<p>The identifier of the user.</p>"""
    email: NotRequired["aws_sdk_workmail.types.email_address.EmailAddress"]
    """<p>The email of the user.</p>"""
    name: NotRequired["aws_sdk_workmail.types.user_name.UserName"]
    """<p>The name of the user.</p>"""
    display_name: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>The display name of the user.</p>"""
    state: NotRequired["aws_sdk_workmail.types.entity_state.EntityState"]
    """<p>The state of the user, which can be ENABLED, DISABLED, or DELETED.</p>"""
    user_role: NotRequired["aws_sdk_workmail.types.user_role.UserRole"]
    """<p>The role of the user.</p>"""
    enabled_date: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the user was enabled for WorkMail use.</p>"""
    disabled_date: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the user was disabled from WorkMail use.</p>"""
    identity_provider_user_id: NotRequired[
        "aws_sdk_workmail.types.identity_provider_user_id.IdentityProviderUserId"
    ]
    """<p>User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.</p>"""
    identity_provider_identity_store_id: NotRequired[
        "aws_sdk_workmail.types.identity_provider_identity_store_id.IdentityProviderIdentityStoreId"
    ]
    """<p>Identity store ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: User) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "email" in value:
        out["Email"] = value["email"]
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "state" in value:
        import aws_sdk_workmail.types.entity_state

        out["State"] = aws_sdk_workmail.types.entity_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "user_role" in value:
        import aws_sdk_workmail.types.user_role

        out["UserRole"] = aws_sdk_workmail.types.user_role.serialize_aws_json_1_1(
            value["user_role"]
        )
    if "enabled_date" in value:
        import aws_sdk_workmail.types.timestamp

        out["EnabledDate"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["enabled_date"]
        )
    if "disabled_date" in value:
        import aws_sdk_workmail.types.timestamp

        out["DisabledDate"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["disabled_date"]
        )
    if "identity_provider_user_id" in value:
        out["IdentityProviderUserId"] = value["identity_provider_user_id"]
    if "identity_provider_identity_store_id" in value:
        out["IdentityProviderIdentityStoreId"] = value[
            "identity_provider_identity_store_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Email" in data:
        out["email"] = data["Email"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "State" in data:
        import aws_sdk_workmail.types.entity_state

        out["state"] = aws_sdk_workmail.types.entity_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "UserRole" in data:
        import aws_sdk_workmail.types.user_role

        out["user_role"] = aws_sdk_workmail.types.user_role.deserialize_aws_json_1_1(
            data["UserRole"]
        )
    if "EnabledDate" in data:
        import aws_sdk_workmail.types.timestamp

        out["enabled_date"] = aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["EnabledDate"]
        )
    if "DisabledDate" in data:
        import aws_sdk_workmail.types.timestamp

        out["disabled_date"] = (
            aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
                data["DisabledDate"]
            )
        )
    if "IdentityProviderUserId" in data:
        out["identity_provider_user_id"] = data["IdentityProviderUserId"]
    if "IdentityProviderIdentityStoreId" in data:
        out["identity_provider_identity_store_id"] = data[
            "IdentityProviderIdentityStoreId"
        ]
    return out
