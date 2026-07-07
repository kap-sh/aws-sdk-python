"""Generated from Smithy shape ``com.amazonaws.autoscaling#CompleteLifecycleActionAnswer``."""

from typing_extensions import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class CompleteLifecycleActionAnswer(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CompleteLifecycleActionAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CompleteLifecycleActionAnswer:
    out: CompleteLifecycleActionAnswer = {}  # type: ignore[typeddict-item]
    return out
