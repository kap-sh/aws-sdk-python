"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetPropertySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_summary

AssetPropertySummaries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_property_summary.AssetPropertySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertySummaries) -> list:
    import aws_sdk_iotsitewise.types.asset_property_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.asset_property_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetPropertySummaries:
    import aws_sdk_iotsitewise.types.asset_property_summary

    out: AssetPropertySummaries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.asset_property_summary.deserialize_json(item)
        )
    return out
