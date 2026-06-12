"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesCompositeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.allowed_operators
    import aws_sdk_securityhub.types.resources_composite_filter_list
    import aws_sdk_securityhub.types.resources_date_filter_list
    import aws_sdk_securityhub.types.resources_map_filter_list
    import aws_sdk_securityhub.types.resources_number_filter_list
    import aws_sdk_securityhub.types.resources_string_filter_list


class ResourcesCompositeFilter(TypedDict):
    string_filters: NotRequired[
        "aws_sdk_securityhub.types.resources_string_filter_list.ResourcesStringFilterList"
    ]
    """<p>Enables filtering based on string field values.</p>"""
    date_filters: NotRequired[
        "aws_sdk_securityhub.types.resources_date_filter_list.ResourcesDateFilterList"
    ]
    """<p>Enables filtering based on date and timestamp field values.</p>"""
    number_filters: NotRequired[
        "aws_sdk_securityhub.types.resources_number_filter_list.ResourcesNumberFilterList"
    ]
    """<p>Enables filtering based on numerical field values.</p>"""
    map_filters: NotRequired[
        "aws_sdk_securityhub.types.resources_map_filter_list.ResourcesMapFilterList"
    ]
    """<p>Enables filtering based on map-based field values.</p>"""
    nested_composite_filters: NotRequired[
        "aws_sdk_securityhub.types.resources_composite_filter_list.ResourcesCompositeFilterList"
    ]
    """<p> Provides an additional level of filtering, creating a three-layer nested structure. The first layer is a <code>CompositeFilters</code> array with a <code>CompositeOperator</code> (<code>AND</code>/<code>OR</code>). The second layer is a <code>CompositeFilter</code> object that contains direct filters and <code>NestedCompositeFilters</code>. The third layer is <code>NestedCompositeFilters</code>, which contains additional filter conditions. </p>"""
    operator: NotRequired[
        "aws_sdk_securityhub.types.allowed_operators.AllowedOperators"
    ]
    """<p>The logical operator used to combine multiple filter conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesCompositeFilter) -> dict:
    out: dict = {}
    if "string_filters" in value:
        import aws_sdk_securityhub.types.resources_string_filter_list

        out["StringFilters"] = (
            aws_sdk_securityhub.types.resources_string_filter_list.serialize_json(
                value["string_filters"]
            )
        )
    if "date_filters" in value:
        import aws_sdk_securityhub.types.resources_date_filter_list

        out["DateFilters"] = (
            aws_sdk_securityhub.types.resources_date_filter_list.serialize_json(
                value["date_filters"]
            )
        )
    if "number_filters" in value:
        import aws_sdk_securityhub.types.resources_number_filter_list

        out["NumberFilters"] = (
            aws_sdk_securityhub.types.resources_number_filter_list.serialize_json(
                value["number_filters"]
            )
        )
    if "map_filters" in value:
        import aws_sdk_securityhub.types.resources_map_filter_list

        out["MapFilters"] = (
            aws_sdk_securityhub.types.resources_map_filter_list.serialize_json(
                value["map_filters"]
            )
        )
    if "nested_composite_filters" in value:
        import aws_sdk_securityhub.types.resources_composite_filter_list

        out["NestedCompositeFilters"] = (
            aws_sdk_securityhub.types.resources_composite_filter_list.serialize_json(
                value["nested_composite_filters"]
            )
        )
    if "operator" in value:
        import aws_sdk_securityhub.types.allowed_operators

        out["Operator"] = aws_sdk_securityhub.types.allowed_operators.serialize_json(
            value["operator"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesCompositeFilter:
    out: ResourcesCompositeFilter = {}  # type: ignore[typeddict-item]
    if "StringFilters" in data:
        import aws_sdk_securityhub.types.resources_string_filter_list

        out["string_filters"] = (
            aws_sdk_securityhub.types.resources_string_filter_list.deserialize_json(
                data["StringFilters"]
            )
        )
    if "DateFilters" in data:
        import aws_sdk_securityhub.types.resources_date_filter_list

        out["date_filters"] = (
            aws_sdk_securityhub.types.resources_date_filter_list.deserialize_json(
                data["DateFilters"]
            )
        )
    if "NumberFilters" in data:
        import aws_sdk_securityhub.types.resources_number_filter_list

        out["number_filters"] = (
            aws_sdk_securityhub.types.resources_number_filter_list.deserialize_json(
                data["NumberFilters"]
            )
        )
    if "MapFilters" in data:
        import aws_sdk_securityhub.types.resources_map_filter_list

        out["map_filters"] = (
            aws_sdk_securityhub.types.resources_map_filter_list.deserialize_json(
                data["MapFilters"]
            )
        )
    if "NestedCompositeFilters" in data:
        import aws_sdk_securityhub.types.resources_composite_filter_list

        out["nested_composite_filters"] = (
            aws_sdk_securityhub.types.resources_composite_filter_list.deserialize_json(
                data["NestedCompositeFilters"]
            )
        )
    if "Operator" in data:
        import aws_sdk_securityhub.types.allowed_operators

        out["operator"] = aws_sdk_securityhub.types.allowed_operators.deserialize_json(
            data["Operator"]
        )
    return out
