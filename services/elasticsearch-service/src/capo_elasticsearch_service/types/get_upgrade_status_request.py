"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#GetUpgradeStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name


class GetUpgradeStatusRequest(TypedDict, closed=True):
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"


# --- restJson1 ser/de ---
def serialize_json(value: GetUpgradeStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUpgradeStatusRequest:
    out: GetUpgradeStatusRequest = {}  # type: ignore[typeddict-item]
    return out
