"""Generated from Smithy shape ``com.amazonaws.sns#GetSMSSandboxAccountStatusInput``."""

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element


class GetSMSSandboxAccountStatusInput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSMSSandboxAccountStatusInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> GetSMSSandboxAccountStatusInput:
    out: GetSMSSandboxAccountStatusInput = {}  # type: ignore[typeddict-item]
    return out
