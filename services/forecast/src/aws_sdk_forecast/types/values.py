"""Generated from Smithy shape ``com.amazonaws.forecast#Values``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.value

Values: TypeAlias = list["aws_sdk_forecast.types.value.Value"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Values) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Values:
    return list(data)
