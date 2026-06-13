"""Generated from Smithy shape ``com.amazonaws.quicksight#NestedFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.inner_filter
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class NestedFilter(TypedDict):
    filter_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    include_inner_set: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A boolean condition to include or exclude the subset that is defined by the values of the nested inner filter.</p>"""
    inner_filter: "aws_sdk_quicksight.types.inner_filter.InnerFilter"
    """<p>The <code>InnerFilter</code> defines the subset of data to be used with the <code>NestedFilter</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NestedFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    out["IncludeInnerSet"] = value.get("include_inner_set", False)
    import aws_sdk_quicksight.types.inner_filter

    out["InnerFilter"] = aws_sdk_quicksight.types.inner_filter.serialize_json(
        value["inner_filter"]
    )
    return out


def deserialize_json(data: dict) -> NestedFilter:
    out: NestedFilter = {}  # type: ignore[typeddict-item]
    if "FilterId" in data:
        out["filter_id"] = data["FilterId"]
    else:
        raise DeserializationError("NestedFilter.filter_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("NestedFilter.column required")
    if "IncludeInnerSet" in data:
        out["include_inner_set"] = data["IncludeInnerSet"]
    else:
        out["include_inner_set"] = False
    if "InnerFilter" in data:
        import aws_sdk_quicksight.types.inner_filter

        out["inner_filter"] = aws_sdk_quicksight.types.inner_filter.deserialize_json(
            data["InnerFilter"]
        )
    else:
        raise DeserializationError("NestedFilter.inner_filter required")
    return out
