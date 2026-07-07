"""Generated from Smithy shape ``com.amazonaws.apigateway#GetDomainNamesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.nullable_integer
    import aws_sdk_api_gateway.types.resource_owner
    import aws_sdk_api_gateway.types.string


class GetDomainNamesRequest(TypedDict, closed=True):
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""
    limit: NotRequired["aws_sdk_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""
    resource_owner: NotRequired[
        "aws_sdk_api_gateway.types.resource_owner.ResourceOwner"
    ]
    """<p>The owner of the domain name access association. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainNamesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainNamesRequest:
    out: GetDomainNamesRequest = {}  # type: ignore[typeddict-item]
    return out
