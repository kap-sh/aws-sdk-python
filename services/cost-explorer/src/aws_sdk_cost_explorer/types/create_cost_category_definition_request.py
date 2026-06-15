"""Generated from Smithy shape ``com.amazonaws.costexplorer#CreateCostCategoryDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_name
    import aws_sdk_cost_explorer.types.cost_category_rule_version
    import aws_sdk_cost_explorer.types.cost_category_rules_list
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list
    import aws_sdk_cost_explorer.types.cost_category_value
    import aws_sdk_cost_explorer.types.resource_tag_list
    import aws_sdk_cost_explorer.types.zoned_date_time


class CreateCostCategoryDefinitionRequest(TypedDict):
    name: "aws_sdk_cost_explorer.types.cost_category_name.CostCategoryName"
    effective_start: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The cost category's effective start date. It can only be a billing start date (first day of the month). If the date isn't provided, it's the first day of the current month. Dates can't be before the previous twelve months, or in the future.</p>"""
    rule_version: (
        "aws_sdk_cost_explorer.types.cost_category_rule_version.CostCategoryRuleVersion"
    )
    rules: "aws_sdk_cost_explorer.types.cost_category_rules_list.CostCategoryRulesList"
    r"""<p>The cost category rules used to categorize costs. For more information, see <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html\">CostCategoryRule</a>.</p>"""
    default_value: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_value.CostCategoryValue"
    ]
    split_charge_rules: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list.CostCategorySplitChargeRulesList"
    ]
    """<p> The split charge rules used to allocate your charges between your cost category values. </p>"""
    resource_tags: NotRequired[
        "aws_sdk_cost_explorer.types.resource_tag_list.ResourceTagList"
    ]
    r"""<p>An optional list of tags to associate with the specified <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html\"> <code>CostCategory</code> </a>. You can use resource tags to control access to your <code>cost category</code> using IAM policies.</p> <p>Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags:</p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services use</p> </li> <li> <p>The maximum length of a key is 128 characters</p> </li> <li> <p>The maximum length of a value is 256 characters</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code> </p> </li> <li> <p>Keys and values are case sensitive</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces</p> </li> <li> <p>Don’t use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services use</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCostCategoryDefinitionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "effective_start" in value:
        out["EffectiveStart"] = value["effective_start"]
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
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "split_charge_rules" in value:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list

        out["SplitChargeRules"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list.serialize_aws_json_1_1(
                value["split_charge_rules"]
            )
        )
    if "resource_tags" in value:
        import aws_sdk_cost_explorer.types.resource_tag_list

        out["ResourceTags"] = (
            aws_sdk_cost_explorer.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCostCategoryDefinitionRequest:
    out: CreateCostCategoryDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateCostCategoryDefinitionRequest.name required")
    if "EffectiveStart" in data:
        out["effective_start"] = data["EffectiveStart"]
    if "RuleVersion" in data:
        import aws_sdk_cost_explorer.types.cost_category_rule_version

        out["rule_version"] = (
            aws_sdk_cost_explorer.types.cost_category_rule_version.deserialize_aws_json_1_1(
                data["RuleVersion"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCostCategoryDefinitionRequest.rule_version required"
        )
    if "Rules" in data:
        import aws_sdk_cost_explorer.types.cost_category_rules_list

        out["rules"] = (
            aws_sdk_cost_explorer.types.cost_category_rules_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        raise DeserializationError("CreateCostCategoryDefinitionRequest.rules required")
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "SplitChargeRules" in data:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list

        out["split_charge_rules"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list.deserialize_aws_json_1_1(
                data["SplitChargeRules"]
            )
        )
    if "ResourceTags" in data:
        import aws_sdk_cost_explorer.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_cost_explorer.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    return out
