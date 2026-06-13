"""Generated from Smithy shape ``com.amazonaws.quicksight#DateDimensionField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.date_time_format_configuration
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.hierarchy_id
    import aws_sdk_quicksight.types.time_granularity


class DateDimensionField(TypedDict):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that is used in the <code>DateDimensionField</code>.</p>"""
    date_granularity: NotRequired[
        "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The date granularity of the <code>DateDimensionField</code>. Choose one of the following options:</p> <ul> <li> <p> <code>YEAR</code> </p> </li> <li> <p> <code>QUARTER</code> </p> </li> <li> <p> <code>MONTH</code> </p> </li> <li> <p> <code>WEEK</code> </p> </li> <li> <p> <code>DAY</code> </p> </li> <li> <p> <code>HOUR</code> </p> </li> <li> <p> <code>MINUTE</code> </p> </li> <li> <p> <code>SECOND</code> </p> </li> <li> <p> <code>MILLISECOND</code> </p> </li> </ul>"""
    hierarchy_id: NotRequired["aws_sdk_quicksight.types.hierarchy_id.HierarchyId"]
    """<p>The custom hierarchy ID.</p>"""
    format_configuration: NotRequired[
        "aws_sdk_quicksight.types.date_time_format_configuration.DateTimeFormatConfiguration"
    ]
    """<p>The format configuration of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateDimensionField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "date_granularity" in value:
        import aws_sdk_quicksight.types.time_granularity

        out["DateGranularity"] = (
            aws_sdk_quicksight.types.time_granularity.serialize_json(
                value["date_granularity"]
            )
        )
    if "hierarchy_id" in value:
        out["HierarchyId"] = value["hierarchy_id"]
    if "format_configuration" in value:
        import aws_sdk_quicksight.types.date_time_format_configuration

        out["FormatConfiguration"] = (
            aws_sdk_quicksight.types.date_time_format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateDimensionField:
    out: DateDimensionField = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("DateDimensionField.field_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("DateDimensionField.column required")
    if "DateGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["date_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["DateGranularity"]
            )
        )
    if "HierarchyId" in data:
        out["hierarchy_id"] = data["HierarchyId"]
    if "FormatConfiguration" in data:
        import aws_sdk_quicksight.types.date_time_format_configuration

        out["format_configuration"] = (
            aws_sdk_quicksight.types.date_time_format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out
