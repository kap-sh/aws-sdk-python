"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ResourceTagMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.compliance_details
    import capo_resource_groups_tagging_api.types.resource_arn
    import capo_resource_groups_tagging_api.types.tag_list


class ResourceTagMapping(TypedDict, closed=True):
    resource_arn: NotRequired[
        "capo_resource_groups_tagging_api.types.resource_arn.ResourceARN"
    ]
    """<p>The ARN of the resource.</p>"""
    tags: NotRequired["capo_resource_groups_tagging_api.types.tag_list.TagList"]
    """<p>The tags that have been applied to one or more Amazon Web Services resources.</p>"""
    compliance_details: NotRequired[
        "capo_resource_groups_tagging_api.types.compliance_details.ComplianceDetails"
    ]
    """<p>Information that shows whether a resource is compliant with the effective tag policy, including details on any noncompliant tag keys.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTagMapping) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tags" in value:
        import capo_resource_groups_tagging_api.types.tag_list

        out["Tags"] = (
            capo_resource_groups_tagging_api.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "compliance_details" in value:
        import capo_resource_groups_tagging_api.types.compliance_details

        out["ComplianceDetails"] = (
            capo_resource_groups_tagging_api.types.compliance_details.serialize_aws_json_1_1(
                value["compliance_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTagMapping:
    out: ResourceTagMapping = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "Tags" in data:
        import capo_resource_groups_tagging_api.types.tag_list

        out["tags"] = (
            capo_resource_groups_tagging_api.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    if "ComplianceDetails" in data:
        import capo_resource_groups_tagging_api.types.compliance_details

        out["compliance_details"] = (
            capo_resource_groups_tagging_api.types.compliance_details.deserialize_aws_json_1_1(
                data["ComplianceDetails"]
            )
        )
    return out
