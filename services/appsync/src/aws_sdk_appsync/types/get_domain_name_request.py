"""Generated from Smithy shape ``com.amazonaws.appsync#GetDomainNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.domain_name


class GetDomainNameRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_appsync.types.domain_name.DomainName"
    """<p>The domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainNameRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainNameRequest:
    out: GetDomainNameRequest = {}  # type: ignore[typeddict-item]
    return out
