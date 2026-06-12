"""Generated from Smithy shape ``com.amazonaws.sns#CreateSMSSandboxPhoneNumberResult``."""

from typing import TypedDict

from aws_sdk_sns._protocol.xml import Element


class CreateSMSSandboxPhoneNumberResult(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateSMSSandboxPhoneNumberResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CreateSMSSandboxPhoneNumberResult:
    out: CreateSMSSandboxPhoneNumberResult = {}  # type: ignore[typeddict-item]
    return out
