"""Generated from Smithy shape ``com.amazonaws.ses#DeleteIdentityPolicyResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class DeleteIdentityPolicyResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteIdentityPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteIdentityPolicyResponse:
    out: DeleteIdentityPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
