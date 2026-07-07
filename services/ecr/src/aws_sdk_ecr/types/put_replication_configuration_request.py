"""Generated from Smithy shape ``com.amazonaws.ecr#PutReplicationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.replication_configuration


class PutReplicationConfigurationRequest(TypedDict, closed=True):
    replication_configuration: (
        "aws_sdk_ecr.types.replication_configuration.ReplicationConfiguration"
    )
    """<p>An object representing the replication configuration for a registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutReplicationConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_ecr.types.replication_configuration

    out["replicationConfiguration"] = (
        aws_sdk_ecr.types.replication_configuration.serialize_aws_json_1_1(
            value["replication_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutReplicationConfigurationRequest:
    out: PutReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "replicationConfiguration" in data:
        import aws_sdk_ecr.types.replication_configuration

        out["replication_configuration"] = (
            aws_sdk_ecr.types.replication_configuration.deserialize_aws_json_1_1(
                data["replicationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutReplicationConfigurationRequest.replication_configuration required"
        )
    return out
