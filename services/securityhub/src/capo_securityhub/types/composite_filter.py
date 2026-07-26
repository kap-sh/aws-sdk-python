"""Generated from Smithy shape ``com.amazonaws.securityhub#CompositeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.allowed_operators
    import capo_securityhub.types.composite_filter_list
    import capo_securityhub.types.ocsf_boolean_filter_list
    import capo_securityhub.types.ocsf_date_filter_list
    import capo_securityhub.types.ocsf_ip_filter_list
    import capo_securityhub.types.ocsf_map_filter_list
    import capo_securityhub.types.ocsf_number_filter_list
    import capo_securityhub.types.ocsf_string_filter_list


class CompositeFilter(TypedDict, closed=True):
    string_filters: NotRequired[
        "capo_securityhub.types.ocsf_string_filter_list.OcsfStringFilterList"
    ]
    """<p>Enables filtering based on string field values.</p>"""
    date_filters: NotRequired[
        "capo_securityhub.types.ocsf_date_filter_list.OcsfDateFilterList"
    ]
    """<p>Enables filtering based on date and timestamp fields.</p>"""
    boolean_filters: NotRequired[
        "capo_securityhub.types.ocsf_boolean_filter_list.OcsfBooleanFilterList"
    ]
    """<p>Enables filtering based on boolean field values.</p>"""
    number_filters: NotRequired[
        "capo_securityhub.types.ocsf_number_filter_list.OcsfNumberFilterList"
    ]
    """<p>Enables filtering based on numerical field values.</p>"""
    map_filters: NotRequired[
        "capo_securityhub.types.ocsf_map_filter_list.OcsfMapFilterList"
    ]
    """<p>Enables filtering based on map field values.</p>"""
    ip_filters: NotRequired[
        "capo_securityhub.types.ocsf_ip_filter_list.OcsfIpFilterList"
    ]
    """<p>A list of IP address filters that allowing you to filter findings based on IP address properties.</p>"""
    nested_composite_filters: NotRequired[
        "capo_securityhub.types.composite_filter_list.CompositeFilterList"
    ]
    """<p> Provides an additional level of filtering, creating a three-layer nested structure. The first layer is a <code>CompositeFilters</code> array with a <code>CompositeOperator</code> (<code>AND</code>/<code>OR</code>). The second layer is a <code>CompositeFilter</code> object that contains direct filters and <code>NestedCompositeFilters</code>. The third layer is <code>NestedCompositeFilters</code>, which contains additional filter conditions. </p>"""
    operator: NotRequired["capo_securityhub.types.allowed_operators.AllowedOperators"]
    """<p>The logical operator used to combine multiple filter conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositeFilter) -> dict:
    out: dict = {}
    if "string_filters" in value:
        import capo_securityhub.types.ocsf_string_filter_list

        out["StringFilters"] = (
            capo_securityhub.types.ocsf_string_filter_list.serialize_json(
                value["string_filters"]
            )
        )
    if "date_filters" in value:
        import capo_securityhub.types.ocsf_date_filter_list

        out["DateFilters"] = (
            capo_securityhub.types.ocsf_date_filter_list.serialize_json(
                value["date_filters"]
            )
        )
    if "boolean_filters" in value:
        import capo_securityhub.types.ocsf_boolean_filter_list

        out["BooleanFilters"] = (
            capo_securityhub.types.ocsf_boolean_filter_list.serialize_json(
                value["boolean_filters"]
            )
        )
    if "number_filters" in value:
        import capo_securityhub.types.ocsf_number_filter_list

        out["NumberFilters"] = (
            capo_securityhub.types.ocsf_number_filter_list.serialize_json(
                value["number_filters"]
            )
        )
    if "map_filters" in value:
        import capo_securityhub.types.ocsf_map_filter_list

        out["MapFilters"] = capo_securityhub.types.ocsf_map_filter_list.serialize_json(
            value["map_filters"]
        )
    if "ip_filters" in value:
        import capo_securityhub.types.ocsf_ip_filter_list

        out["IpFilters"] = capo_securityhub.types.ocsf_ip_filter_list.serialize_json(
            value["ip_filters"]
        )
    if "nested_composite_filters" in value:
        import capo_securityhub.types.composite_filter_list

        out["NestedCompositeFilters"] = (
            capo_securityhub.types.composite_filter_list.serialize_json(
                value["nested_composite_filters"]
            )
        )
    if "operator" in value:
        import capo_securityhub.types.allowed_operators

        out["Operator"] = capo_securityhub.types.allowed_operators.serialize_json(
            value["operator"]
        )
    return out


def deserialize_json(data: dict) -> CompositeFilter:
    out: CompositeFilter = {}  # type: ignore[typeddict-item]
    if "StringFilters" in data:
        import capo_securityhub.types.ocsf_string_filter_list

        out["string_filters"] = (
            capo_securityhub.types.ocsf_string_filter_list.deserialize_json(
                data["StringFilters"]
            )
        )
    if "DateFilters" in data:
        import capo_securityhub.types.ocsf_date_filter_list

        out["date_filters"] = (
            capo_securityhub.types.ocsf_date_filter_list.deserialize_json(
                data["DateFilters"]
            )
        )
    if "BooleanFilters" in data:
        import capo_securityhub.types.ocsf_boolean_filter_list

        out["boolean_filters"] = (
            capo_securityhub.types.ocsf_boolean_filter_list.deserialize_json(
                data["BooleanFilters"]
            )
        )
    if "NumberFilters" in data:
        import capo_securityhub.types.ocsf_number_filter_list

        out["number_filters"] = (
            capo_securityhub.types.ocsf_number_filter_list.deserialize_json(
                data["NumberFilters"]
            )
        )
    if "MapFilters" in data:
        import capo_securityhub.types.ocsf_map_filter_list

        out["map_filters"] = (
            capo_securityhub.types.ocsf_map_filter_list.deserialize_json(
                data["MapFilters"]
            )
        )
    if "IpFilters" in data:
        import capo_securityhub.types.ocsf_ip_filter_list

        out["ip_filters"] = capo_securityhub.types.ocsf_ip_filter_list.deserialize_json(
            data["IpFilters"]
        )
    if "NestedCompositeFilters" in data:
        import capo_securityhub.types.composite_filter_list

        out["nested_composite_filters"] = (
            capo_securityhub.types.composite_filter_list.deserialize_json(
                data["NestedCompositeFilters"]
            )
        )
    if "Operator" in data:
        import capo_securityhub.types.allowed_operators

        out["operator"] = capo_securityhub.types.allowed_operators.deserialize_json(
            data["Operator"]
        )
    return out
