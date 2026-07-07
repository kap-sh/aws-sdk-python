"""Generated from Smithy shape ``com.amazonaws.sns#DeleteSMSSandboxPhoneNumberResult``."""

from typing_extensions import TypedDict

from aws_sdk_sns._protocol.xml import Element


class DeleteSMSSandboxPhoneNumberResult(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSMSSandboxPhoneNumberResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteSMSSandboxPhoneNumberResult:
    out: DeleteSMSSandboxPhoneNumberResult = {}  # type: ignore[typeddict-item]
    return out
