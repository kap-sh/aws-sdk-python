"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteDomainNameAccessAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteDomainNameAccessAssociationRequest(TypedDict):
    domain_name_access_association_arn: "aws_sdk_api_gateway.types.string.String"
    """<p> The ARN of the domain name access association resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainNameAccessAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainNameAccessAssociationRequest:
    out: DeleteDomainNameAccessAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
