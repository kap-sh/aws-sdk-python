"""Generated from Smithy shape ``com.amazonaws.forecast#Featurizations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.featurization

Featurizations: TypeAlias = list["capo_forecast.types.featurization.Featurization"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Featurizations) -> list:
    import capo_forecast.types.featurization

    out: list = []
    for item in value:
        out.append(capo_forecast.types.featurization.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Featurizations:
    import capo_forecast.types.featurization

    out: Featurizations = []
    for item in data:
        out.append(capo_forecast.types.featurization.deserialize_aws_json_1_1(item))
    return out
