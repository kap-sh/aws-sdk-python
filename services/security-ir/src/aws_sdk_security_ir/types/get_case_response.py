"""Generated from Smithy shape ``com.amazonaws.securityir#GetCaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_security_ir.types.case_arn
    import aws_sdk_security_ir.types.case_attachments_list
    import aws_sdk_security_ir.types.case_description
    import aws_sdk_security_ir.types.case_metadata
    import aws_sdk_security_ir.types.case_status
    import aws_sdk_security_ir.types.case_title
    import aws_sdk_security_ir.types.closure_code
    import aws_sdk_security_ir.types.engagement_type
    import aws_sdk_security_ir.types.impacted_accounts
    import aws_sdk_security_ir.types.impacted_aws_region_list
    import aws_sdk_security_ir.types.impacted_services_list
    import aws_sdk_security_ir.types.pending_action
    import aws_sdk_security_ir.types.resolver_type
    import aws_sdk_security_ir.types.threat_actor_ip_list
    import aws_sdk_security_ir.types.watchers


class GetCaseResponse(TypedDict):
    title: NotRequired["aws_sdk_security_ir.types.case_title.CaseTitle"]
    """<p>Response element for GetCase that provides the case title.</p>"""
    case_arn: NotRequired["aws_sdk_security_ir.types.case_arn.CaseArn"]
    """<p>Response element for GetCase that provides the case ARN</p>"""
    description: NotRequired[
        "aws_sdk_security_ir.types.case_description.CaseDescription"
    ]
    """<p>Response element for GetCase that provides contents of the case description.</p>"""
    case_status: NotRequired["aws_sdk_security_ir.types.case_status.CaseStatus"]
    """<p>Response element for GetCase that provides the case status. Options for statuses include <code>Submitted | Detection and Analysis | Eradication, Containment and Recovery | Post-Incident Activities | Closed </code> </p>"""
    engagement_type: NotRequired[
        "aws_sdk_security_ir.types.engagement_type.EngagementType"
    ]
    """<p>Response element for GetCase that provides the engagement type. Options for engagement type include <code>Active Security Event | Investigations</code> </p>"""
    reported_incident_start_date: NotRequired["datetime.datetime"]
    """<p>Response element for GetCase that provides the customer provided incident start date.</p>"""
    actual_incident_start_date: NotRequired["datetime.datetime"]
    """<p>Response element for GetCase that provides the actual incident start date as identified by data analysis during the investigation. </p>"""
    impacted_aws_regions: NotRequired[
        "aws_sdk_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
    ]
    """<p>Response element for GetCase that provides the impacted regions.</p>"""
    threat_actor_ip_addresses: NotRequired[
        "aws_sdk_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
    ]
    """<p>Response element for GetCase that provides a list of suspicious IP addresses associated with unauthorized activity. </p>"""
    pending_action: NotRequired[
        "aws_sdk_security_ir.types.pending_action.PendingAction"
    ]
    """<p>Response element for GetCase that identifies the case is waiting on customer input.</p>"""
    impacted_accounts: NotRequired[
        "aws_sdk_security_ir.types.impacted_accounts.ImpactedAccounts"
    ]
    """<p>Response element for GetCase that provides a list of impacted accounts.</p>"""
    watchers: NotRequired["aws_sdk_security_ir.types.watchers.Watchers"]
    """<p>Response element for GetCase that provides a list of Watchers added to the case.</p>"""
    created_date: NotRequired["datetime.datetime"]
    """<p>Response element for GetCase that provides the date the case was created.</p>"""
    last_updated_date: NotRequired["datetime.datetime"]
    """<p>Response element for GetCase that provides the date a case was last modified.</p>"""
    closure_code: NotRequired["aws_sdk_security_ir.types.closure_code.ClosureCode"]
    """<p>Response element for GetCase that provides the summary code for why a case was closed.</p>"""
    resolver_type: NotRequired["aws_sdk_security_ir.types.resolver_type.ResolverType"]
    """<p>Response element for GetCase that provides the current resolver types.</p>"""
    impacted_services: NotRequired[
        "aws_sdk_security_ir.types.impacted_services_list.ImpactedServicesList"
    ]
    """<p>Response element for GetCase that provides a list of impacted services.</p>"""
    case_attachments: NotRequired[
        "aws_sdk_security_ir.types.case_attachments_list.CaseAttachmentsList"
    ]
    """<p>Response element for GetCase that provides a list of current case attachments.</p>"""
    closed_date: NotRequired["datetime.datetime"]
    """<p>Response element for GetCase that provides the date a specified case was closed.</p>"""
    case_metadata: NotRequired["aws_sdk_security_ir.types.case_metadata.CaseMetadata"]
    """<p>Case response metadata</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseResponse) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "case_arn" in value:
        out["caseArn"] = value["case_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "case_status" in value:
        import aws_sdk_security_ir.types.case_status

        out["caseStatus"] = aws_sdk_security_ir.types.case_status.serialize_json(
            value["case_status"]
        )
    if "engagement_type" in value:
        import aws_sdk_security_ir.types.engagement_type

        out["engagementType"] = (
            aws_sdk_security_ir.types.engagement_type.serialize_json(
                value["engagement_type"]
            )
        )
    if "reported_incident_start_date" in value:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["reportedIncidentStartDate"] = (
            aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
                value["reported_incident_start_date"]
            )
        )
    if "actual_incident_start_date" in value:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["actualIncidentStartDate"] = (
            aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
                value["actual_incident_start_date"]
            )
        )
    if "impacted_aws_regions" in value:
        import aws_sdk_security_ir.types.impacted_aws_region_list

        out["impactedAwsRegions"] = (
            aws_sdk_security_ir.types.impacted_aws_region_list.serialize_json(
                value["impacted_aws_regions"]
            )
        )
    if "threat_actor_ip_addresses" in value:
        import aws_sdk_security_ir.types.threat_actor_ip_list

        out["threatActorIpAddresses"] = (
            aws_sdk_security_ir.types.threat_actor_ip_list.serialize_json(
                value["threat_actor_ip_addresses"]
            )
        )
    if "pending_action" in value:
        import aws_sdk_security_ir.types.pending_action

        out["pendingAction"] = aws_sdk_security_ir.types.pending_action.serialize_json(
            value["pending_action"]
        )
    if "impacted_accounts" in value:
        import aws_sdk_security_ir.types.impacted_accounts

        out["impactedAccounts"] = (
            aws_sdk_security_ir.types.impacted_accounts.serialize_json(
                value["impacted_accounts"]
            )
        )
    if "watchers" in value:
        import aws_sdk_security_ir.types.watchers

        out["watchers"] = aws_sdk_security_ir.types.watchers.serialize_json(
            value["watchers"]
        )
    if "created_date" in value:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["createdDate"] = (
            aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "last_updated_date" in value:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["lastUpdatedDate"] = (
            aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "closure_code" in value:
        import aws_sdk_security_ir.types.closure_code

        out["closureCode"] = aws_sdk_security_ir.types.closure_code.serialize_json(
            value["closure_code"]
        )
    if "resolver_type" in value:
        import aws_sdk_security_ir.types.resolver_type

        out["resolverType"] = aws_sdk_security_ir.types.resolver_type.serialize_json(
            value["resolver_type"]
        )
    if "impacted_services" in value:
        import aws_sdk_security_ir.types.impacted_services_list

        out["impactedServices"] = (
            aws_sdk_security_ir.types.impacted_services_list.serialize_json(
                value["impacted_services"]
            )
        )
    if "case_attachments" in value:
        import aws_sdk_security_ir.types.case_attachments_list

        out["caseAttachments"] = (
            aws_sdk_security_ir.types.case_attachments_list.serialize_json(
                value["case_attachments"]
            )
        )
    if "closed_date" in value:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["closedDate"] = aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
            value["closed_date"]
        )
    if "case_metadata" in value:
        import aws_sdk_security_ir.types.case_metadata

        out["caseMetadata"] = aws_sdk_security_ir.types.case_metadata.serialize_json(
            value["case_metadata"]
        )
    return out


def deserialize_json(data: dict) -> GetCaseResponse:
    out: GetCaseResponse = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    if "caseArn" in data:
        out["case_arn"] = data["caseArn"]
    if "description" in data:
        out["description"] = data["description"]
    if "caseStatus" in data:
        import aws_sdk_security_ir.types.case_status

        out["case_status"] = aws_sdk_security_ir.types.case_status.deserialize_json(
            data["caseStatus"]
        )
    if "engagementType" in data:
        import aws_sdk_security_ir.types.engagement_type

        out["engagement_type"] = (
            aws_sdk_security_ir.types.engagement_type.deserialize_json(
                data["engagementType"]
            )
        )
    if "reportedIncidentStartDate" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["reported_incident_start_date"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["reportedIncidentStartDate"]
            )
        )
    if "actualIncidentStartDate" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["actual_incident_start_date"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["actualIncidentStartDate"]
            )
        )
    if "impactedAwsRegions" in data:
        import aws_sdk_security_ir.types.impacted_aws_region_list

        out["impacted_aws_regions"] = (
            aws_sdk_security_ir.types.impacted_aws_region_list.deserialize_json(
                data["impactedAwsRegions"]
            )
        )
    if "threatActorIpAddresses" in data:
        import aws_sdk_security_ir.types.threat_actor_ip_list

        out["threat_actor_ip_addresses"] = (
            aws_sdk_security_ir.types.threat_actor_ip_list.deserialize_json(
                data["threatActorIpAddresses"]
            )
        )
    if "pendingAction" in data:
        import aws_sdk_security_ir.types.pending_action

        out["pending_action"] = (
            aws_sdk_security_ir.types.pending_action.deserialize_json(
                data["pendingAction"]
            )
        )
    if "impactedAccounts" in data:
        import aws_sdk_security_ir.types.impacted_accounts

        out["impacted_accounts"] = (
            aws_sdk_security_ir.types.impacted_accounts.deserialize_json(
                data["impactedAccounts"]
            )
        )
    if "watchers" in data:
        import aws_sdk_security_ir.types.watchers

        out["watchers"] = aws_sdk_security_ir.types.watchers.deserialize_json(
            data["watchers"]
        )
    if "createdDate" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["created_date"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "lastUpdatedDate" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["last_updated_date"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "closureCode" in data:
        import aws_sdk_security_ir.types.closure_code

        out["closure_code"] = aws_sdk_security_ir.types.closure_code.deserialize_json(
            data["closureCode"]
        )
    if "resolverType" in data:
        import aws_sdk_security_ir.types.resolver_type

        out["resolver_type"] = aws_sdk_security_ir.types.resolver_type.deserialize_json(
            data["resolverType"]
        )
    if "impactedServices" in data:
        import aws_sdk_security_ir.types.impacted_services_list

        out["impacted_services"] = (
            aws_sdk_security_ir.types.impacted_services_list.deserialize_json(
                data["impactedServices"]
            )
        )
    if "caseAttachments" in data:
        import aws_sdk_security_ir.types.case_attachments_list

        out["case_attachments"] = (
            aws_sdk_security_ir.types.case_attachments_list.deserialize_json(
                data["caseAttachments"]
            )
        )
    if "closedDate" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["closed_date"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["closedDate"]
            )
        )
    if "caseMetadata" in data:
        import aws_sdk_security_ir.types.case_metadata

        out["case_metadata"] = aws_sdk_security_ir.types.case_metadata.deserialize_json(
            data["caseMetadata"]
        )
    return out
