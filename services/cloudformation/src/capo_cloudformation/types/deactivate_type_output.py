"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeactivateTypeOutput``."""

from typing_extensions import TypedDict

from capo_cloudformation._protocol.xml import Element


class DeactivateTypeOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeactivateTypeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeactivateTypeOutput:
    out: DeactivateTypeOutput = {}  # type: ignore[typeddict-item]
    return out
