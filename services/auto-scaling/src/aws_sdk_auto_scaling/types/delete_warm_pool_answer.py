"""Generated from Smithy shape ``com.amazonaws.autoscaling#DeleteWarmPoolAnswer``."""

from typing import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class DeleteWarmPoolAnswer(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteWarmPoolAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteWarmPoolAnswer:
    out: DeleteWarmPoolAnswer = {}  # type: ignore[typeddict-item]
    return out
