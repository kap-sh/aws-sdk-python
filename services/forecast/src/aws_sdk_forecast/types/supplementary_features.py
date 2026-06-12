"""Generated from Smithy shape ``com.amazonaws.forecast#SupplementaryFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.supplementary_feature

SupplementaryFeatures: TypeAlias = list[
    "aws_sdk_forecast.types.supplementary_feature.SupplementaryFeature"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupplementaryFeatures) -> list:
    import aws_sdk_forecast.types.supplementary_feature

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.supplementary_feature.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SupplementaryFeatures:
    import aws_sdk_forecast.types.supplementary_feature

    out: SupplementaryFeatures = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.supplementary_feature.deserialize_aws_json_1_1(item)
        )
    return out
