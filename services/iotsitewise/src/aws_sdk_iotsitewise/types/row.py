"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Row``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.datum_list


class Row(TypedDict, closed=True):
    data: "aws_sdk_iotsitewise.types.datum_list.DatumList"
    """<p>List of data points in a single row of the result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Row) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.datum_list

    out["data"] = aws_sdk_iotsitewise.types.datum_list.serialize_json(value["data"])
    return out


def deserialize_json(data: dict) -> Row:
    out: Row = {}  # type: ignore[typeddict-item]
    if "data" in data:
        import aws_sdk_iotsitewise.types.datum_list

        out["data"] = aws_sdk_iotsitewise.types.datum_list.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("Row.data required")
    return out
