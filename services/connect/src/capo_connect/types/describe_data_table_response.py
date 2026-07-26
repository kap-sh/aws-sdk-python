"""Generated from Smithy shape ``com.amazonaws.connect#DescribeDataTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.data_table


class DescribeDataTableResponse(TypedDict, closed=True):
    data_table: "capo_connect.types.data_table.DataTable"
    """<p>The complete data table information including metadata, configuration, and versioning details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataTableResponse) -> dict:
    out: dict = {}
    import capo_connect.types.data_table

    out["DataTable"] = capo_connect.types.data_table.serialize_json(value["data_table"])
    return out


def deserialize_json(data: dict) -> DescribeDataTableResponse:
    out: DescribeDataTableResponse = {}  # type: ignore[typeddict-item]
    if "DataTable" in data:
        import capo_connect.types.data_table

        out["data_table"] = capo_connect.types.data_table.deserialize_json(
            data["DataTable"]
        )
    else:
        raise DeserializationError("DescribeDataTableResponse.data_table required")
    return out
