"""Generated from Smithy shape ``com.amazonaws.autoscaling#PutWarmPoolAnswer``."""

from typing import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class PutWarmPoolAnswer(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: PutWarmPoolAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> PutWarmPoolAnswer:
    out: PutWarmPoolAnswer = {}  # type: ignore[typeddict-item]
    return out
