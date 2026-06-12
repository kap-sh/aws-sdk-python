"""Generated from Smithy shape ``com.amazonaws.appsync#GetApiAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.domain_name


class GetApiAssociationRequest(TypedDict):
    domain_name: "aws_sdk_appsync.types.domain_name.DomainName"
    """<p>The domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApiAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApiAssociationRequest:
    out: GetApiAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
