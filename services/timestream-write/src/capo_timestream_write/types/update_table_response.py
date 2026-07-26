"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#UpdateTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.table


class UpdateTableResponse(TypedDict, closed=True):
    table: NotRequired["capo_timestream_write.types.table.Table"]
    """<p>The updated Timestream table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTableResponse) -> dict:
    out: dict = {}
    if "table" in value:
        import capo_timestream_write.types.table

        out["Table"] = capo_timestream_write.types.table.serialize_aws_json_1_0(
            value["table"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTableResponse:
    out: UpdateTableResponse = {}  # type: ignore[typeddict-item]
    if "Table" in data:
        import capo_timestream_write.types.table

        out["table"] = capo_timestream_write.types.table.deserialize_aws_json_1_0(
            data["Table"]
        )
    return out
