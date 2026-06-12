"""Generated from Smithy shape ``com.amazonaws.sns#VerifySMSSandboxPhoneNumberResult``."""

from typing import TypedDict

from aws_sdk_sns._protocol.xml import Element


class VerifySMSSandboxPhoneNumberResult(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifySMSSandboxPhoneNumberResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> VerifySMSSandboxPhoneNumberResult:
    out: VerifySMSSandboxPhoneNumberResult = {}  # type: ignore[typeddict-item]
    return out
