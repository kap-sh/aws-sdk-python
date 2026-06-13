"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateCaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_security_ir.types.case_description
    import aws_sdk_security_ir.types.case_id
    import aws_sdk_security_ir.types.case_metadata
    import aws_sdk_security_ir.types.case_title
    import aws_sdk_security_ir.types.engagement_type
    import aws_sdk_security_ir.types.impacted_accounts
    import aws_sdk_security_ir.types.impacted_aws_region_list
    import aws_sdk_security_ir.types.impacted_services_list
    import aws_sdk_security_ir.types.threat_actor_ip_list
    import aws_sdk_security_ir.types.watchers


class UpdateCaseRequest(TypedDict):
    case_id: "aws_sdk_security_ir.types.case_id.CaseId"
    """<p>Required element for UpdateCase to identify the case ID for updates.</p>"""
    title: NotRequired["aws_sdk_security_ir.types.case_title.CaseTitle"]
    """<p>Optional element for UpdateCase to provide content for the title field.</p>"""
    description: NotRequired[
        "aws_sdk_security_ir.types.case_description.CaseDescription"
    ]
    """<p>Optional element for UpdateCase to provide content for the description field.</p>"""
    reported_incident_start_date: NotRequired["datetime.datetime"]
    """<p>Optional element for UpdateCase to provide content for the customer reported incident start date field. </p>"""
    actual_incident_start_date: NotRequired["datetime.datetime"]
    """<p>Optional element for UpdateCase to provide content for the incident start date field.</p>"""
    engagement_type: NotRequired[
        "aws_sdk_security_ir.types.engagement_type.EngagementType"
    ]
    """<p>Optional element for UpdateCase to provide content for the engagement type field. <code>Available engagement types include Security Incident | Investigation</code>. </p>"""
    watchers_to_add: NotRequired["aws_sdk_security_ir.types.watchers.Watchers"]
    """<p>Optional element for UpdateCase to provide content to add additional watchers to a case.</p>"""
    watchers_to_delete: NotRequired["aws_sdk_security_ir.types.watchers.Watchers"]
    """<p>Optional element for UpdateCase to provide content to remove existing watchers from a case.</p>"""
    threat_actor_ip_addresses_to_add: NotRequired[
        "aws_sdk_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
    ]
    """<p>Optional element for UpdateCase to provide content to add additional suspicious IP addresses related to a case. </p>"""
    threat_actor_ip_addresses_to_delete: NotRequired[
        "aws_sdk_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
    ]
    """<p>Optional element for UpdateCase to provide content to remove suspicious IP addresses from a case.</p>"""
    impacted_services_to_add: NotRequired[
        "aws_sdk_security_ir.types.impacted_services_list.ImpactedServicesList"
    ]
    """<p>Optional element for UpdateCase to provide content to add services impacted.</p>"""
    impacted_services_to_delete: NotRequired[
        "aws_sdk_security_ir.types.impacted_services_list.ImpactedServicesList"
    ]
    """<p>Optional element for UpdateCase to provide content to remove services impacted.</p>"""
    impacted_aws_regions_to_add: NotRequired[
        "aws_sdk_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
    ]
    """<p>Optional element for UpdateCase to provide content to add regions impacted.</p>"""
    impacted_aws_regions_to_delete: NotRequired[
        "aws_sdk_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
    ]
    """<p>Optional element for UpdateCase to provide content to remove regions impacted.</p>"""
    impacted_accounts_to_add: NotRequired[
        "aws_sdk_security_ir.types.impacted_accounts.ImpactedAccounts"
    ]
    """<p>Optional element for UpdateCase to provide content to add accounts impacted.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>"""
    impacted_accounts_to_delete: NotRequired[
        "aws_sdk_security_ir.types.impacted_accounts.ImpactedAccounts"
    ]
    """<p>Optional element for UpdateCase to provide content to add accounts impacted.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>"""
    case_metadata: NotRequired["aws_sdk_security_ir.types.case_metadata.CaseMetadata"]
    """<p>Update the case request with case metadata</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCaseRequest) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
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
    if "engagement_type" in value:
        import aws_sdk_security_ir.types.engagement_type

        out["engagementType"] = (
            aws_sdk_security_ir.types.engagement_type.serialize_json(
                value["engagement_type"]
            )
        )
    if "watchers_to_add" in value:
        import aws_sdk_security_ir.types.watchers

        out["watchersToAdd"] = aws_sdk_security_ir.types.watchers.serialize_json(
            value["watchers_to_add"]
        )
    if "watchers_to_delete" in value:
        import aws_sdk_security_ir.types.watchers

        out["watchersToDelete"] = aws_sdk_security_ir.types.watchers.serialize_json(
            value["watchers_to_delete"]
        )
    if "threat_actor_ip_addresses_to_add" in value:
        import aws_sdk_security_ir.types.threat_actor_ip_list

        out["threatActorIpAddressesToAdd"] = (
            aws_sdk_security_ir.types.threat_actor_ip_list.serialize_json(
                value["threat_actor_ip_addresses_to_add"]
            )
        )
    if "threat_actor_ip_addresses_to_delete" in value:
        import aws_sdk_security_ir.types.threat_actor_ip_list

        out["threatActorIpAddressesToDelete"] = (
            aws_sdk_security_ir.types.threat_actor_ip_list.serialize_json(
                value["threat_actor_ip_addresses_to_delete"]
            )
        )
    if "impacted_services_to_add" in value:
        import aws_sdk_security_ir.types.impacted_services_list

        out["impactedServicesToAdd"] = (
            aws_sdk_security_ir.types.impacted_services_list.serialize_json(
                value["impacted_services_to_add"]
            )
        )
    if "impacted_services_to_delete" in value:
        import aws_sdk_security_ir.types.impacted_services_list

        out["impactedServicesToDelete"] = (
            aws_sdk_security_ir.types.impacted_services_list.serialize_json(
                value["impacted_services_to_delete"]
            )
        )
    if "impacted_aws_regions_to_add" in value:
        import aws_sdk_security_ir.types.impacted_aws_region_list

        out["impactedAwsRegionsToAdd"] = (
            aws_sdk_security_ir.types.impacted_aws_region_list.serialize_json(
                value["impacted_aws_regions_to_add"]
            )
        )
    if "impacted_aws_regions_to_delete" in value:
        import aws_sdk_security_ir.types.impacted_aws_region_list

        out["impactedAwsRegionsToDelete"] = (
            aws_sdk_security_ir.types.impacted_aws_region_list.serialize_json(
                value["impacted_aws_regions_to_delete"]
            )
        )
    if "impacted_accounts_to_add" in value:
        import aws_sdk_security_ir.types.impacted_accounts

        out["impactedAccountsToAdd"] = (
            aws_sdk_security_ir.types.impacted_accounts.serialize_json(
                value["impacted_accounts_to_add"]
            )
        )
    if "impacted_accounts_to_delete" in value:
        import aws_sdk_security_ir.types.impacted_accounts

        out["impactedAccountsToDelete"] = (
            aws_sdk_security_ir.types.impacted_accounts.serialize_json(
                value["impacted_accounts_to_delete"]
            )
        )
    if "case_metadata" in value:
        import aws_sdk_security_ir.types.case_metadata

        out["caseMetadata"] = aws_sdk_security_ir.types.case_metadata.serialize_json(
            value["case_metadata"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCaseRequest:
    out: UpdateCaseRequest = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    if "description" in data:
        out["description"] = data["description"]
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
    if "engagementType" in data:
        import aws_sdk_security_ir.types.engagement_type

        out["engagement_type"] = (
            aws_sdk_security_ir.types.engagement_type.deserialize_json(
                data["engagementType"]
            )
        )
    if "watchersToAdd" in data:
        import aws_sdk_security_ir.types.watchers

        out["watchers_to_add"] = aws_sdk_security_ir.types.watchers.deserialize_json(
            data["watchersToAdd"]
        )
    if "watchersToDelete" in data:
        import aws_sdk_security_ir.types.watchers

        out["watchers_to_delete"] = aws_sdk_security_ir.types.watchers.deserialize_json(
            data["watchersToDelete"]
        )
    if "threatActorIpAddressesToAdd" in data:
        import aws_sdk_security_ir.types.threat_actor_ip_list

        out["threat_actor_ip_addresses_to_add"] = (
            aws_sdk_security_ir.types.threat_actor_ip_list.deserialize_json(
                data["threatActorIpAddressesToAdd"]
            )
        )
    if "threatActorIpAddressesToDelete" in data:
        import aws_sdk_security_ir.types.threat_actor_ip_list

        out["threat_actor_ip_addresses_to_delete"] = (
            aws_sdk_security_ir.types.threat_actor_ip_list.deserialize_json(
                data["threatActorIpAddressesToDelete"]
            )
        )
    if "impactedServicesToAdd" in data:
        import aws_sdk_security_ir.types.impacted_services_list

        out["impacted_services_to_add"] = (
            aws_sdk_security_ir.types.impacted_services_list.deserialize_json(
                data["impactedServicesToAdd"]
            )
        )
    if "impactedServicesToDelete" in data:
        import aws_sdk_security_ir.types.impacted_services_list

        out["impacted_services_to_delete"] = (
            aws_sdk_security_ir.types.impacted_services_list.deserialize_json(
                data["impactedServicesToDelete"]
            )
        )
    if "impactedAwsRegionsToAdd" in data:
        import aws_sdk_security_ir.types.impacted_aws_region_list

        out["impacted_aws_regions_to_add"] = (
            aws_sdk_security_ir.types.impacted_aws_region_list.deserialize_json(
                data["impactedAwsRegionsToAdd"]
            )
        )
    if "impactedAwsRegionsToDelete" in data:
        import aws_sdk_security_ir.types.impacted_aws_region_list

        out["impacted_aws_regions_to_delete"] = (
            aws_sdk_security_ir.types.impacted_aws_region_list.deserialize_json(
                data["impactedAwsRegionsToDelete"]
            )
        )
    if "impactedAccountsToAdd" in data:
        import aws_sdk_security_ir.types.impacted_accounts

        out["impacted_accounts_to_add"] = (
            aws_sdk_security_ir.types.impacted_accounts.deserialize_json(
                data["impactedAccountsToAdd"]
            )
        )
    if "impactedAccountsToDelete" in data:
        import aws_sdk_security_ir.types.impacted_accounts

        out["impacted_accounts_to_delete"] = (
            aws_sdk_security_ir.types.impacted_accounts.deserialize_json(
                data["impactedAccountsToDelete"]
            )
        )
    if "caseMetadata" in data:
        import aws_sdk_security_ir.types.case_metadata

        out["case_metadata"] = aws_sdk_security_ir.types.case_metadata.deserialize_json(
            data["caseMetadata"]
        )
    return out
