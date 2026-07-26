"""Generated from Smithy shape ``com.amazonaws.forecast#Action``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.double
    import capo_forecast.types.name
    import capo_forecast.types.operation


class Action(TypedDict, closed=True):
    attribute_name: "capo_forecast.types.name.Name"
    """<p>The related time series that you are modifying. This value is case insensitive.</p>"""
    operation: "capo_forecast.types.operation.Operation"
    """<p>The operation that is applied to the provided attribute. Operations include:</p> <ul> <li> <p> <code>ADD</code> - adds <code>Value</code> to all rows of <code>AttributeName</code>.</p> </li> <li> <p> <code>SUBTRACT</code> - subtracts <code>Value</code> from all rows of <code>AttributeName</code>.</p> </li> <li> <p> <code>MULTIPLY</code> - multiplies all rows of <code>AttributeName</code> by <code>Value</code>.</p> </li> <li> <p> <code>DIVIDE</code> - divides all rows of <code>AttributeName</code> by <code>Value</code>.</p> </li> </ul>"""
    value: "capo_forecast.types.double.Double"
    """<p>The value that is applied for the chosen <code>Operation</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Action) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import capo_forecast.types.operation

    out["Operation"] = capo_forecast.types.operation.serialize_aws_json_1_1(
        value["operation"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("Action.attribute_name required")
    if "Operation" in data:
        import capo_forecast.types.operation

        out["operation"] = capo_forecast.types.operation.deserialize_aws_json_1_1(
            data["Operation"]
        )
    else:
        raise DeserializationError("Action.operation required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Action.value required")
    return out
