"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainChangeProgressRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.guid


class DescribeDomainChangeProgressRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain to get progress information for.</p>"""
    change_id: NotRequired["aws_sdk_opensearch.types.guid.GUID"]
    """<p>The specific change ID for which you want to get progress information. If omitted, the request returns information about the most recent configuration change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainChangeProgressRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDomainChangeProgressRequest:
    out: DescribeDomainChangeProgressRequest = {}  # type: ignore[typeddict-item]
    return out
