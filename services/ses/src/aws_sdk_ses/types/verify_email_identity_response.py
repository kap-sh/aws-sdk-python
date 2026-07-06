"""Generated from Smithy shape ``com.amazonaws.ses#VerifyEmailIdentityResponse``."""

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element


class VerifyEmailIdentityResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifyEmailIdentityResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> VerifyEmailIdentityResponse:
    out: VerifyEmailIdentityResponse = {}  # type: ignore[typeddict-item]
    return out
