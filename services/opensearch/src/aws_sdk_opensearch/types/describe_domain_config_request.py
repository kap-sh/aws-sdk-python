"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name


class DescribeDomainConfigRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>Name of the OpenSearch Service domain configuration that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDomainConfigRequest:
    out: DescribeDomainConfigRequest = {}  # type: ignore[typeddict-item]
    return out
