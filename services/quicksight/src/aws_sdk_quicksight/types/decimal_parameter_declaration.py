"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalParameterDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.decimal_default_values
    import aws_sdk_quicksight.types.decimal_value_when_unset_configuration
    import aws_sdk_quicksight.types.mapped_data_set_parameters
    import aws_sdk_quicksight.types.parameter_name
    import aws_sdk_quicksight.types.parameter_value_type


class DecimalParameterDeclaration(TypedDict, closed=True):
    parameter_value_type: (
        "aws_sdk_quicksight.types.parameter_value_type.ParameterValueType"
    )
    """<p>The value type determines whether the parameter is a single-value or multi-value parameter.</p>"""
    name: "aws_sdk_quicksight.types.parameter_name.ParameterName"
    """<p>The name of the parameter that is being declared.</p>"""
    default_values: NotRequired[
        "aws_sdk_quicksight.types.decimal_default_values.DecimalDefaultValues"
    ]
    """<p>The default values of a parameter. If the parameter is a single-value parameter, a maximum of one default value can be provided.</p>"""
    value_when_unset: NotRequired[
        "aws_sdk_quicksight.types.decimal_value_when_unset_configuration.DecimalValueWhenUnsetConfiguration"
    ]
    """<p>The configuration that defines the default value of a <code>Decimal</code> parameter when a value has not been set.</p>"""
    mapped_data_set_parameters: NotRequired[
        "aws_sdk_quicksight.types.mapped_data_set_parameters.MappedDataSetParameters"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DecimalParameterDeclaration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.parameter_value_type

    out["ParameterValueType"] = (
        aws_sdk_quicksight.types.parameter_value_type.serialize_json(
            value["parameter_value_type"]
        )
    )
    out["Name"] = value["name"]
    if "default_values" in value:
        import aws_sdk_quicksight.types.decimal_default_values

        out["DefaultValues"] = (
            aws_sdk_quicksight.types.decimal_default_values.serialize_json(
                value["default_values"]
            )
        )
    if "value_when_unset" in value:
        import aws_sdk_quicksight.types.decimal_value_when_unset_configuration

        out["ValueWhenUnset"] = (
            aws_sdk_quicksight.types.decimal_value_when_unset_configuration.serialize_json(
                value["value_when_unset"]
            )
        )
    if "mapped_data_set_parameters" in value:
        import aws_sdk_quicksight.types.mapped_data_set_parameters

        out["MappedDataSetParameters"] = (
            aws_sdk_quicksight.types.mapped_data_set_parameters.serialize_json(
                value["mapped_data_set_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> DecimalParameterDeclaration:
    out: DecimalParameterDeclaration = {}  # type: ignore[typeddict-item]
    if "ParameterValueType" in data:
        import aws_sdk_quicksight.types.parameter_value_type

        out["parameter_value_type"] = (
            aws_sdk_quicksight.types.parameter_value_type.deserialize_json(
                data["ParameterValueType"]
            )
        )
    else:
        raise DeserializationError(
            "DecimalParameterDeclaration.parameter_value_type required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DecimalParameterDeclaration.name required")
    if "DefaultValues" in data:
        import aws_sdk_quicksight.types.decimal_default_values

        out["default_values"] = (
            aws_sdk_quicksight.types.decimal_default_values.deserialize_json(
                data["DefaultValues"]
            )
        )
    if "ValueWhenUnset" in data:
        import aws_sdk_quicksight.types.decimal_value_when_unset_configuration

        out["value_when_unset"] = (
            aws_sdk_quicksight.types.decimal_value_when_unset_configuration.deserialize_json(
                data["ValueWhenUnset"]
            )
        )
    if "MappedDataSetParameters" in data:
        import aws_sdk_quicksight.types.mapped_data_set_parameters

        out["mapped_data_set_parameters"] = (
            aws_sdk_quicksight.types.mapped_data_set_parameters.deserialize_json(
                data["MappedDataSetParameters"]
            )
        )
    return out
