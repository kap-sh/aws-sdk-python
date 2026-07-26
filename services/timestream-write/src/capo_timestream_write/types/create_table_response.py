"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#CreateTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.table


class CreateTableResponse(TypedDict, closed=True):
    table: NotRequired["capo_timestream_write.types.table.Table"]
    """<p>The newly created Timestream table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTableResponse) -> dict:
    out: dict = {}
    if "table" in value:
        import capo_timestream_write.types.table

        out["Table"] = capo_timestream_write.types.table.serialize_aws_json_1_0(
            value["table"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTableResponse:
    out: CreateTableResponse = {}  # type: ignore[typeddict-item]
    if "Table" in data:
        import capo_timestream_write.types.table

        out["table"] = capo_timestream_write.types.table.deserialize_aws_json_1_0(
            data["Table"]
        )
    return out
