"""Generated from Smithy shape ``com.amazonaws.autoscaling#DeleteLifecycleHookAnswer``."""

from typing import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class DeleteLifecycleHookAnswer(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteLifecycleHookAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteLifecycleHookAnswer:
    out: DeleteLifecycleHookAnswer = {}  # type: ignore[typeddict-item]
    return out
