"""Generated from Smithy shape ``com.amazonaws.securityhub#AggregatorV2List``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aggregator_v2

AggregatorV2List: TypeAlias = list[
    "aws_sdk_securityhub.types.aggregator_v2.AggregatorV2"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregatorV2List) -> list:
    import aws_sdk_securityhub.types.aggregator_v2

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.aggregator_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregatorV2List:
    import aws_sdk_securityhub.types.aggregator_v2

    out: AggregatorV2List = []
    for item in data:
        out.append(aws_sdk_securityhub.types.aggregator_v2.deserialize_json(item))
    return out
