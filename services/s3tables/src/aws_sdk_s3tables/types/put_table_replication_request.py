"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableReplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_arn
    import aws_sdk_s3tables.types.table_replication_configuration


class PutTableReplicationRequest(TypedDict):
    table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the source table.</p>"""
    version_token: NotRequired["str"]
    """<p>A version token from a previous GetTableReplication call. Use this token to ensure you're updating the expected version of the configuration.</p>"""
    configuration: "aws_sdk_s3tables.types.table_replication_configuration.TableReplicationConfiguration"
    """<p>The replication configuration to apply to the table, including the IAM role and replication rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableReplicationRequest) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.table_replication_configuration

    out["configuration"] = (
        aws_sdk_s3tables.types.table_replication_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTableReplicationRequest:
    out: PutTableReplicationRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_s3tables.types.table_replication_configuration

        out["configuration"] = (
            aws_sdk_s3tables.types.table_replication_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("PutTableReplicationRequest.configuration required")
    return out
