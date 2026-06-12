"""Generated from Smithy shape ``com.amazonaws.forecast#CategoricalParameterRange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.values


class CategoricalParameterRange(TypedDict):
    name: "aws_sdk_forecast.types.name.Name"
    """<p>The name of the categorical hyperparameter to tune.</p>"""
    values: "aws_sdk_forecast.types.values.Values"
    """<p>A list of the tunable categories for the hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameterRange) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_forecast.types.values

    out["Values"] = aws_sdk_forecast.types.values.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CategoricalParameterRange:
    out: CategoricalParameterRange = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CategoricalParameterRange.name required")
    if "Values" in data:
        import aws_sdk_forecast.types.values

        out["values"] = aws_sdk_forecast.types.values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        raise DeserializationError("CategoricalParameterRange.values required")
    return out
