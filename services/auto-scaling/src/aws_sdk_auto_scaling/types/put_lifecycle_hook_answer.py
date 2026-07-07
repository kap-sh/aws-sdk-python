"""Generated from Smithy shape ``com.amazonaws.autoscaling#PutLifecycleHookAnswer``."""

from typing_extensions import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class PutLifecycleHookAnswer(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: PutLifecycleHookAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> PutLifecycleHookAnswer:
    out: PutLifecycleHookAnswer = {}  # type: ignore[typeddict-item]
    return out
