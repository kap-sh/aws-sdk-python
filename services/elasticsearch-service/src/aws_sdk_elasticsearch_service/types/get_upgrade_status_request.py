"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#GetUpgradeStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name


class GetUpgradeStatusRequest(TypedDict):
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"


# --- restJson1 ser/de ---
def serialize_json(value: GetUpgradeStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUpgradeStatusRequest:
    out: GetUpgradeStatusRequest = {}  # type: ignore[typeddict-item]
    return out
