"""Generated from Smithy shape ``com.amazonaws.sagemaker#TimeSeriesConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.grouping_attribute_names
    import capo_sagemaker.types.item_identifier_attribute_name
    import capo_sagemaker.types.target_attribute_name
    import capo_sagemaker.types.timestamp_attribute_name


class TimeSeriesConfig(TypedDict, closed=True):
    target_attribute_name: NotRequired[
        "capo_sagemaker.types.target_attribute_name.TargetAttributeName"
    ]
    """<p>The name of the column representing the target variable that you want to predict for each item in your dataset. The data type of the target variable must be numerical.</p>"""
    timestamp_attribute_name: NotRequired[
        "capo_sagemaker.types.timestamp_attribute_name.TimestampAttributeName"
    ]
    """<p>The name of the column indicating a point in time at which the target value of a given item is recorded.</p>"""
    item_identifier_attribute_name: NotRequired[
        "capo_sagemaker.types.item_identifier_attribute_name.ItemIdentifierAttributeName"
    ]
    """<p>The name of the column that represents the set of item identifiers for which you want to predict the target value.</p>"""
    grouping_attribute_names: NotRequired[
        "capo_sagemaker.types.grouping_attribute_names.GroupingAttributeNames"
    ]
    """<p>A set of columns names that can be grouped with the item identifier column to create a composite key for which a target value is predicted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesConfig) -> dict:
    out: dict = {}
    if "target_attribute_name" in value:
        out["TargetAttributeName"] = value["target_attribute_name"]
    if "timestamp_attribute_name" in value:
        out["TimestampAttributeName"] = value["timestamp_attribute_name"]
    if "item_identifier_attribute_name" in value:
        out["ItemIdentifierAttributeName"] = value["item_identifier_attribute_name"]
    if "grouping_attribute_names" in value:
        import capo_sagemaker.types.grouping_attribute_names

        out["GroupingAttributeNames"] = (
            capo_sagemaker.types.grouping_attribute_names.serialize_aws_json_1_1(
                value["grouping_attribute_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeSeriesConfig:
    out: TimeSeriesConfig = {}  # type: ignore[typeddict-item]
    if "TargetAttributeName" in data:
        out["target_attribute_name"] = data["TargetAttributeName"]
    if "TimestampAttributeName" in data:
        out["timestamp_attribute_name"] = data["TimestampAttributeName"]
    if "ItemIdentifierAttributeName" in data:
        out["item_identifier_attribute_name"] = data["ItemIdentifierAttributeName"]
    if "GroupingAttributeNames" in data:
        import capo_sagemaker.types.grouping_attribute_names

        out["grouping_attribute_names"] = (
            capo_sagemaker.types.grouping_attribute_names.deserialize_aws_json_1_1(
                data["GroupingAttributeNames"]
            )
        )
    return out
