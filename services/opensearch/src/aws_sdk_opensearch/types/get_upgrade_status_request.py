"""Generated from Smithy shape ``com.amazonaws.opensearch#GetUpgradeStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name


class GetUpgradeStatusRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The domain of the domain to get upgrade status information for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUpgradeStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUpgradeStatusRequest:
    out: GetUpgradeStatusRequest = {}  # type: ignore[typeddict-item]
    return out
