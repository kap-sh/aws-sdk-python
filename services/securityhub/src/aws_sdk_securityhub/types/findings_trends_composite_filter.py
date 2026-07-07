"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsTrendsCompositeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.allowed_operators
    import aws_sdk_securityhub.types.findings_trends_composite_filter_list
    import aws_sdk_securityhub.types.findings_trends_string_filter_list


class FindingsTrendsCompositeFilter(TypedDict, closed=True):
    string_filters: NotRequired[
        "aws_sdk_securityhub.types.findings_trends_string_filter_list.FindingsTrendsStringFilterList"
    ]
    """<p>A list of string filters that apply to findings trend data fields.</p>"""
    nested_composite_filters: NotRequired[
        "aws_sdk_securityhub.types.findings_trends_composite_filter_list.FindingsTrendsCompositeFilterList"
    ]
    """<p>A list of nested composite filters that you can use to create complex filter conditions for findings trend data.</p>"""
    operator: NotRequired[
        "aws_sdk_securityhub.types.allowed_operators.AllowedOperators"
    ]
    """<p>The logical operator (AND, OR) to apply between the string filters and nested composite filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingsTrendsCompositeFilter) -> dict:
    out: dict = {}
    if "string_filters" in value:
        import aws_sdk_securityhub.types.findings_trends_string_filter_list

        out["StringFilters"] = (
            aws_sdk_securityhub.types.findings_trends_string_filter_list.serialize_json(
                value["string_filters"]
            )
        )
    if "nested_composite_filters" in value:
        import aws_sdk_securityhub.types.findings_trends_composite_filter_list

        out["NestedCompositeFilters"] = (
            aws_sdk_securityhub.types.findings_trends_composite_filter_list.serialize_json(
                value["nested_composite_filters"]
            )
        )
    if "operator" in value:
        import aws_sdk_securityhub.types.allowed_operators

        out["Operator"] = aws_sdk_securityhub.types.allowed_operators.serialize_json(
            value["operator"]
        )
    return out


def deserialize_json(data: dict) -> FindingsTrendsCompositeFilter:
    out: FindingsTrendsCompositeFilter = {}  # type: ignore[typeddict-item]
    if "StringFilters" in data:
        import aws_sdk_securityhub.types.findings_trends_string_filter_list

        out["string_filters"] = (
            aws_sdk_securityhub.types.findings_trends_string_filter_list.deserialize_json(
                data["StringFilters"]
            )
        )
    if "NestedCompositeFilters" in data:
        import aws_sdk_securityhub.types.findings_trends_composite_filter_list

        out["nested_composite_filters"] = (
            aws_sdk_securityhub.types.findings_trends_composite_filter_list.deserialize_json(
                data["NestedCompositeFilters"]
            )
        )
    if "Operator" in data:
        import aws_sdk_securityhub.types.allowed_operators

        out["operator"] = aws_sdk_securityhub.types.allowed_operators.deserialize_json(
            data["Operator"]
        )
    return out
