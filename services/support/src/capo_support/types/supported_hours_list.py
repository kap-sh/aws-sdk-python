"""Generated from Smithy shape ``com.amazonaws.support#SupportedHoursList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.supported_hour

SupportedHoursList: TypeAlias = list["capo_support.types.supported_hour.SupportedHour"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedHoursList) -> list:
    import capo_support.types.supported_hour

    out: list = []
    for item in value:
        out.append(capo_support.types.supported_hour.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SupportedHoursList:
    import capo_support.types.supported_hour

    out: SupportedHoursList = []
    for item in data:
        out.append(capo_support.types.supported_hour.deserialize_aws_json_1_1(item))
    return out
