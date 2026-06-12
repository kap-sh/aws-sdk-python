"""Generated from Smithy shape ``com.amazonaws.forecast#Featurizations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.featurization

Featurizations: TypeAlias = list["aws_sdk_forecast.types.featurization.Featurization"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Featurizations) -> list:
    import aws_sdk_forecast.types.featurization

    out: list = []
    for item in value:
        out.append(aws_sdk_forecast.types.featurization.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Featurizations:
    import aws_sdk_forecast.types.featurization

    out: Featurizations = []
    for item in data:
        out.append(aws_sdk_forecast.types.featurization.deserialize_aws_json_1_1(item))
    return out
