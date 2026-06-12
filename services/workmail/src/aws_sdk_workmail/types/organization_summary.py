"""Generated from Smithy shape ``com.amazonaws.workmail#OrganizationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.domain_name
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.organization_name
    import aws_sdk_workmail.types.string


class OrganizationSummary(TypedDict):
    organization_id: NotRequired[
        "aws_sdk_workmail.types.organization_id.OrganizationId"
    ]
    """<p>The identifier associated with the organization.</p>"""
    alias: NotRequired["aws_sdk_workmail.types.organization_name.OrganizationName"]
    """<p>The alias associated with the organization.</p>"""
    default_mail_domain: NotRequired["aws_sdk_workmail.types.domain_name.DomainName"]
    """<p>The default email domain associated with the organization.</p>"""
    error_message: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>The error message associated with the organization. It is only present if unexpected behavior has occurred with regards to the organization. It provides insight or solutions regarding unexpected behavior.</p>"""
    state: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>The state associated with the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationSummary) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "default_mail_domain" in value:
        out["DefaultMailDomain"] = value["default_mail_domain"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationSummary:
    out: OrganizationSummary = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    if "DefaultMailDomain" in data:
        out["default_mail_domain"] = data["DefaultMailDomain"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "State" in data:
        out["state"] = data["State"]
    return out
