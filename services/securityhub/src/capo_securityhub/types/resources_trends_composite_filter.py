"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsCompositeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.allowed_operators
    import capo_securityhub.types.resources_trends_composite_filter_list
    import capo_securityhub.types.resources_trends_string_filter_list


class ResourcesTrendsCompositeFilter(TypedDict, closed=True):
    string_filters: NotRequired[
        "capo_securityhub.types.resources_trends_string_filter_list.ResourcesTrendsStringFilterList"
    ]
    """<p>A list of string filters that apply to resources trend data fields.</p>"""
    nested_composite_filters: NotRequired[
        "capo_securityhub.types.resources_trends_composite_filter_list.ResourcesTrendsCompositeFilterList"
    ]
    """<p>A list of nested composite filters that you can use to create complex filter conditions for resources trend data.</p>"""
    operator: NotRequired["capo_securityhub.types.allowed_operators.AllowedOperators"]
    """<p>The logical operator (AND, OR) to apply between the string filters and nested composite filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsCompositeFilter) -> dict:
    out: dict = {}
    if "string_filters" in value:
        import capo_securityhub.types.resources_trends_string_filter_list

        out["StringFilters"] = (
            capo_securityhub.types.resources_trends_string_filter_list.serialize_json(
                value["string_filters"]
            )
        )
    if "nested_composite_filters" in value:
        import capo_securityhub.types.resources_trends_composite_filter_list

        out["NestedCompositeFilters"] = (
            capo_securityhub.types.resources_trends_composite_filter_list.serialize_json(
                value["nested_composite_filters"]
            )
        )
    if "operator" in value:
        import capo_securityhub.types.allowed_operators

        out["Operator"] = capo_securityhub.types.allowed_operators.serialize_json(
            value["operator"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesTrendsCompositeFilter:
    out: ResourcesTrendsCompositeFilter = {}  # type: ignore[typeddict-item]
    if "StringFilters" in data:
        import capo_securityhub.types.resources_trends_string_filter_list

        out["string_filters"] = (
            capo_securityhub.types.resources_trends_string_filter_list.deserialize_json(
                data["StringFilters"]
            )
        )
    if "NestedCompositeFilters" in data:
        import capo_securityhub.types.resources_trends_composite_filter_list

        out["nested_composite_filters"] = (
            capo_securityhub.types.resources_trends_composite_filter_list.deserialize_json(
                data["NestedCompositeFilters"]
            )
        )
    if "Operator" in data:
        import capo_securityhub.types.allowed_operators

        out["operator"] = capo_securityhub.types.allowed_operators.deserialize_json(
            data["Operator"]
        )
    return out
