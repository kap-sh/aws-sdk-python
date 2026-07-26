"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteDomainNameAccessAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class DeleteDomainNameAccessAssociationRequest(TypedDict, closed=True):
    domain_name_access_association_arn: "capo_api_gateway.types.string.String"
    """<p> The ARN of the domain name access association resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainNameAccessAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainNameAccessAssociationRequest:
    out: DeleteDomainNameAccessAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
