"""Generated from Smithy shape ``com.amazonaws.forecast#SupplementaryFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.supplementary_feature

SupplementaryFeatures: TypeAlias = list[
    "capo_forecast.types.supplementary_feature.SupplementaryFeature"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupplementaryFeatures) -> list:
    import capo_forecast.types.supplementary_feature

    out: list = []
    for item in value:
        out.append(
            capo_forecast.types.supplementary_feature.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SupplementaryFeatures:
    import capo_forecast.types.supplementary_feature

    out: SupplementaryFeatures = []
    for item in data:
        out.append(
            capo_forecast.types.supplementary_feature.deserialize_aws_json_1_1(item)
        )
    return out
