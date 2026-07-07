"""Generated from Smithy shape ``com.amazonaws.ses#SetIdentityMailFromDomainResponse``."""

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element


class SetIdentityMailFromDomainResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIdentityMailFromDomainResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> SetIdentityMailFromDomainResponse:
    out: SetIdentityMailFromDomainResponse = {}  # type: ignore[typeddict-item]
    return out
