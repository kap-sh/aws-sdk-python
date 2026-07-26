"""Generated from Smithy shape ``com.amazonaws.sagemaker#HolidayConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.holiday_config_attributes

HolidayConfig: TypeAlias = list[
    "capo_sagemaker.types.holiday_config_attributes.HolidayConfigAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HolidayConfig) -> list:
    import capo_sagemaker.types.holiday_config_attributes

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.holiday_config_attributes.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HolidayConfig:
    import capo_sagemaker.types.holiday_config_attributes

    out: HolidayConfig = []
    for item in data:
        out.append(
            capo_sagemaker.types.holiday_config_attributes.deserialize_aws_json_1_1(
                item
            )
        )
    return out
