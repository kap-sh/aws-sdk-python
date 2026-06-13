"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.account_id
    import aws_sdk_resiliencehubv2.types.achievability
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.assessment_status
    import aws_sdk_resiliencehubv2.types.associated_system_list
    import aws_sdk_resiliencehubv2.types.dependency_discovery_config
    import aws_sdk_resiliencehubv2.types.entity_name
    import aws_sdk_resiliencehubv2.types.organization_id
    import aws_sdk_resiliencehubv2.types.ou_id
    import aws_sdk_resiliencehubv2.types.region_list


class ServiceSummary(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    name: "aws_sdk_resiliencehubv2.types.entity_name.EntityName"
    associated_systems: NotRequired[
        "aws_sdk_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
    ]
    """<p>The systems associated with the service.</p>"""
    regions: NotRequired["aws_sdk_resiliencehubv2.types.region_list.RegionList"]
    """<p>The AWS Regions where the service operates.</p>"""
    policy_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    assessment_status: NotRequired[
        "aws_sdk_resiliencehubv2.types.assessment_status.AssessmentStatus"
    ]
    """<p>The current assessment status of the service.</p>"""
    open_findings_count: NotRequired["int"]
    """<p>The number of open findings.</p>"""
    resolved_findings_count: NotRequired["int"]
    """<p>The number of resolved findings.</p>"""
    dependency_discovery: NotRequired[
        "aws_sdk_resiliencehubv2.types.dependency_discovery_config.DependencyDiscoveryConfig"
    ]
    """<p>The dependency discovery configuration.</p>"""
    achievability: NotRequired[
        "aws_sdk_resiliencehubv2.types.achievability.Achievability"
    ]
    """<p>The achievability status of the service's resilience targets.</p>"""
    organization_id: NotRequired[
        "aws_sdk_resiliencehubv2.types.organization_id.OrganizationId"
    ]
    """<p>Displayed only if caller has access.</p>"""
    ou_id: NotRequired["aws_sdk_resiliencehubv2.types.ou_id.OuId"]
    """<p>Displayed only if caller has access.</p>"""
    account_id: NotRequired["aws_sdk_resiliencehubv2.types.account_id.AccountId"]
    """<p>Displayed only if caller has access.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceSummary) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["name"] = value["name"]
    if "associated_systems" in value:
        import aws_sdk_resiliencehubv2.types.associated_system_list

        out["associatedSystems"] = (
            aws_sdk_resiliencehubv2.types.associated_system_list.serialize_json(
                value["associated_systems"]
            )
        )
    if "regions" in value:
        import aws_sdk_resiliencehubv2.types.region_list

        out["regions"] = aws_sdk_resiliencehubv2.types.region_list.serialize_json(
            value["regions"]
        )
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "assessment_status" in value:
        import aws_sdk_resiliencehubv2.types.assessment_status

        out["assessmentStatus"] = (
            aws_sdk_resiliencehubv2.types.assessment_status.serialize_json(
                value["assessment_status"]
            )
        )
    if "open_findings_count" in value:
        out["openFindingsCount"] = value["open_findings_count"]
    if "resolved_findings_count" in value:
        out["resolvedFindingsCount"] = value["resolved_findings_count"]
    if "dependency_discovery" in value:
        import aws_sdk_resiliencehubv2.types.dependency_discovery_config

        out["dependencyDiscovery"] = (
            aws_sdk_resiliencehubv2.types.dependency_discovery_config.serialize_json(
                value["dependency_discovery"]
            )
        )
    if "achievability" in value:
        import aws_sdk_resiliencehubv2.types.achievability

        out["achievability"] = (
            aws_sdk_resiliencehubv2.types.achievability.serialize_json(
                value["achievability"]
            )
        )
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    if "ou_id" in value:
        out["ouId"] = value["ou_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "created_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceSummary:
    out: ServiceSummary = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("ServiceSummary.service_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ServiceSummary.name required")
    if "associatedSystems" in data:
        import aws_sdk_resiliencehubv2.types.associated_system_list

        out["associated_systems"] = (
            aws_sdk_resiliencehubv2.types.associated_system_list.deserialize_json(
                data["associatedSystems"]
            )
        )
    if "regions" in data:
        import aws_sdk_resiliencehubv2.types.region_list

        out["regions"] = aws_sdk_resiliencehubv2.types.region_list.deserialize_json(
            data["regions"]
        )
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "assessmentStatus" in data:
        import aws_sdk_resiliencehubv2.types.assessment_status

        out["assessment_status"] = (
            aws_sdk_resiliencehubv2.types.assessment_status.deserialize_json(
                data["assessmentStatus"]
            )
        )
    if "openFindingsCount" in data:
        out["open_findings_count"] = data["openFindingsCount"]
    if "resolvedFindingsCount" in data:
        out["resolved_findings_count"] = data["resolvedFindingsCount"]
    if "dependencyDiscovery" in data:
        import aws_sdk_resiliencehubv2.types.dependency_discovery_config

        out["dependency_discovery"] = (
            aws_sdk_resiliencehubv2.types.dependency_discovery_config.deserialize_json(
                data["dependencyDiscovery"]
            )
        )
    if "achievability" in data:
        import aws_sdk_resiliencehubv2.types.achievability

        out["achievability"] = (
            aws_sdk_resiliencehubv2.types.achievability.deserialize_json(
                data["achievability"]
            )
        )
    if "organizationId" in data:
        out["organization_id"] = data["organizationId"]
    if "ouId" in data:
        out["ou_id"] = data["ouId"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "createdAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
