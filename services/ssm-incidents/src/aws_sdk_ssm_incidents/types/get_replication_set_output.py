"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetReplicationSetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.replication_set


class GetReplicationSetOutput(TypedDict, closed=True):
    replication_set: "aws_sdk_ssm_incidents.types.replication_set.ReplicationSet"
    """<p>Details of the replication set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReplicationSetOutput) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.replication_set

    out["replicationSet"] = aws_sdk_ssm_incidents.types.replication_set.serialize_json(
        value["replication_set"]
    )
    return out


def deserialize_json(data: dict) -> GetReplicationSetOutput:
    out: GetReplicationSetOutput = {}  # type: ignore[typeddict-item]
    if "replicationSet" in data:
        import aws_sdk_ssm_incidents.types.replication_set

        out["replication_set"] = (
            aws_sdk_ssm_incidents.types.replication_set.deserialize_json(
                data["replicationSet"]
            )
        )
    else:
        raise DeserializationError("GetReplicationSetOutput.replication_set required")
    return out
