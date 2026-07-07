"""Generated from Smithy shape ``com.amazonaws.autoscaling#PutWarmPoolAnswer``."""

from typing_extensions import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class PutWarmPoolAnswer(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: PutWarmPoolAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> PutWarmPoolAnswer:
    out: PutWarmPoolAnswer = {}  # type: ignore[typeddict-item]
    return out
