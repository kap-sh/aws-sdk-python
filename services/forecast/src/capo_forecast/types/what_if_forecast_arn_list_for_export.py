"""Generated from Smithy shape ``com.amazonaws.forecast#WhatIfForecastArnListForExport``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.long_arn

WhatIfForecastArnListForExport: TypeAlias = list["capo_forecast.types.long_arn.LongArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WhatIfForecastArnListForExport) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WhatIfForecastArnListForExport:
    return list(data)
