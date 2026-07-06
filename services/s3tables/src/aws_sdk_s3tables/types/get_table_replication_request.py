"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_arn


class GetTableReplicationRequest(TypedDict, closed=True):
    table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableReplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableReplicationRequest:
    out: GetTableReplicationRequest = {}  # type: ignore[typeddict-item]
    return out
