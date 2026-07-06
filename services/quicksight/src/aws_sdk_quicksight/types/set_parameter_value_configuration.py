"""Generated from Smithy shape ``com.amazonaws.quicksight#SetParameterValueConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.destination_parameter_value_configuration
    import aws_sdk_quicksight.types.parameter_name


class SetParameterValueConfiguration(TypedDict, closed=True):
    destination_parameter_name: "aws_sdk_quicksight.types.parameter_name.ParameterName"
    """<p>The destination parameter name of the <code>SetParameterValueConfiguration</code>.</p>"""
    value: "aws_sdk_quicksight.types.destination_parameter_value_configuration.DestinationParameterValueConfiguration"


# --- restJson1 ser/de ---
def serialize_json(value: SetParameterValueConfiguration) -> dict:
    out: dict = {}
    out["DestinationParameterName"] = value["destination_parameter_name"]
    import aws_sdk_quicksight.types.destination_parameter_value_configuration

    out["Value"] = (
        aws_sdk_quicksight.types.destination_parameter_value_configuration.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> SetParameterValueConfiguration:
    out: SetParameterValueConfiguration = {}  # type: ignore[typeddict-item]
    if "DestinationParameterName" in data:
        out["destination_parameter_name"] = data["DestinationParameterName"]
    else:
        raise DeserializationError(
            "SetParameterValueConfiguration.destination_parameter_name required"
        )
    if "Value" in data:
        import aws_sdk_quicksight.types.destination_parameter_value_configuration

        out["value"] = (
            aws_sdk_quicksight.types.destination_parameter_value_configuration.deserialize_json(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("SetParameterValueConfiguration.value required")
    return out
