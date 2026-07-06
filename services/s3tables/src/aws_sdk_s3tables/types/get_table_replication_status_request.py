"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableReplicationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_arn


class GetTableReplicationStatusRequest(TypedDict, closed=True):
    table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableReplicationStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableReplicationStatusRequest:
    out: GetTableReplicationStatusRequest = {}  # type: ignore[typeddict-item]
    return out
