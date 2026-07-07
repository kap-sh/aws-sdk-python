"""Generated from Smithy shape ``com.amazonaws.eventbridge#ReplicationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.replication_state


class ReplicationConfig(TypedDict, closed=True):
    state: NotRequired["aws_sdk_eventbridge.types.replication_state.ReplicationState"]
    """<p>The state of event replication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationConfig) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_eventbridge.types.replication_state

        out["State"] = (
            aws_sdk_eventbridge.types.replication_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationConfig:
    out: ReplicationConfig = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_eventbridge.types.replication_state

        out["state"] = (
            aws_sdk_eventbridge.types.replication_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out
