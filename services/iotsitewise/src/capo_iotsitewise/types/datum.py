"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Datum``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.datum_list
    import capo_iotsitewise.types.nullable_boolean
    import capo_iotsitewise.types.row
    import capo_iotsitewise.types.scalar_value


class Datum(TypedDict, closed=True):
    scalar_value: NotRequired["capo_iotsitewise.types.scalar_value.ScalarValue"]
    """<p>Indicates if the data point is a scalar value such as integer, string, double, or Boolean. </p>"""
    array_value: NotRequired["capo_iotsitewise.types.datum_list.DatumList"]
    """<p>Indicates if the data point is an array. </p>"""
    row_value: NotRequired["capo_iotsitewise.types.row.Row"]
    """<p>Indicates if the data point is a row.</p>"""
    null_value: NotRequired["capo_iotsitewise.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates if the data point is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Datum) -> dict:
    out: dict = {}
    if "scalar_value" in value:
        out["scalarValue"] = value["scalar_value"]
    if "array_value" in value:
        import capo_iotsitewise.types.datum_list

        out["arrayValue"] = capo_iotsitewise.types.datum_list.serialize_json(
            value["array_value"]
        )
    if "row_value" in value:
        import capo_iotsitewise.types.row

        out["rowValue"] = capo_iotsitewise.types.row.serialize_json(value["row_value"])
    if "null_value" in value:
        out["nullValue"] = value["null_value"]
    return out


def deserialize_json(data: dict) -> Datum:
    out: Datum = {}  # type: ignore[typeddict-item]
    if "scalarValue" in data:
        out["scalar_value"] = data["scalarValue"]
    if "arrayValue" in data:
        import capo_iotsitewise.types.datum_list

        out["array_value"] = capo_iotsitewise.types.datum_list.deserialize_json(
            data["arrayValue"]
        )
    if "rowValue" in data:
        import capo_iotsitewise.types.row

        out["row_value"] = capo_iotsitewise.types.row.deserialize_json(data["rowValue"])
    if "nullValue" in data:
        out["null_value"] = data["nullValue"]
    return out
