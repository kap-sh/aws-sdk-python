"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableBucketReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_bucket_replication_configuration
    import capo_s3tables.types.version_token


class PutTableBucketReplicationRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the source table bucket.</p>"""
    version_token: NotRequired["capo_s3tables.types.version_token.VersionToken"]
    """<p>A version token from a previous GetTableBucketReplication call. Use this token to ensure you're updating the expected version of the configuration.</p>"""
    configuration: "capo_s3tables.types.table_bucket_replication_configuration.TableBucketReplicationConfiguration"
    """<p>The replication configuration to apply, including the IAM role and replication rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableBucketReplicationRequest) -> dict:
    out: dict = {}
    import capo_s3tables.types.table_bucket_replication_configuration

    out["configuration"] = (
        capo_s3tables.types.table_bucket_replication_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTableBucketReplicationRequest:
    out: PutTableBucketReplicationRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import capo_s3tables.types.table_bucket_replication_configuration

        out["configuration"] = (
            capo_s3tables.types.table_bucket_replication_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "PutTableBucketReplicationRequest.configuration required"
        )
    return out
