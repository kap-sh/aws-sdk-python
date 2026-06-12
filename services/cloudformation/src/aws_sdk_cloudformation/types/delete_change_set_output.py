"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeleteChangeSetOutput``."""

from typing import TypedDict

from aws_sdk_cloudformation._protocol.xml import Element


class DeleteChangeSetOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteChangeSetOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteChangeSetOutput:
    out: DeleteChangeSetOutput = {}  # type: ignore[typeddict-item]
    return out
