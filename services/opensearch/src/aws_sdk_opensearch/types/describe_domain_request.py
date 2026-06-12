"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name


class DescribeDomainRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain that you want information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDomainRequest:
    out: DescribeDomainRequest = {}  # type: ignore[typeddict-item]
    return out
