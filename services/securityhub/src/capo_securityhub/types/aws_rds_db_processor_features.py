"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbProcessorFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_processor_feature

AwsRdsDbProcessorFeatures: TypeAlias = list[
    "capo_securityhub.types.aws_rds_db_processor_feature.AwsRdsDbProcessorFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbProcessorFeatures) -> list:
    import capo_securityhub.types.aws_rds_db_processor_feature

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_rds_db_processor_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbProcessorFeatures:
    import capo_securityhub.types.aws_rds_db_processor_feature

    out: AwsRdsDbProcessorFeatures = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_rds_db_processor_feature.deserialize_json(item)
        )
    return out
