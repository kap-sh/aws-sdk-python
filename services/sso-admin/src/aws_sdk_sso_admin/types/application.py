"""Generated from Smithy shape ``com.amazonaws.ssoadmin#Application``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_id
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.application_name_type
    import aws_sdk_sso_admin.types.application_provider_arn
    import aws_sdk_sso_admin.types.application_status
    import aws_sdk_sso_admin.types.date
    import aws_sdk_sso_admin.types.description
    import aws_sdk_sso_admin.types.identity_store_arn
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.portal_options
    import aws_sdk_sso_admin.types.region_name


class Application(TypedDict, closed=True):
    application_arn: NotRequired[
        "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    ]
    """<p>The ARN of the application.</p>"""
    application_provider_arn: NotRequired[
        "aws_sdk_sso_admin.types.application_provider_arn.ApplicationProviderArn"
    ]
    """<p>The ARN of the application provider for this application.</p>"""
    name: NotRequired[
        "aws_sdk_sso_admin.types.application_name_type.ApplicationNameType"
    ]
    """<p>The name of the application.</p>"""
    application_account: NotRequired["aws_sdk_sso_admin.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID number of the application.</p>"""
    instance_arn: NotRequired["aws_sdk_sso_admin.types.instance_arn.InstanceArn"]
    """<p>The ARN of the instance of IAM Identity Center that is configured with this application.</p>"""
    identity_store_arn: NotRequired[
        "aws_sdk_sso_admin.types.identity_store_arn.IdentityStoreArn"
    ]
    """<p>The ARN of the identity store that is connected to the instance of IAM Identity Center.</p>"""
    status: NotRequired["aws_sdk_sso_admin.types.application_status.ApplicationStatus"]
    """<p>The current status of the application in this instance of IAM Identity Center.</p>"""
    portal_options: NotRequired["aws_sdk_sso_admin.types.portal_options.PortalOptions"]
    """<p>A structure that describes the options for the access portal associated with this application.</p>"""
    description: NotRequired["aws_sdk_sso_admin.types.description.Description"]
    """<p>The description of the application.</p>"""
    created_date: NotRequired["aws_sdk_sso_admin.types.date.Date"]
    """<p>The date and time when the application was originally created.</p>"""
    created_from: NotRequired["aws_sdk_sso_admin.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where the application was created in IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Application) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "application_provider_arn" in value:
        out["ApplicationProviderArn"] = value["application_provider_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "application_account" in value:
        out["ApplicationAccount"] = value["application_account"]
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "identity_store_arn" in value:
        out["IdentityStoreArn"] = value["identity_store_arn"]
    if "status" in value:
        import aws_sdk_sso_admin.types.application_status

        out["Status"] = (
            aws_sdk_sso_admin.types.application_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "portal_options" in value:
        import aws_sdk_sso_admin.types.portal_options

        out["PortalOptions"] = (
            aws_sdk_sso_admin.types.portal_options.serialize_aws_json_1_1(
                value["portal_options"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_date" in value:
        import aws_sdk_sso_admin.types.date

        out["CreatedDate"] = aws_sdk_sso_admin.types.date.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "created_from" in value:
        out["CreatedFrom"] = value["created_from"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    if "ApplicationProviderArn" in data:
        out["application_provider_arn"] = data["ApplicationProviderArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ApplicationAccount" in data:
        out["application_account"] = data["ApplicationAccount"]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    if "IdentityStoreArn" in data:
        out["identity_store_arn"] = data["IdentityStoreArn"]
    if "Status" in data:
        import aws_sdk_sso_admin.types.application_status

        out["status"] = (
            aws_sdk_sso_admin.types.application_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "PortalOptions" in data:
        import aws_sdk_sso_admin.types.portal_options

        out["portal_options"] = (
            aws_sdk_sso_admin.types.portal_options.deserialize_aws_json_1_1(
                data["PortalOptions"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedDate" in data:
        import aws_sdk_sso_admin.types.date

        out["created_date"] = aws_sdk_sso_admin.types.date.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if "CreatedFrom" in data:
        out["created_from"] = data["CreatedFrom"]
    return out
