"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_name_type
    import aws_sdk_sso_admin.types.application_provider_arn
    import aws_sdk_sso_admin.types.application_status
    import aws_sdk_sso_admin.types.client_token
    import aws_sdk_sso_admin.types.description
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.portal_options
    import aws_sdk_sso_admin.types.tag_list


class CreateApplicationRequest(TypedDict, closed=True):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    r"""<p>The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    application_provider_arn: (
        "aws_sdk_sso_admin.types.application_provider_arn.ApplicationProviderArn"
    )
    """<p>The ARN of the application provider under which the operation will run.</p>"""
    name: "aws_sdk_sso_admin.types.application_name_type.ApplicationNameType"
    """<p>The name of the .</p>"""
    description: NotRequired["aws_sdk_sso_admin.types.description.Description"]
    """<p>The description of the .</p>"""
    portal_options: NotRequired["aws_sdk_sso_admin.types.portal_options.PortalOptions"]
    """<p>A structure that describes the options for the portal associated with an application.</p>"""
    tags: NotRequired["aws_sdk_sso_admin.types.tag_list.TagList"]
    """<p>Specifies tags to be attached to the application.</p>"""
    status: NotRequired["aws_sdk_sso_admin.types.application_status.ApplicationStatus"]
    """<p>Specifies whether the application is enabled or disabled.</p>"""
    client_token: NotRequired["aws_sdk_sso_admin.types.client_token.ClientToken"]
    r"""<p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["ApplicationProviderArn"] = value["application_provider_arn"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "portal_options" in value:
        import aws_sdk_sso_admin.types.portal_options

        out["PortalOptions"] = (
            aws_sdk_sso_admin.types.portal_options.serialize_aws_json_1_1(
                value["portal_options"]
            )
        )
    if "tags" in value:
        import aws_sdk_sso_admin.types.tag_list

        out["Tags"] = aws_sdk_sso_admin.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "status" in value:
        import aws_sdk_sso_admin.types.application_status

        out["Status"] = (
            aws_sdk_sso_admin.types.application_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("CreateApplicationRequest.instance_arn required")
    if "ApplicationProviderArn" in data:
        out["application_provider_arn"] = data["ApplicationProviderArn"]
    else:
        raise DeserializationError(
            "CreateApplicationRequest.application_provider_arn required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateApplicationRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "PortalOptions" in data:
        import aws_sdk_sso_admin.types.portal_options

        out["portal_options"] = (
            aws_sdk_sso_admin.types.portal_options.deserialize_aws_json_1_1(
                data["PortalOptions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sso_admin.types.tag_list

        out["tags"] = aws_sdk_sso_admin.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "Status" in data:
        import aws_sdk_sso_admin.types.application_status

        out["status"] = (
            aws_sdk_sso_admin.types.application_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
