"""Generated from Smithy shape ``com.amazonaws.sns#VerifySMSSandboxPhoneNumberResult``."""

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element


class VerifySMSSandboxPhoneNumberResult(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifySMSSandboxPhoneNumberResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> VerifySMSSandboxPhoneNumberResult:
    out: VerifySMSSandboxPhoneNumberResult = {}  # type: ignore[typeddict-item]
    return out
