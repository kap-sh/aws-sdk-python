"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeactivateTypeOutput``."""

from typing import TypedDict

from aws_sdk_cloudformation._protocol.xml import Element


class DeactivateTypeOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeactivateTypeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeactivateTypeOutput:
    out: DeactivateTypeOutput = {}  # type: ignore[typeddict-item]
    return out
