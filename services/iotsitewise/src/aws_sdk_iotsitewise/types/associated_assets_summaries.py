"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssociatedAssetsSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.associated_assets_summary

AssociatedAssetsSummaries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.associated_assets_summary.AssociatedAssetsSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedAssetsSummaries) -> list:
    import aws_sdk_iotsitewise.types.associated_assets_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.associated_assets_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociatedAssetsSummaries:
    import aws_sdk_iotsitewise.types.associated_assets_summary

    out: AssociatedAssetsSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.associated_assets_summary.deserialize_json(item)
        )
    return out
