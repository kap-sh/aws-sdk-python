"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#Criteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.double_criteria_condition_list
    import aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list
    import aws_sdk_compute_optimizer_automation.types.resource_tags_criteria_condition_list
    import aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list


class Criteria(TypedDict, closed=True):
    region: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.StringCriteriaConditionList"
    ]
    """<p>Filter criteria for Amazon Web Services regions where resources must be located.</p>"""
    resource_arn: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.StringCriteriaConditionList"
    ]
    """<p>Filter criteria for specific resource ARNs to include or exclude.</p>"""
    ebs_volume_type: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.StringCriteriaConditionList"
    ]
    """<p>Filter criteria for EBS volume types, such as gp2, gp3, io1, io2, st1, or sc1.</p>"""
    ebs_volume_size_in_gib: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list.IntegerCriteriaConditionList"
    ]
    """<p>Filter criteria for EBS volume sizes in gibibytes (GiB).</p>"""
    estimated_monthly_savings: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.double_criteria_condition_list.DoubleCriteriaConditionList"
    ]
    """<p>Filter criteria for estimated monthly cost savings from the recommended action.</p>"""
    resource_tag: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.resource_tags_criteria_condition_list.ResourceTagsCriteriaConditionList"
    ]
    """<p>Filter criteria for resource tags, allowing filtering by tag key and value combinations.</p>"""
    look_back_period_in_days: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list.IntegerCriteriaConditionList"
    ]
    """<p>Filter criteria for the lookback period in days used to analyze resource utilization.</p>"""
    restart_needed: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.StringCriteriaConditionList"
    ]
    """<p>Filter criteria indicating whether the recommended action requires a resource restart.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Criteria) -> dict:
    out: dict = {}
    if "region" in value:
        import aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list

        out["region"] = (
            aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.serialize_aws_json_1_0(
                value["region"]
            )
        )
    if "resource_arn" in value:
        import aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list

        out["resourceArn"] = (
            aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.serialize_aws_json_1_0(
                value["resource_arn"]
            )
        )
    if "ebs_volume_type" in value:
        import aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list

        out["ebsVolumeType"] = (
            aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.serialize_aws_json_1_0(
                value["ebs_volume_type"]
            )
        )
    if "ebs_volume_size_in_gib" in value:
        import aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list

        out["ebsVolumeSizeInGib"] = (
            aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list.serialize_aws_json_1_0(
                value["ebs_volume_size_in_gib"]
            )
        )
    if "estimated_monthly_savings" in value:
        import aws_sdk_compute_optimizer_automation.types.double_criteria_condition_list

        out["estimatedMonthlySavings"] = (
            aws_sdk_compute_optimizer_automation.types.double_criteria_condition_list.serialize_aws_json_1_0(
                value["estimated_monthly_savings"]
            )
        )
    if "resource_tag" in value:
        import aws_sdk_compute_optimizer_automation.types.resource_tags_criteria_condition_list

        out["resourceTag"] = (
            aws_sdk_compute_optimizer_automation.types.resource_tags_criteria_condition_list.serialize_aws_json_1_0(
                value["resource_tag"]
            )
        )
    if "look_back_period_in_days" in value:
        import aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list

        out["lookBackPeriodInDays"] = (
            aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list.serialize_aws_json_1_0(
                value["look_back_period_in_days"]
            )
        )
    if "restart_needed" in value:
        import aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list

        out["restartNeeded"] = (
            aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.serialize_aws_json_1_0(
                value["restart_needed"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Criteria:
    out: Criteria = {}  # type: ignore[typeddict-item]
    if "region" in data:
        import aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list

        out["region"] = (
            aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_aws_json_1_0(
                data["region"]
            )
        )
    if "resourceArn" in data:
        import aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list

        out["resource_arn"] = (
            aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_aws_json_1_0(
                data["resourceArn"]
            )
        )
    if "ebsVolumeType" in data:
        import aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list

        out["ebs_volume_type"] = (
            aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_aws_json_1_0(
                data["ebsVolumeType"]
            )
        )
    if "ebsVolumeSizeInGib" in data:
        import aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list

        out["ebs_volume_size_in_gib"] = (
            aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list.deserialize_aws_json_1_0(
                data["ebsVolumeSizeInGib"]
            )
        )
    if "estimatedMonthlySavings" in data:
        import aws_sdk_compute_optimizer_automation.types.double_criteria_condition_list

        out["estimated_monthly_savings"] = (
            aws_sdk_compute_optimizer_automation.types.double_criteria_condition_list.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    if "resourceTag" in data:
        import aws_sdk_compute_optimizer_automation.types.resource_tags_criteria_condition_list

        out["resource_tag"] = (
            aws_sdk_compute_optimizer_automation.types.resource_tags_criteria_condition_list.deserialize_aws_json_1_0(
                data["resourceTag"]
            )
        )
    if "lookBackPeriodInDays" in data:
        import aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list

        out["look_back_period_in_days"] = (
            aws_sdk_compute_optimizer_automation.types.integer_criteria_condition_list.deserialize_aws_json_1_0(
                data["lookBackPeriodInDays"]
            )
        )
    if "restartNeeded" in data:
        import aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list

        out["restart_needed"] = (
            aws_sdk_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_aws_json_1_0(
                data["restartNeeded"]
            )
        )
    return out
