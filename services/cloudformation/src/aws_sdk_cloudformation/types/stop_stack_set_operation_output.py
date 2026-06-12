"""Generated from Smithy shape ``com.amazonaws.cloudformation#StopStackSetOperationOutput``."""

from typing import TypedDict

from aws_sdk_cloudformation._protocol.xml import Element


class StopStackSetOperationOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: StopStackSetOperationOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> StopStackSetOperationOutput:
    out: StopStackSetOperationOutput = {}  # type: ignore[typeddict-item]
    return out
