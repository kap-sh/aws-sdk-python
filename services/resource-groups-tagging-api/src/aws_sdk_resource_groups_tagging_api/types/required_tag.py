"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#RequiredTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.cloud_formation_resource_types
    import aws_sdk_resource_groups_tagging_api.types.reporting_tag_keys
    import aws_sdk_resource_groups_tagging_api.types.resource_type


class RequiredTag(TypedDict, closed=True):
    resource_type: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.resource_type.ResourceType"
    ]
    """<p>Describes the resource type for the required tag keys.</p>"""
    cloud_formation_resource_types: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.cloud_formation_resource_types.CloudFormationResourceTypes"
    ]
    """<p>Describes the CloudFormation resource type assigned the required tag keys.</p>"""
    reporting_tag_keys: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.reporting_tag_keys.ReportingTagKeys"
    ]
    """<p>These tag keys are marked as <code>required</code> in the <code>report_required_tag_for</code> block of the effective tag policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequiredTag) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "cloud_formation_resource_types" in value:
        import aws_sdk_resource_groups_tagging_api.types.cloud_formation_resource_types

        out["CloudFormationResourceTypes"] = (
            aws_sdk_resource_groups_tagging_api.types.cloud_formation_resource_types.serialize_aws_json_1_1(
                value["cloud_formation_resource_types"]
            )
        )
    if "reporting_tag_keys" in value:
        import aws_sdk_resource_groups_tagging_api.types.reporting_tag_keys

        out["ReportingTagKeys"] = (
            aws_sdk_resource_groups_tagging_api.types.reporting_tag_keys.serialize_aws_json_1_1(
                value["reporting_tag_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequiredTag:
    out: RequiredTag = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "CloudFormationResourceTypes" in data:
        import aws_sdk_resource_groups_tagging_api.types.cloud_formation_resource_types

        out["cloud_formation_resource_types"] = (
            aws_sdk_resource_groups_tagging_api.types.cloud_formation_resource_types.deserialize_aws_json_1_1(
                data["CloudFormationResourceTypes"]
            )
        )
    if "ReportingTagKeys" in data:
        import aws_sdk_resource_groups_tagging_api.types.reporting_tag_keys

        out["reporting_tag_keys"] = (
            aws_sdk_resource_groups_tagging_api.types.reporting_tag_keys.deserialize_aws_json_1_1(
                data["ReportingTagKeys"]
            )
        )
    return out
