"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.arn
    import aws_sdk_cost_explorer.types.cost_category_name
    import aws_sdk_cost_explorer.types.cost_category_processing_status_list
    import aws_sdk_cost_explorer.types.cost_category_value
    import aws_sdk_cost_explorer.types.cost_category_values_list
    import aws_sdk_cost_explorer.types.non_negative_integer
    import aws_sdk_cost_explorer.types.resource_types
    import aws_sdk_cost_explorer.types.zoned_date_time


class CostCategoryReference(TypedDict, closed=True):
    cost_category_arn: NotRequired["aws_sdk_cost_explorer.types.arn.Arn"]
    """<p>The unique identifier for your cost category. </p>"""
    name: NotRequired["aws_sdk_cost_explorer.types.cost_category_name.CostCategoryName"]
    effective_start: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The cost category's effective start date.</p>"""
    effective_end: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The cost category's effective end date.</p>"""
    number_of_rules: (
        "aws_sdk_cost_explorer.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The number of rules that are associated with a specific cost category. </p>"""
    processing_status: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_processing_status_list.CostCategoryProcessingStatusList"
    ]
    """<p>The list of processing statuses for Cost Management products for a specific cost category. </p>"""
    values: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_values_list.CostCategoryValuesList"
    ]
    """<p>A list of unique cost category values in a specific cost category. </p>"""
    default_value: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_value.CostCategoryValue"
    ]
    supported_resource_types: NotRequired[
        "aws_sdk_cost_explorer.types.resource_types.ResourceTypes"
    ]
    """<p> The resource types supported by a specific cost category. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryReference) -> dict:
    out: dict = {}
    if "cost_category_arn" in value:
        out["CostCategoryArn"] = value["cost_category_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "effective_start" in value:
        out["EffectiveStart"] = value["effective_start"]
    if "effective_end" in value:
        out["EffectiveEnd"] = value["effective_end"]
    out["NumberOfRules"] = value.get("number_of_rules", 0)
    if "processing_status" in value:
        import aws_sdk_cost_explorer.types.cost_category_processing_status_list

        out["ProcessingStatus"] = (
            aws_sdk_cost_explorer.types.cost_category_processing_status_list.serialize_aws_json_1_1(
                value["processing_status"]
            )
        )
    if "values" in value:
        import aws_sdk_cost_explorer.types.cost_category_values_list

        out["Values"] = (
            aws_sdk_cost_explorer.types.cost_category_values_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "supported_resource_types" in value:
        import aws_sdk_cost_explorer.types.resource_types

        out["SupportedResourceTypes"] = (
            aws_sdk_cost_explorer.types.resource_types.serialize_aws_json_1_1(
                value["supported_resource_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategoryReference:
    out: CostCategoryReference = {}  # type: ignore[typeddict-item]
    if "CostCategoryArn" in data:
        out["cost_category_arn"] = data["CostCategoryArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "EffectiveStart" in data:
        out["effective_start"] = data["EffectiveStart"]
    if "EffectiveEnd" in data:
        out["effective_end"] = data["EffectiveEnd"]
    if "NumberOfRules" in data:
        out["number_of_rules"] = data["NumberOfRules"]
    else:
        out["number_of_rules"] = 0
    if "ProcessingStatus" in data:
        import aws_sdk_cost_explorer.types.cost_category_processing_status_list

        out["processing_status"] = (
            aws_sdk_cost_explorer.types.cost_category_processing_status_list.deserialize_aws_json_1_1(
                data["ProcessingStatus"]
            )
        )
    if "Values" in data:
        import aws_sdk_cost_explorer.types.cost_category_values_list

        out["values"] = (
            aws_sdk_cost_explorer.types.cost_category_values_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "SupportedResourceTypes" in data:
        import aws_sdk_cost_explorer.types.resource_types

        out["supported_resource_types"] = (
            aws_sdk_cost_explorer.types.resource_types.deserialize_aws_json_1_1(
                data["SupportedResourceTypes"]
            )
        )
    return out
