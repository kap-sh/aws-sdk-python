"""Generated from Smithy shape ``com.amazonaws.securityir#CreateCaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_security_ir.types.case_description
    import aws_sdk_security_ir.types.case_title
    import aws_sdk_security_ir.types.engagement_type
    import aws_sdk_security_ir.types.impacted_accounts
    import aws_sdk_security_ir.types.impacted_aws_region_list
    import aws_sdk_security_ir.types.impacted_services_list
    import aws_sdk_security_ir.types.resolver_type
    import aws_sdk_security_ir.types.tag_map
    import aws_sdk_security_ir.types.threat_actor_ip_list
    import aws_sdk_security_ir.types.watchers


class CreateCaseRequest(TypedDict):
    client_token: NotRequired["str"]
    """<note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>"""
    resolver_type: "aws_sdk_security_ir.types.resolver_type.ResolverType"
    """<p>Required element used in combination with CreateCase to identify the resolver type.</p>"""
    title: "aws_sdk_security_ir.types.case_title.CaseTitle"
    """<p>Required element used in combination with CreateCase to provide a title for the new case.</p>"""
    description: "aws_sdk_security_ir.types.case_description.CaseDescription"
    """<p>Required element used in combination with CreateCase</p> <p>to provide a description for the new case.</p>"""
    engagement_type: "aws_sdk_security_ir.types.engagement_type.EngagementType"
    """<p>Required element used in combination with CreateCase to provide an engagement type for the new cases. Available engagement types include Security Incident | Investigation </p>"""
    reported_incident_start_date: "datetime.datetime"
    """<p>Required element used in combination with CreateCase to provide an initial start date for the unauthorized activity. </p>"""
    impacted_accounts: "aws_sdk_security_ir.types.impacted_accounts.ImpactedAccounts"
    """<p>Required element used in combination with CreateCase to provide a list of impacted accounts.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>"""
    watchers: "aws_sdk_security_ir.types.watchers.Watchers"
    """<p>Required element used in combination with CreateCase to provide a list of entities to receive notifications for case updates. </p>"""
    threat_actor_ip_addresses: NotRequired[
        "aws_sdk_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
    ]
    """<p>An optional element used in combination with CreateCase to provide a list of suspicious internet protocol addresses associated with unauthorized activity. </p>"""
    impacted_services: NotRequired[
        "aws_sdk_security_ir.types.impacted_services_list.ImpactedServicesList"
    ]
    """<p>An optional element used in combination with CreateCase to provide a list of services impacted.</p>"""
    impacted_aws_regions: NotRequired[
        "aws_sdk_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
    ]
    """<p>An optional element used in combination with CreateCase to provide a list of impacted regions.</p>"""
    tags: NotRequired["aws_sdk_security_ir.types.tag_map.TagMap"]
    """<p>An optional element used in combination with CreateCase to add customer specified tags to a case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_security_ir.types.resolver_type

    out["resolverType"] = aws_sdk_security_ir.types.resolver_type.serialize_json(
        value["resolver_type"]
    )
    out["title"] = value["title"]
    out["description"] = value["description"]
    import aws_sdk_security_ir.types.engagement_type

    out["engagementType"] = aws_sdk_security_ir.types.engagement_type.serialize_json(
        value["engagement_type"]
    )
    import aws_sdk_security_ir.types._prelude.timestamp

    out["reportedIncidentStartDate"] = (
        aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
            value["reported_incident_start_date"]
        )
    )
    import aws_sdk_security_ir.types.impacted_accounts

    out["impactedAccounts"] = (
        aws_sdk_security_ir.types.impacted_accounts.serialize_json(
            value["impacted_accounts"]
        )
    )
    import aws_sdk_security_ir.types.watchers

    out["watchers"] = aws_sdk_security_ir.types.watchers.serialize_json(
        value["watchers"]
    )
    import aws_sdk_security_ir.types.threat_actor_ip_list

    out["threatActorIpAddresses"] = (
        aws_sdk_security_ir.types.threat_actor_ip_list.serialize_json(
            value.get("threat_actor_ip_addresses", [])
        )
    )
    import aws_sdk_security_ir.types.impacted_services_list

    out["impactedServices"] = (
        aws_sdk_security_ir.types.impacted_services_list.serialize_json(
            value.get("impacted_services", [])
        )
    )
    import aws_sdk_security_ir.types.impacted_aws_region_list

    out["impactedAwsRegions"] = (
        aws_sdk_security_ir.types.impacted_aws_region_list.serialize_json(
            value.get("impacted_aws_regions", [])
        )
    )
    if "tags" in value:
        import aws_sdk_security_ir.types.tag_map

        out["tags"] = aws_sdk_security_ir.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCaseRequest:
    out: CreateCaseRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "resolverType" in data:
        import aws_sdk_security_ir.types.resolver_type

        out["resolver_type"] = aws_sdk_security_ir.types.resolver_type.deserialize_json(
            data["resolverType"]
        )
    else:
        raise DeserializationError("CreateCaseRequest.resolver_type required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("CreateCaseRequest.title required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("CreateCaseRequest.description required")
    if "engagementType" in data:
        import aws_sdk_security_ir.types.engagement_type

        out["engagement_type"] = (
            aws_sdk_security_ir.types.engagement_type.deserialize_json(
                data["engagementType"]
            )
        )
    else:
        raise DeserializationError("CreateCaseRequest.engagement_type required")
    if "reportedIncidentStartDate" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["reported_incident_start_date"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["reportedIncidentStartDate"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCaseRequest.reported_incident_start_date required"
        )
    if "impactedAccounts" in data:
        import aws_sdk_security_ir.types.impacted_accounts

        out["impacted_accounts"] = (
            aws_sdk_security_ir.types.impacted_accounts.deserialize_json(
                data["impactedAccounts"]
            )
        )
    else:
        raise DeserializationError("CreateCaseRequest.impacted_accounts required")
    if "watchers" in data:
        import aws_sdk_security_ir.types.watchers

        out["watchers"] = aws_sdk_security_ir.types.watchers.deserialize_json(
            data["watchers"]
        )
    else:
        raise DeserializationError("CreateCaseRequest.watchers required")
    if "threatActorIpAddresses" in data:
        import aws_sdk_security_ir.types.threat_actor_ip_list

        out["threat_actor_ip_addresses"] = (
            aws_sdk_security_ir.types.threat_actor_ip_list.deserialize_json(
                data["threatActorIpAddresses"]
            )
        )
    else:
        out["threat_actor_ip_addresses"] = []
    if "impactedServices" in data:
        import aws_sdk_security_ir.types.impacted_services_list

        out["impacted_services"] = (
            aws_sdk_security_ir.types.impacted_services_list.deserialize_json(
                data["impactedServices"]
            )
        )
    else:
        out["impacted_services"] = []
    if "impactedAwsRegions" in data:
        import aws_sdk_security_ir.types.impacted_aws_region_list

        out["impacted_aws_regions"] = (
            aws_sdk_security_ir.types.impacted_aws_region_list.deserialize_json(
                data["impactedAwsRegions"]
            )
        )
    else:
        out["impacted_aws_regions"] = []
    if "tags" in data:
        import aws_sdk_security_ir.types.tag_map

        out["tags"] = aws_sdk_security_ir.types.tag_map.deserialize_json(data["tags"])
    return out
