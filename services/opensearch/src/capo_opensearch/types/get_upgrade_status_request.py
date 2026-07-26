"""Generated from Smithy shape ``com.amazonaws.opensearch#GetUpgradeStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name


class GetUpgradeStatusRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The domain of the domain to get upgrade status information for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUpgradeStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUpgradeStatusRequest:
    out: GetUpgradeStatusRequest = {}  # type: ignore[typeddict-item]
    return out
