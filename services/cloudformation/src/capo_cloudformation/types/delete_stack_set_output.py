"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeleteStackSetOutput``."""

from typing_extensions import TypedDict

from capo_cloudformation._protocol.xml import Element


class DeleteStackSetOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteStackSetOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteStackSetOutput:
    out: DeleteStackSetOutput = {}  # type: ignore[typeddict-item]
    return out
