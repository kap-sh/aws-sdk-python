"""Generated from Smithy shape ``com.amazonaws.mpa#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.filter_field
    import aws_sdk_mpa.types.operator
    import aws_sdk_mpa.types.string


class Filter(TypedDict, closed=True):
    field_name: NotRequired["aws_sdk_mpa.types.filter_field.FilterField"]
    """<p>Name of the filter to use.</p> <note> <p> <b>Supported filters</b> </p> <p>The supported filters for <a>ListSessions</a> are: <code>ActionName</code>, <code>SessionStatus</code>, and <code>InitationTime</code>.</p> </note>"""
    operator: NotRequired["aws_sdk_mpa.types.operator.Operator"]
    """<p>Operator to use for filtering.</p> <ul> <li> <p> <code>EQ</code>: Equal to the specified value</p> </li> <li> <p> <code>NE</code>: Not equal to the specified value</p> </li> <li> <p> <code>GT</code>: Greater than the specified value</p> </li> <li> <p> <code>LT</code>: Less than the specified value</p> </li> <li> <p> <code>GTE</code>: Greater than or equal to the specified value</p> </li> <li> <p> <code>LTE</code>: Less than or equal to the specified value</p> </li> <li> <p> <code>CONTAINS</code>: Contains the specified value</p> </li> <li> <p> <code>NOT_CONTAINS</code>: Does not contain the specified value</p> </li> <li> <p> <code>BETWEEN</code>: Between two values, inclusive of the specified values.</p> </li> </ul> <note> <p> <b>Supported operators for each filter</b>:</p> <ul> <li> <p> <code>ActionName</code>: <code>EQ</code> | <code>NE</code> | <code>CONTAINS</code> | <code>NOT_CONTAINS</code> </p> </li> <li> <p> <code>SessionStatus</code>: <code>EQ</code> | <code>NE</code> </p> </li> <li> <p> <code>InitiationTime</code>: <code>GT</code> | <code>LT</code> | <code>GTE</code> | <code>LTE</code> | <code>BETWEEN</code> </p> </li> </ul> </note>"""
    value: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Value to use for filtering. For the <code>BETWEEN</code> operator, specify values in the format <code>a AND b</code> (<code>AND</code> is case-insensitive).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import aws_sdk_mpa.types.filter_field

        out["FieldName"] = aws_sdk_mpa.types.filter_field.serialize_json(
            value["field_name"]
        )
    if "operator" in value:
        import aws_sdk_mpa.types.operator

        out["Operator"] = aws_sdk_mpa.types.operator.serialize_json(value["operator"])
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import aws_sdk_mpa.types.filter_field

        out["field_name"] = aws_sdk_mpa.types.filter_field.deserialize_json(
            data["FieldName"]
        )
    if "Operator" in data:
        import aws_sdk_mpa.types.operator

        out["operator"] = aws_sdk_mpa.types.operator.deserialize_json(data["Operator"])
    if "Value" in data:
        out["value"] = data["Value"]
    return out
