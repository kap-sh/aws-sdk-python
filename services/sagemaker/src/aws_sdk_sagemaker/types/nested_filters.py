"""Generated from Smithy shape ``com.amazonaws.sagemaker#NestedFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.filter_list
    import aws_sdk_sagemaker.types.resource_property_name


class NestedFilters(TypedDict, closed=True):
    nested_property_name: NotRequired[
        "aws_sdk_sagemaker.types.resource_property_name.ResourcePropertyName"
    ]
    """<p>The name of the property to use in the nested filters. The value must match a listed property name, such as <code>InputDataConfig</code>.</p>"""
    filters: NotRequired["aws_sdk_sagemaker.types.filter_list.FilterList"]
    """<p>A list of filters. Each filter acts on a property. Filters must contain at least one <code>Filters</code> value. For example, a <code>NestedFilters</code> call might include a filter on the <code>PropertyName</code> parameter of the <code>InputDataConfig</code> property: <code>InputDataConfig.DataSource.S3DataSource.S3Uri</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NestedFilters) -> dict:
    out: dict = {}
    if "nested_property_name" in value:
        out["NestedPropertyName"] = value["nested_property_name"]
    if "filters" in value:
        import aws_sdk_sagemaker.types.filter_list

        out["Filters"] = aws_sdk_sagemaker.types.filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NestedFilters:
    out: NestedFilters = {}  # type: ignore[typeddict-item]
    if "NestedPropertyName" in data:
        out["nested_property_name"] = data["NestedPropertyName"]
    if "Filters" in data:
        import aws_sdk_sagemaker.types.filter_list

        out["filters"] = aws_sdk_sagemaker.types.filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    return out
