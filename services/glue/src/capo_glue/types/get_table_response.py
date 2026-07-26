"""Generated from Smithy shape ``com.amazonaws.glue#GetTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.table


class GetTableResponse(TypedDict, closed=True):
    table: NotRequired["capo_glue.types.table.Table"]
    """<p>The <code>Table</code> object that defines the specified table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableResponse) -> dict:
    out: dict = {}
    if "table" in value:
        import capo_glue.types.table

        out["Table"] = capo_glue.types.table.serialize_aws_json_1_1(value["table"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableResponse:
    out: GetTableResponse = {}  # type: ignore[typeddict-item]
    if "Table" in data:
        import capo_glue.types.table

        out["table"] = capo_glue.types.table.deserialize_aws_json_1_1(data["Table"])
    return out
