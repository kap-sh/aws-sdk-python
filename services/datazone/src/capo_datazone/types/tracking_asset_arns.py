"""Generated from Smithy shape ``com.amazonaws.datazone#TrackingAssetArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.sage_maker_resource_arn

TrackingAssetArns: TypeAlias = list[
    "capo_datazone.types.sage_maker_resource_arn.SageMakerResourceArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrackingAssetArns) -> list:
    return list(value)


def deserialize_json(data: list) -> TrackingAssetArns:
    return list(data)
