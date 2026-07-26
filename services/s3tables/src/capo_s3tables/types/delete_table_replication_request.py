"""Generated from Smithy shape ``com.amazonaws.s3tables#DeleteTableReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_arn


class DeleteTableReplicationRequest(TypedDict, closed=True):
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    version_token: "str"
    """<p>A version token from a previous GetTableReplication call. Use this token to ensure you're deleting the expected version of the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTableReplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTableReplicationRequest:
    out: DeleteTableReplicationRequest = {}  # type: ignore[typeddict-item]
    return out
