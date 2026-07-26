"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesCompositeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.allowed_operators
    import capo_securityhub.types.resources_composite_filter_list
    import capo_securityhub.types.resources_date_filter_list
    import capo_securityhub.types.resources_map_filter_list
    import capo_securityhub.types.resources_number_filter_list
    import capo_securityhub.types.resources_string_filter_list


class ResourcesCompositeFilter(TypedDict, closed=True):
    string_filters: NotRequired[
        "capo_securityhub.types.resources_string_filter_list.ResourcesStringFilterList"
    ]
    """<p>Enables filtering based on string field values.</p>"""
    date_filters: NotRequired[
        "capo_securityhub.types.resources_date_filter_list.ResourcesDateFilterList"
    ]
    """<p>Enables filtering based on date and timestamp field values.</p>"""
    number_filters: NotRequired[
        "capo_securityhub.types.resources_number_filter_list.ResourcesNumberFilterList"
    ]
    """<p>Enables filtering based on numerical field values.</p>"""
    map_filters: NotRequired[
        "capo_securityhub.types.resources_map_filter_list.ResourcesMapFilterList"
    ]
    """<p>Enables filtering based on map-based field values.</p>"""
    nested_composite_filters: NotRequired[
        "capo_securityhub.types.resources_composite_filter_list.ResourcesCompositeFilterList"
    ]
    """<p> Provides an additional level of filtering, creating a three-layer nested structure. The first layer is a <code>CompositeFilters</code> array with a <code>CompositeOperator</code> (<code>AND</code>/<code>OR</code>). The second layer is a <code>CompositeFilter</code> object that contains direct filters and <code>NestedCompositeFilters</code>. The third layer is <code>NestedCompositeFilters</code>, which contains additional filter conditions. </p>"""
    operator: NotRequired["capo_securityhub.types.allowed_operators.AllowedOperators"]
    """<p>The logical operator used to combine multiple filter conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesCompositeFilter) -> dict:
    out: dict = {}
    if "string_filters" in value:
        import capo_securityhub.types.resources_string_filter_list

        out["StringFilters"] = (
            capo_securityhub.types.resources_string_filter_list.serialize_json(
                value["string_filters"]
            )
        )
    if "date_filters" in value:
        import capo_securityhub.types.resources_date_filter_list

        out["DateFilters"] = (
            capo_securityhub.types.resources_date_filter_list.serialize_json(
                value["date_filters"]
            )
        )
    if "number_filters" in value:
        import capo_securityhub.types.resources_number_filter_list

        out["NumberFilters"] = (
            capo_securityhub.types.resources_number_filter_list.serialize_json(
                value["number_filters"]
            )
        )
    if "map_filters" in value:
        import capo_securityhub.types.resources_map_filter_list

        out["MapFilters"] = (
            capo_securityhub.types.resources_map_filter_list.serialize_json(
                value["map_filters"]
            )
        )
    if "nested_composite_filters" in value:
        import capo_securityhub.types.resources_composite_filter_list

        out["NestedCompositeFilters"] = (
            capo_securityhub.types.resources_composite_filter_list.serialize_json(
                value["nested_composite_filters"]
            )
        )
    if "operator" in value:
        import capo_securityhub.types.allowed_operators

        out["Operator"] = capo_securityhub.types.allowed_operators.serialize_json(
            value["operator"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesCompositeFilter:
    out: ResourcesCompositeFilter = {}  # type: ignore[typeddict-item]
    if "StringFilters" in data:
        import capo_securityhub.types.resources_string_filter_list

        out["string_filters"] = (
            capo_securityhub.types.resources_string_filter_list.deserialize_json(
                data["StringFilters"]
            )
        )
    if "DateFilters" in data:
        import capo_securityhub.types.resources_date_filter_list

        out["date_filters"] = (
            capo_securityhub.types.resources_date_filter_list.deserialize_json(
                data["DateFilters"]
            )
        )
    if "NumberFilters" in data:
        import capo_securityhub.types.resources_number_filter_list

        out["number_filters"] = (
            capo_securityhub.types.resources_number_filter_list.deserialize_json(
                data["NumberFilters"]
            )
        )
    if "MapFilters" in data:
        import capo_securityhub.types.resources_map_filter_list

        out["map_filters"] = (
            capo_securityhub.types.resources_map_filter_list.deserialize_json(
                data["MapFilters"]
            )
        )
    if "NestedCompositeFilters" in data:
        import capo_securityhub.types.resources_composite_filter_list

        out["nested_composite_filters"] = (
            capo_securityhub.types.resources_composite_filter_list.deserialize_json(
                data["NestedCompositeFilters"]
            )
        )
    if "Operator" in data:
        import capo_securityhub.types.allowed_operators

        out["operator"] = capo_securityhub.types.allowed_operators.deserialize_json(
            data["Operator"]
        )
    return out
