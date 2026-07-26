"""Generated from Smithy shape ``com.amazonaws.forecast#CategoricalParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.name
    import capo_forecast.types.values


class CategoricalParameterRange(TypedDict, closed=True):
    name: "capo_forecast.types.name.Name"
    """<p>The name of the categorical hyperparameter to tune.</p>"""
    values: "capo_forecast.types.values.Values"
    """<p>A list of the tunable categories for the hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameterRange) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_forecast.types.values

    out["Values"] = capo_forecast.types.values.serialize_aws_json_1_1(value["values"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CategoricalParameterRange:
    out: CategoricalParameterRange = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CategoricalParameterRange.name required")
    if "Values" in data:
        import capo_forecast.types.values

        out["values"] = capo_forecast.types.values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        raise DeserializationError("CategoricalParameterRange.values required")
    return out
