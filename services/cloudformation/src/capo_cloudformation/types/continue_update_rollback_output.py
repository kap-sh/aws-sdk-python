"""Generated from Smithy shape ``com.amazonaws.cloudformation#ContinueUpdateRollbackOutput``."""

from typing_extensions import TypedDict

from capo_cloudformation._protocol.xml import Element


class ContinueUpdateRollbackOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: ContinueUpdateRollbackOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> ContinueUpdateRollbackOutput:
    out: ContinueUpdateRollbackOutput = {}  # type: ignore[typeddict-item]
    return out
