"""Generated from Smithy shape ``com.amazonaws.cloudformation#SetTypeDefaultVersionOutput``."""

from typing import TypedDict

from aws_sdk_cloudformation._protocol.xml import Element


class SetTypeDefaultVersionOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetTypeDefaultVersionOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> SetTypeDefaultVersionOutput:
    out: SetTypeDefaultVersionOutput = {}  # type: ignore[typeddict-item]
    return out
