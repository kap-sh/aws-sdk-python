"""Generated from Smithy shape ``com.amazonaws.organizations#ListAWSServiceAccessForOrganizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.enabled_service_principals
    import aws_sdk_organizations.types.next_token


class ListAWSServiceAccessForOrganizationResponse(TypedDict):
    enabled_service_principals: NotRequired[
        "aws_sdk_organizations.types.enabled_service_principals.EnabledServicePrincipals"
    ]
    """<p>A list of the service principals for the services that are enabled to integrate with your organization. Each principal is a structure that includes the name and the date that it was enabled for integration with Organizations.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAWSServiceAccessForOrganizationResponse) -> dict:
    out: dict = {}
    if "enabled_service_principals" in value:
        import aws_sdk_organizations.types.enabled_service_principals

        out["EnabledServicePrincipals"] = (
            aws_sdk_organizations.types.enabled_service_principals.serialize_aws_json_1_1(
                value["enabled_service_principals"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAWSServiceAccessForOrganizationResponse:
    out: ListAWSServiceAccessForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "EnabledServicePrincipals" in data:
        import aws_sdk_organizations.types.enabled_service_principals

        out["enabled_service_principals"] = (
            aws_sdk_organizations.types.enabled_service_principals.deserialize_aws_json_1_1(
                data["EnabledServicePrincipals"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
