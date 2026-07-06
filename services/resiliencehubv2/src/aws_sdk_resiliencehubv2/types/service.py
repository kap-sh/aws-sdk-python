"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#Service``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.account_id
    import aws_sdk_resiliencehubv2.types.achievability
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.assessment_cost
    import aws_sdk_resiliencehubv2.types.assessment_status
    import aws_sdk_resiliencehubv2.types.associated_system_list
    import aws_sdk_resiliencehubv2.types.dependency_discovery_config
    import aws_sdk_resiliencehubv2.types.effective_policy_values
    import aws_sdk_resiliencehubv2.types.entity_name
    import aws_sdk_resiliencehubv2.types.kms_key_id
    import aws_sdk_resiliencehubv2.types.long_description
    import aws_sdk_resiliencehubv2.types.organization_id
    import aws_sdk_resiliencehubv2.types.ou_id
    import aws_sdk_resiliencehubv2.types.permission_model
    import aws_sdk_resiliencehubv2.types.region_list
    import aws_sdk_resiliencehubv2.types.resource_discovery_status
    import aws_sdk_resiliencehubv2.types.service_report_configuration
    import aws_sdk_resiliencehubv2.types.tag_map


class Service(TypedDict, closed=True):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    name: "aws_sdk_resiliencehubv2.types.entity_name.EntityName"
    description: NotRequired[
        "aws_sdk_resiliencehubv2.types.long_description.LongDescription"
    ]
    associated_systems: NotRequired[
        "aws_sdk_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
    ]
    """<p>The systems associated with the service.</p>"""
    policy_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    regions: NotRequired["aws_sdk_resiliencehubv2.types.region_list.RegionList"]
    """<p>The AWS Regions where the service operates.</p>"""
    permission_model: NotRequired[
        "aws_sdk_resiliencehubv2.types.permission_model.PermissionModel"
    ]
    """<p>The permission model for the service.</p>"""
    dependency_discovery: NotRequired[
        "aws_sdk_resiliencehubv2.types.dependency_discovery_config.DependencyDiscoveryConfig"
    ]
    """<p>The dependency discovery configuration for the service.</p>"""
    effective_policy_values: NotRequired[
        "aws_sdk_resiliencehubv2.types.effective_policy_values.EffectivePolicyValues"
    ]
    """<p>The effective policy values for the service.</p>"""
    achievability: NotRequired[
        "aws_sdk_resiliencehubv2.types.achievability.Achievability"
    ]
    """<p>The achievability status of the service's resilience targets.</p>"""
    report_configuration: NotRequired[
        "aws_sdk_resiliencehubv2.types.service_report_configuration.ServiceReportConfiguration"
    ]
    kms_key_id: NotRequired["aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    tags: NotRequired["aws_sdk_resiliencehubv2.types.tag_map.TagMap"]
    estimated_assessment_cost: NotRequired[
        "aws_sdk_resiliencehubv2.types.assessment_cost.AssessmentCost"
    ]
    """<p>The estimated cost of running an assessment on the service.</p>"""
    resource_discovery: NotRequired[
        "aws_sdk_resiliencehubv2.types.resource_discovery_status.ResourceDiscoveryStatus"
    ]
    """<p>The resource discovery status for the service.</p>"""
    assessment_status: NotRequired[
        "aws_sdk_resiliencehubv2.types.assessment_status.AssessmentStatus"
    ]
    """<p>The current assessment status of the service.</p>"""
    rerun_assessment: NotRequired["bool"]
    """<p>Indicates whether the assessment should be rerun.</p>"""
    open_findings_count: NotRequired["int"]
    """<p>The number of open findings for the service.</p>"""
    resolved_findings_count: NotRequired["int"]
    """<p>The number of resolved findings for the service.</p>"""
    organization_id: NotRequired[
        "aws_sdk_resiliencehubv2.types.organization_id.OrganizationId"
    ]
    """<p>The AWS Organizations identifier for the service.</p>"""
    ou_id: NotRequired["aws_sdk_resiliencehubv2.types.ou_id.OuId"]
    """<p>The organizational unit (OU) identifier for the service.</p>"""
    account_id: NotRequired["aws_sdk_resiliencehubv2.types.account_id.AccountId"]
    """<p>The AWS account ID that owns the service.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Service) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "associated_systems" in value:
        import aws_sdk_resiliencehubv2.types.associated_system_list

        out["associatedSystems"] = (
            aws_sdk_resiliencehubv2.types.associated_system_list.serialize_json(
                value["associated_systems"]
            )
        )
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "regions" in value:
        import aws_sdk_resiliencehubv2.types.region_list

        out["regions"] = aws_sdk_resiliencehubv2.types.region_list.serialize_json(
            value["regions"]
        )
    if "permission_model" in value:
        import aws_sdk_resiliencehubv2.types.permission_model

        out["permissionModel"] = (
            aws_sdk_resiliencehubv2.types.permission_model.serialize_json(
                value["permission_model"]
            )
        )
    if "dependency_discovery" in value:
        import aws_sdk_resiliencehubv2.types.dependency_discovery_config

        out["dependencyDiscovery"] = (
            aws_sdk_resiliencehubv2.types.dependency_discovery_config.serialize_json(
                value["dependency_discovery"]
            )
        )
    if "effective_policy_values" in value:
        import aws_sdk_resiliencehubv2.types.effective_policy_values

        out["effectivePolicyValues"] = (
            aws_sdk_resiliencehubv2.types.effective_policy_values.serialize_json(
                value["effective_policy_values"]
            )
        )
    if "achievability" in value:
        import aws_sdk_resiliencehubv2.types.achievability

        out["achievability"] = (
            aws_sdk_resiliencehubv2.types.achievability.serialize_json(
                value["achievability"]
            )
        )
    if "report_configuration" in value:
        import aws_sdk_resiliencehubv2.types.service_report_configuration

        out["reportConfiguration"] = (
            aws_sdk_resiliencehubv2.types.service_report_configuration.serialize_json(
                value["report_configuration"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.serialize_json(
            value["tags"]
        )
    if "estimated_assessment_cost" in value:
        import aws_sdk_resiliencehubv2.types.assessment_cost

        out["estimatedAssessmentCost"] = (
            aws_sdk_resiliencehubv2.types.assessment_cost.serialize_json(
                value["estimated_assessment_cost"]
            )
        )
    if "resource_discovery" in value:
        import aws_sdk_resiliencehubv2.types.resource_discovery_status

        out["resourceDiscovery"] = (
            aws_sdk_resiliencehubv2.types.resource_discovery_status.serialize_json(
                value["resource_discovery"]
            )
        )
    if "assessment_status" in value:
        import aws_sdk_resiliencehubv2.types.assessment_status

        out["assessmentStatus"] = (
            aws_sdk_resiliencehubv2.types.assessment_status.serialize_json(
                value["assessment_status"]
            )
        )
    if "rerun_assessment" in value:
        out["rerunAssessment"] = value["rerun_assessment"]
    if "open_findings_count" in value:
        out["openFindingsCount"] = value["open_findings_count"]
    if "resolved_findings_count" in value:
        out["resolvedFindingsCount"] = value["resolved_findings_count"]
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


def deserialize_json(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("Service.service_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Service.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "associatedSystems" in data:
        import aws_sdk_resiliencehubv2.types.associated_system_list

        out["associated_systems"] = (
            aws_sdk_resiliencehubv2.types.associated_system_list.deserialize_json(
                data["associatedSystems"]
            )
        )
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "regions" in data:
        import aws_sdk_resiliencehubv2.types.region_list

        out["regions"] = aws_sdk_resiliencehubv2.types.region_list.deserialize_json(
            data["regions"]
        )
    if "permissionModel" in data:
        import aws_sdk_resiliencehubv2.types.permission_model

        out["permission_model"] = (
            aws_sdk_resiliencehubv2.types.permission_model.deserialize_json(
                data["permissionModel"]
            )
        )
    if "dependencyDiscovery" in data:
        import aws_sdk_resiliencehubv2.types.dependency_discovery_config

        out["dependency_discovery"] = (
            aws_sdk_resiliencehubv2.types.dependency_discovery_config.deserialize_json(
                data["dependencyDiscovery"]
            )
        )
    if "effectivePolicyValues" in data:
        import aws_sdk_resiliencehubv2.types.effective_policy_values

        out["effective_policy_values"] = (
            aws_sdk_resiliencehubv2.types.effective_policy_values.deserialize_json(
                data["effectivePolicyValues"]
            )
        )
    if "achievability" in data:
        import aws_sdk_resiliencehubv2.types.achievability

        out["achievability"] = (
            aws_sdk_resiliencehubv2.types.achievability.deserialize_json(
                data["achievability"]
            )
        )
    if "reportConfiguration" in data:
        import aws_sdk_resiliencehubv2.types.service_report_configuration

        out["report_configuration"] = (
            aws_sdk_resiliencehubv2.types.service_report_configuration.deserialize_json(
                data["reportConfiguration"]
            )
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "tags" in data:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "estimatedAssessmentCost" in data:
        import aws_sdk_resiliencehubv2.types.assessment_cost

        out["estimated_assessment_cost"] = (
            aws_sdk_resiliencehubv2.types.assessment_cost.deserialize_json(
                data["estimatedAssessmentCost"]
            )
        )
    if "resourceDiscovery" in data:
        import aws_sdk_resiliencehubv2.types.resource_discovery_status

        out["resource_discovery"] = (
            aws_sdk_resiliencehubv2.types.resource_discovery_status.deserialize_json(
                data["resourceDiscovery"]
            )
        )
    if "assessmentStatus" in data:
        import aws_sdk_resiliencehubv2.types.assessment_status

        out["assessment_status"] = (
            aws_sdk_resiliencehubv2.types.assessment_status.deserialize_json(
                data["assessmentStatus"]
            )
        )
    if "rerunAssessment" in data:
        out["rerun_assessment"] = data["rerunAssessment"]
    if "openFindingsCount" in data:
        out["open_findings_count"] = data["openFindingsCount"]
    if "resolvedFindingsCount" in data:
        out["resolved_findings_count"] = data["resolvedFindingsCount"]
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
