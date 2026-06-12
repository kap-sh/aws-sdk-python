"""Generated from Smithy shape ``com.amazonaws.ses#DeleteIdentityResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class DeleteIdentityResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteIdentityResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteIdentityResponse:
    out: DeleteIdentityResponse = {}  # type: ignore[typeddict-item]
    return out
