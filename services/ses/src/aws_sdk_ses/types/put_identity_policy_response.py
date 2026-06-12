"""Generated from Smithy shape ``com.amazonaws.ses#PutIdentityPolicyResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class PutIdentityPolicyResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: PutIdentityPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> PutIdentityPolicyResponse:
    out: PutIdentityPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
