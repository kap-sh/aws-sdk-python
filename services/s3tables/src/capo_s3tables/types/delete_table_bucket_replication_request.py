"""Generated from Smithy shape ``com.amazonaws.s3tables#DeleteTableBucketReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.version_token


class DeleteTableBucketReplicationRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""
    version_token: NotRequired["capo_s3tables.types.version_token.VersionToken"]
    """<p>A version token from a previous GetTableBucketReplication call. Use this token to ensure you're deleting the expected version of the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTableBucketReplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTableBucketReplicationRequest:
    out: DeleteTableBucketReplicationRequest = {}  # type: ignore[typeddict-item]
    return out
