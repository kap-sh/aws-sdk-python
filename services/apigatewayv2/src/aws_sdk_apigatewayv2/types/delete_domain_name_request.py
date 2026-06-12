"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteDomainNameRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeleteDomainNameRequest(TypedDict):
    domain_name: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainNameRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainNameRequest:
    out: DeleteDomainNameRequest = {}  # type: ignore[typeddict-item]
    return out
