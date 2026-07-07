"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomActionSetParametersOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.set_parameter_value_configuration_list


class CustomActionSetParametersOperation(TypedDict, closed=True):
    parameter_value_configurations: "aws_sdk_quicksight.types.set_parameter_value_configuration_list.SetParameterValueConfigurationList"
    """<p>The parameter that determines the value configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionSetParametersOperation) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.set_parameter_value_configuration_list

    out["ParameterValueConfigurations"] = (
        aws_sdk_quicksight.types.set_parameter_value_configuration_list.serialize_json(
            value["parameter_value_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomActionSetParametersOperation:
    out: CustomActionSetParametersOperation = {}  # type: ignore[typeddict-item]
    if "ParameterValueConfigurations" in data:
        import aws_sdk_quicksight.types.set_parameter_value_configuration_list

        out["parameter_value_configurations"] = (
            aws_sdk_quicksight.types.set_parameter_value_configuration_list.deserialize_json(
                data["ParameterValueConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CustomActionSetParametersOperation.parameter_value_configurations required"
        )
    return out
