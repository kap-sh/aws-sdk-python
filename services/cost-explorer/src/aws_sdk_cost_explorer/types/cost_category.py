"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.arn
    import aws_sdk_cost_explorer.types.cost_category_name
    import aws_sdk_cost_explorer.types.cost_category_processing_status_list
    import aws_sdk_cost_explorer.types.cost_category_rule_version
    import aws_sdk_cost_explorer.types.cost_category_rules_list
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list
    import aws_sdk_cost_explorer.types.cost_category_value
    import aws_sdk_cost_explorer.types.zoned_date_time


class CostCategory(TypedDict, closed=True):
    cost_category_arn: "aws_sdk_cost_explorer.types.arn.Arn"
    """<p>The unique identifier for your cost category. </p>"""
    effective_start: "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    """<p>The effective start date of your cost category.</p>"""
    effective_end: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The effective end date of your cost category.</p>"""
    name: "aws_sdk_cost_explorer.types.cost_category_name.CostCategoryName"
    rule_version: (
        "aws_sdk_cost_explorer.types.cost_category_rule_version.CostCategoryRuleVersion"
    )
    rules: "aws_sdk_cost_explorer.types.cost_category_rules_list.CostCategoryRulesList"
    """<p>The rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that cost category value. </p>"""
    split_charge_rules: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list.CostCategorySplitChargeRulesList"
    ]
    """<p> The split charge rules that are used to allocate your charges between your cost category values. </p>"""
    processing_status: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_processing_status_list.CostCategoryProcessingStatusList"
    ]
    """<p>The list of processing statuses for Cost Management products for a specific cost category. </p>"""
    default_value: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_value.CostCategoryValue"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategory) -> dict:
    out: dict = {}
    out["CostCategoryArn"] = value["cost_category_arn"]
    out["EffectiveStart"] = value["effective_start"]
    if "effective_end" in value:
        out["EffectiveEnd"] = value["effective_end"]
    out["Name"] = value["name"]
    import aws_sdk_cost_explorer.types.cost_category_rule_version

    out["RuleVersion"] = (
        aws_sdk_cost_explorer.types.cost_category_rule_version.serialize_aws_json_1_1(
            value["rule_version"]
        )
    )
    import aws_sdk_cost_explorer.types.cost_category_rules_list

    out["Rules"] = (
        aws_sdk_cost_explorer.types.cost_category_rules_list.serialize_aws_json_1_1(
            value["rules"]
        )
    )
    if "split_charge_rules" in value:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list

        out["SplitChargeRules"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list.serialize_aws_json_1_1(
                value["split_charge_rules"]
            )
        )
    if "processing_status" in value:
        import aws_sdk_cost_explorer.types.cost_category_processing_status_list

        out["ProcessingStatus"] = (
            aws_sdk_cost_explorer.types.cost_category_processing_status_list.serialize_aws_json_1_1(
                value["processing_status"]
            )
        )
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategory:
    out: CostCategory = {}  # type: ignore[typeddict-item]
    if "CostCategoryArn" in data:
        out["cost_category_arn"] = data["CostCategoryArn"]
    else:
        raise DeserializationError("CostCategory.cost_category_arn required")
    if "EffectiveStart" in data:
        out["effective_start"] = data["EffectiveStart"]
    else:
        raise DeserializationError("CostCategory.effective_start required")
    if "EffectiveEnd" in data:
        out["effective_end"] = data["EffectiveEnd"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CostCategory.name required")
    if "RuleVersion" in data:
        import aws_sdk_cost_explorer.types.cost_category_rule_version

        out["rule_version"] = (
            aws_sdk_cost_explorer.types.cost_category_rule_version.deserialize_aws_json_1_1(
                data["RuleVersion"]
            )
        )
    else:
        raise DeserializationError("CostCategory.rule_version required")
    if "Rules" in data:
        import aws_sdk_cost_explorer.types.cost_category_rules_list

        out["rules"] = (
            aws_sdk_cost_explorer.types.cost_category_rules_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        raise DeserializationError("CostCategory.rules required")
    if "SplitChargeRules" in data:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list

        out["split_charge_rules"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list.deserialize_aws_json_1_1(
                data["SplitChargeRules"]
            )
        )
    if "ProcessingStatus" in data:
        import aws_sdk_cost_explorer.types.cost_category_processing_status_list

        out["processing_status"] = (
            aws_sdk_cost_explorer.types.cost_category_processing_status_list.deserialize_aws_json_1_1(
                data["ProcessingStatus"]
            )
        )
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    return out
