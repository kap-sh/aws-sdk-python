"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.amazon_resource_name
    import capo_workmail.types.boolean
    import capo_workmail.types.organization_id
    import capo_workmail.types.organization_name
    import capo_workmail.types.string
    import capo_workmail.types.timestamp
    import capo_workmail.types.work_mail_identifier


class DescribeOrganizationResponse(TypedDict, closed=True):
    organization_id: NotRequired["capo_workmail.types.organization_id.OrganizationId"]
    """<p>The identifier of an organization.</p>"""
    alias: NotRequired["capo_workmail.types.organization_name.OrganizationName"]
    """<p>The alias for an organization.</p>"""
    state: NotRequired["capo_workmail.types.string.String"]
    """<p>The state of an organization.</p>"""
    directory_id: NotRequired["capo_workmail.types.string.String"]
    """<p>The identifier for the directory associated with an WorkMail organization.</p>"""
    directory_type: NotRequired["capo_workmail.types.string.String"]
    """<p>The type of directory associated with the WorkMail organization.</p>"""
    default_mail_domain: NotRequired["capo_workmail.types.string.String"]
    """<p>The default mail domain associated with the organization.</p>"""
    completed_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date at which the organization became usable in the WorkMail context, in UNIX epoch time format.</p>"""
    error_message: NotRequired["capo_workmail.types.string.String"]
    """<p>(Optional) The error message indicating if unexpected behavior was encountered with regards to the organization.</p>"""
    arn: NotRequired["capo_workmail.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the organization.</p>"""
    migration_admin: NotRequired[
        "capo_workmail.types.work_mail_identifier.WorkMailIdentifier"
    ]
    """<p>The user ID of the migration admin if migration is enabled for the organization.</p>"""
    interoperability_enabled: "capo_workmail.types.boolean.Boolean"
    """<p>Indicates if interoperability is enabled for this organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOrganizationResponse) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "state" in value:
        out["State"] = value["state"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "directory_type" in value:
        out["DirectoryType"] = value["directory_type"]
    if "default_mail_domain" in value:
        out["DefaultMailDomain"] = value["default_mail_domain"]
    if "completed_date" in value:
        import capo_workmail.types.timestamp

        out["CompletedDate"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["completed_date"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "migration_admin" in value:
        out["MigrationAdmin"] = value["migration_admin"]
    out["InteroperabilityEnabled"] = value.get("interoperability_enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeOrganizationResponse:
    out: DescribeOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    if "State" in data:
        out["state"] = data["State"]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "DirectoryType" in data:
        out["directory_type"] = data["DirectoryType"]
    if "DefaultMailDomain" in data:
        out["default_mail_domain"] = data["DefaultMailDomain"]
    if "CompletedDate" in data:
        import capo_workmail.types.timestamp

        out["completed_date"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["CompletedDate"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "MigrationAdmin" in data:
        out["migration_admin"] = data["MigrationAdmin"]
    if "InteroperabilityEnabled" in data:
        out["interoperability_enabled"] = data["InteroperabilityEnabled"]
    else:
        out["interoperability_enabled"] = False
    return out
