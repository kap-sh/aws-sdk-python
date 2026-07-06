"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainHealthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name


class DescribeDomainHealthRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainHealthRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDomainHealthRequest:
    out: DescribeDomainHealthRequest = {}  # type: ignore[typeddict-item]
    return out
