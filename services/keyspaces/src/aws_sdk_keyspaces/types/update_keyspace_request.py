"""Generated from Smithy shape ``com.amazonaws.keyspaces#UpdateKeyspaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.client_side_timestamps
    import aws_sdk_keyspaces.types.keyspace_name
    import aws_sdk_keyspaces.types.replication_specification


class UpdateKeyspaceRequest(TypedDict):
    keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p> The name of the keyspace. </p>"""
    replication_specification: (
        "aws_sdk_keyspaces.types.replication_specification.ReplicationSpecification"
    )
    client_side_timestamps: NotRequired[
        "aws_sdk_keyspaces.types.client_side_timestamps.ClientSideTimestamps"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateKeyspaceRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    import aws_sdk_keyspaces.types.replication_specification

    out["replicationSpecification"] = (
        aws_sdk_keyspaces.types.replication_specification.serialize_aws_json_1_0(
            value["replication_specification"]
        )
    )
    if "client_side_timestamps" in value:
        import aws_sdk_keyspaces.types.client_side_timestamps

        out["clientSideTimestamps"] = (
            aws_sdk_keyspaces.types.client_side_timestamps.serialize_aws_json_1_0(
                value["client_side_timestamps"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateKeyspaceRequest:
    out: UpdateKeyspaceRequest = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("UpdateKeyspaceRequest.keyspace_name required")
    if "replicationSpecification" in data:
        import aws_sdk_keyspaces.types.replication_specification

        out["replication_specification"] = (
            aws_sdk_keyspaces.types.replication_specification.deserialize_aws_json_1_0(
                data["replicationSpecification"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateKeyspaceRequest.replication_specification required"
        )
    if "clientSideTimestamps" in data:
        import aws_sdk_keyspaces.types.client_side_timestamps

        out["client_side_timestamps"] = (
            aws_sdk_keyspaces.types.client_side_timestamps.deserialize_aws_json_1_0(
                data["clientSideTimestamps"]
            )
        )
    return out
