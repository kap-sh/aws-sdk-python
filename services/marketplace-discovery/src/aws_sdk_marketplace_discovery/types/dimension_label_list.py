"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DimensionLabelList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.dimension_label

DimensionLabelList: TypeAlias = list["aws_sdk_marketplace_discovery.types.dimension_label.DimensionLabel"]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionLabelList) -> list:
    import aws_sdk_marketplace_discovery.types.dimension_label
    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_discovery.types.dimension_label.serialize_json(item))
    return out


def deserialize_json(data: list) -> DimensionLabelList:
    import aws_sdk_marketplace_discovery.types.dimension_label
    out: DimensionLabelList = []
    for item in data:
        out.append(aws_sdk_marketplace_discovery.types.dimension_label.deserialize_json(item))
    return out