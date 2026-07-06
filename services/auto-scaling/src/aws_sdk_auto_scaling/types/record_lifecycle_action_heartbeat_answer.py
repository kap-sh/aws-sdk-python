"""Generated from Smithy shape ``com.amazonaws.autoscaling#RecordLifecycleActionHeartbeatAnswer``."""

from typing_extensions import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class RecordLifecycleActionHeartbeatAnswer(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: RecordLifecycleActionHeartbeatAnswer,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> RecordLifecycleActionHeartbeatAnswer:
    out: RecordLifecycleActionHeartbeatAnswer = {}  # type: ignore[typeddict-item]
    return out
