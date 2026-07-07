"""Generated from Smithy shape ``com.amazonaws.cloudformation#ExecuteChangeSetOutput``."""

from typing_extensions import TypedDict

from aws_sdk_cloudformation._protocol.xml import Element


class ExecuteChangeSetOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: ExecuteChangeSetOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> ExecuteChangeSetOutput:
    out: ExecuteChangeSetOutput = {}  # type: ignore[typeddict-item]
    return out
