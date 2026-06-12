"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.boolean
    import aws_sdk_workmail.types.email_address
    import aws_sdk_workmail.types.entity_state
    import aws_sdk_workmail.types.identity_provider_identity_store_id
    import aws_sdk_workmail.types.identity_provider_user_id
    import aws_sdk_workmail.types.timestamp
    import aws_sdk_workmail.types.user_attribute
    import aws_sdk_workmail.types.user_name
    import aws_sdk_workmail.types.user_role
    import aws_sdk_workmail.types.work_mail_identifier


class DescribeUserResponse(TypedDict):
    user_id: NotRequired[
        "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier"
    ]
    """<p>The identifier for the described user.</p>"""
    name: NotRequired["aws_sdk_workmail.types.user_name.UserName"]
    """<p>The name for the user.</p>"""
    email: NotRequired["aws_sdk_workmail.types.email_address.EmailAddress"]
    """<p>The email of the user.</p>"""
    display_name: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>The display name of the user.</p>"""
    state: NotRequired["aws_sdk_workmail.types.entity_state.EntityState"]
    """<p>The state of a user: enabled (registered to WorkMail) or disabled (deregistered or never registered to WorkMail).</p>"""
    user_role: NotRequired["aws_sdk_workmail.types.user_role.UserRole"]
    """<p>In certain cases, other entities are modeled as users. If interoperability is enabled, resources are imported into WorkMail as users. Because different WorkMail organizations rely on different directory types, administrators can distinguish between an unregistered user (account is disabled and has a user role) and the directory administrators. The values are USER, RESOURCE, SYSTEM_USER, and REMOTE_USER.</p>"""
    enabled_date: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date and time at which the user was enabled for WorkMailusage, in UNIX epoch time format.</p>"""
    disabled_date: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date and time at which the user was disabled for WorkMail usage, in UNIX epoch time format.</p>"""
    mailbox_provisioned_date: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date when the mailbox was created for the user.</p>"""
    mailbox_deprovisioned_date: NotRequired[
        "aws_sdk_workmail.types.timestamp.Timestamp"
    ]
    """<p>The date when the mailbox was removed for the user.</p>"""
    first_name: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>First name of the user.</p>"""
    last_name: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>Last name of the user.</p>"""
    hidden_from_global_address_list: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>If enabled, the user is hidden from the global address list.</p>"""
    initials: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>Initials of the user.</p>"""
    telephone: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>User's contact number.</p>"""
    street: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>Street where the user is located.</p>"""
    job_title: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>Job title of the user.</p>"""
    city: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>City where the user is located.</p>"""
    company: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>Company of the user.</p>"""
    zip_code: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>Zip code of the user.</p>"""
    department: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>Department of the user.</p>"""
    country: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>Country where the user is located.</p>"""
    office: NotRequired["aws_sdk_workmail.types.user_attribute.UserAttribute"]
    """<p>Office where the user is located.</p>"""
    identity_provider_user_id: NotRequired[
        "aws_sdk_workmail.types.identity_provider_user_id.IdentityProviderUserId"
    ]
    """<p>User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.</p>"""
    identity_provider_identity_store_id: NotRequired[
        "aws_sdk_workmail.types.identity_provider_identity_store_id.IdentityProviderIdentityStoreId"
    ]
    """<p> Identity Store ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "email" in value:
        out["Email"] = value["email"]
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
    if "mailbox_provisioned_date" in value:
        import aws_sdk_workmail.types.timestamp

        out["MailboxProvisionedDate"] = (
            aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
                value["mailbox_provisioned_date"]
            )
        )
    if "mailbox_deprovisioned_date" in value:
        import aws_sdk_workmail.types.timestamp

        out["MailboxDeprovisionedDate"] = (
            aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
                value["mailbox_deprovisioned_date"]
            )
        )
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    out["HiddenFromGlobalAddressList"] = value.get(
        "hidden_from_global_address_list", False
    )
    if "initials" in value:
        out["Initials"] = value["initials"]
    if "telephone" in value:
        out["Telephone"] = value["telephone"]
    if "street" in value:
        out["Street"] = value["street"]
    if "job_title" in value:
        out["JobTitle"] = value["job_title"]
    if "city" in value:
        out["City"] = value["city"]
    if "company" in value:
        out["Company"] = value["company"]
    if "zip_code" in value:
        out["ZipCode"] = value["zip_code"]
    if "department" in value:
        out["Department"] = value["department"]
    if "country" in value:
        out["Country"] = value["country"]
    if "office" in value:
        out["Office"] = value["office"]
    if "identity_provider_user_id" in value:
        out["IdentityProviderUserId"] = value["identity_provider_user_id"]
    if "identity_provider_identity_store_id" in value:
        out["IdentityProviderIdentityStoreId"] = value[
            "identity_provider_identity_store_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserResponse:
    out: DescribeUserResponse = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Email" in data:
        out["email"] = data["Email"]
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
    if "MailboxProvisionedDate" in data:
        import aws_sdk_workmail.types.timestamp

        out["mailbox_provisioned_date"] = (
            aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
                data["MailboxProvisionedDate"]
            )
        )
    if "MailboxDeprovisionedDate" in data:
        import aws_sdk_workmail.types.timestamp

        out["mailbox_deprovisioned_date"] = (
            aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
                data["MailboxDeprovisionedDate"]
            )
        )
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    if "HiddenFromGlobalAddressList" in data:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    else:
        out["hidden_from_global_address_list"] = False
    if "Initials" in data:
        out["initials"] = data["Initials"]
    if "Telephone" in data:
        out["telephone"] = data["Telephone"]
    if "Street" in data:
        out["street"] = data["Street"]
    if "JobTitle" in data:
        out["job_title"] = data["JobTitle"]
    if "City" in data:
        out["city"] = data["City"]
    if "Company" in data:
        out["company"] = data["Company"]
    if "ZipCode" in data:
        out["zip_code"] = data["ZipCode"]
    if "Department" in data:
        out["department"] = data["Department"]
    if "Country" in data:
        out["country"] = data["Country"]
    if "Office" in data:
        out["office"] = data["Office"]
    if "IdentityProviderUserId" in data:
        out["identity_provider_user_id"] = data["IdentityProviderUserId"]
    if "IdentityProviderIdentityStoreId" in data:
        out["identity_provider_identity_store_id"] = data[
            "IdentityProviderIdentityStoreId"
        ]
    return out
