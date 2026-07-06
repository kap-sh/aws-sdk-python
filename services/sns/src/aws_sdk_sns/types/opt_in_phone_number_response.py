"""Generated from Smithy shape ``com.amazonaws.sns#OptInPhoneNumberResponse``."""

from typing_extensions import TypedDict

from aws_sdk_sns._protocol.xml import Element


class OptInPhoneNumberResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: OptInPhoneNumberResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> OptInPhoneNumberResponse:
    out: OptInPhoneNumberResponse = {}  # type: ignore[typeddict-item]
    return out
