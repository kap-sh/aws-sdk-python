"""Generated from Smithy shape ``com.amazonaws.cloudformation#RecordHandlerProgressOutput``."""

from typing_extensions import TypedDict

from capo_cloudformation._protocol.xml import Element


class RecordHandlerProgressOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: RecordHandlerProgressOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> RecordHandlerProgressOutput:
    out: RecordHandlerProgressOutput = {}  # type: ignore[typeddict-item]
    return out
