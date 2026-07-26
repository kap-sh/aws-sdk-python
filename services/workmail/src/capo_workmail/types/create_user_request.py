"""Generated from Smithy shape ``com.amazonaws.workmail#CreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.boolean
    import capo_workmail.types.identity_provider_user_id
    import capo_workmail.types.organization_id
    import capo_workmail.types.password
    import capo_workmail.types.user_attribute
    import capo_workmail.types.user_name
    import capo_workmail.types.user_role


class CreateUserRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier of the organization for which the user is created.</p>"""
    name: "capo_workmail.types.user_name.UserName"
    """<p>The name for the new user. WorkMail directory user names have a maximum length of 64. All others have a maximum length of 20.</p>"""
    display_name: "capo_workmail.types.user_attribute.UserAttribute"
    """<p>The display name for the new user.</p>"""
    password: NotRequired["capo_workmail.types.password.Password"]
    """<p>The password for the new user.</p>"""
    role: NotRequired["capo_workmail.types.user_role.UserRole"]
    """<p>The role of the new user.</p> <p>You cannot pass <i>SYSTEM_USER</i> or <i>RESOURCE</i> role in a single request. When a user role is not selected, the default role of <i>USER</i> is selected.</p>"""
    first_name: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>The first name of the new user.</p>"""
    last_name: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>The last name of the new user. </p>"""
    hidden_from_global_address_list: "capo_workmail.types.boolean.Boolean"
    """<p>If this parameter is enabled, the user will be hidden from the address book.</p>"""
    identity_provider_user_id: NotRequired[
        "capo_workmail.types.identity_provider_user_id.IdentityProviderUserId"
    ]
    """<p>User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Name"] = value["name"]
    out["DisplayName"] = value["display_name"]
    if "password" in value:
        out["Password"] = value["password"]
    if "role" in value:
        import capo_workmail.types.user_role

        out["Role"] = capo_workmail.types.user_role.serialize_aws_json_1_1(
            value["role"]
        )
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    out["HiddenFromGlobalAddressList"] = value.get(
        "hidden_from_global_address_list", False
    )
    if "identity_provider_user_id" in value:
        out["IdentityProviderUserId"] = value["identity_provider_user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("CreateUserRequest.organization_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateUserRequest.name required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("CreateUserRequest.display_name required")
    if "Password" in data:
        out["password"] = data["Password"]
    if "Role" in data:
        import capo_workmail.types.user_role

        out["role"] = capo_workmail.types.user_role.deserialize_aws_json_1_1(
            data["Role"]
        )
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    if "HiddenFromGlobalAddressList" in data:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    else:
        out["hidden_from_global_address_list"] = False
    if "IdentityProviderUserId" in data:
        out["identity_provider_user_id"] = data["IdentityProviderUserId"]
    return out
