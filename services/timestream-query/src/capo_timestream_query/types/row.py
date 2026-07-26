"""Generated from Smithy shape ``com.amazonaws.timestreamquery#Row``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_query.types.datum_list


class Row(TypedDict, closed=True):
    data: "capo_timestream_query.types.datum_list.DatumList"
    """<p>List of data points in a single row of the result set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Row) -> dict:
    out: dict = {}
    import capo_timestream_query.types.datum_list

    out["Data"] = capo_timestream_query.types.datum_list.serialize_aws_json_1_0(
        value["data"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Row:
    out: Row = {}  # type: ignore[typeddict-item]
    if "Data" in data:
        import capo_timestream_query.types.datum_list

        out["data"] = capo_timestream_query.types.datum_list.deserialize_aws_json_1_0(
            data["Data"]
        )
    else:
        raise DeserializationError("Row.data required")
    return out
