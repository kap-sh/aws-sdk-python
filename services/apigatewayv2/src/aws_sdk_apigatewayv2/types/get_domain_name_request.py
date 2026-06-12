"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetDomainNameRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetDomainNameRequest(TypedDict):
    domain_name: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainNameRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainNameRequest:
    out: GetDomainNameRequest = {}  # type: ignore[typeddict-item]
    return out
