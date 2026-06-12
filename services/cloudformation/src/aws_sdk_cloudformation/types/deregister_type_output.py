"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeregisterTypeOutput``."""

from typing import TypedDict

from aws_sdk_cloudformation._protocol.xml import Element


class DeregisterTypeOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeregisterTypeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeregisterTypeOutput:
    out: DeregisterTypeOutput = {}  # type: ignore[typeddict-item]
    return out
