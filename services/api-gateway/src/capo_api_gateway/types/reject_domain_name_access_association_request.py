"""Generated from Smithy shape ``com.amazonaws.apigateway#RejectDomainNameAccessAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class RejectDomainNameAccessAssociationRequest(TypedDict, closed=True):
    domain_name_access_association_arn: "capo_api_gateway.types.string.String"
    """<p>The ARN of the domain name access association resource. </p>"""
    domain_name_arn: "capo_api_gateway.types.string.String"
    """<p> The ARN of the domain name. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectDomainNameAccessAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RejectDomainNameAccessAssociationRequest:
    out: RejectDomainNameAccessAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
