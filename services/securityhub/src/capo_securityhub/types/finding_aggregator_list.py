"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingAggregatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.finding_aggregator

FindingAggregatorList: TypeAlias = list[
    "capo_securityhub.types.finding_aggregator.FindingAggregator"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingAggregatorList) -> list:
    import capo_securityhub.types.finding_aggregator

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.finding_aggregator.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingAggregatorList:
    import capo_securityhub.types.finding_aggregator

    out: FindingAggregatorList = []
    for item in data:
        out.append(capo_securityhub.types.finding_aggregator.deserialize_json(item))
    return out
