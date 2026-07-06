"""Generated from Smithy shape ``com.amazonaws.ecr#PutReplicationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.replication_configuration


class PutReplicationConfigurationResponse(TypedDict, closed=True):
    replication_configuration: NotRequired[
        "aws_sdk_ecr.types.replication_configuration.ReplicationConfiguration"
    ]
    """<p>The contents of the replication configuration for the registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutReplicationConfigurationResponse) -> dict:
    out: dict = {}
    if "replication_configuration" in value:
        import aws_sdk_ecr.types.replication_configuration

        out["replicationConfiguration"] = (
            aws_sdk_ecr.types.replication_configuration.serialize_aws_json_1_1(
                value["replication_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutReplicationConfigurationResponse:
    out: PutReplicationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "replicationConfiguration" in data:
        import aws_sdk_ecr.types.replication_configuration

        out["replication_configuration"] = (
            aws_sdk_ecr.types.replication_configuration.deserialize_aws_json_1_1(
                data["replicationConfiguration"]
            )
        )
    return out
