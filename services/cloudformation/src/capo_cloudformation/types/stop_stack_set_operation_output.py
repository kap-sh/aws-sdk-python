"""Generated from Smithy shape ``com.amazonaws.cloudformation#StopStackSetOperationOutput``."""

from typing_extensions import TypedDict

from capo_cloudformation._protocol.xml import Element


class StopStackSetOperationOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: StopStackSetOperationOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> StopStackSetOperationOutput:
    out: StopStackSetOperationOutput = {}  # type: ignore[typeddict-item]
    return out
