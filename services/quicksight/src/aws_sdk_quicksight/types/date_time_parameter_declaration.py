"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeParameterDeclaration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.date_time_default_values
    import aws_sdk_quicksight.types.date_time_value_when_unset_configuration
    import aws_sdk_quicksight.types.mapped_data_set_parameters
    import aws_sdk_quicksight.types.parameter_name
    import aws_sdk_quicksight.types.time_granularity


class DateTimeParameterDeclaration(TypedDict):
    name: "aws_sdk_quicksight.types.parameter_name.ParameterName"
    """<p>The name of the parameter that is being declared.</p>"""
    default_values: NotRequired[
        "aws_sdk_quicksight.types.date_time_default_values.DateTimeDefaultValues"
    ]
    """<p>The default values of a parameter. If the parameter is a single-value parameter, a maximum of one default value can be provided.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    value_when_unset: NotRequired[
        "aws_sdk_quicksight.types.date_time_value_when_unset_configuration.DateTimeValueWhenUnsetConfiguration"
    ]
    """<p>The configuration that defines the default value of a <code>DateTime</code> parameter when a value has not been set.</p>"""
    mapped_data_set_parameters: NotRequired[
        "aws_sdk_quicksight.types.mapped_data_set_parameters.MappedDataSetParameters"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeParameterDeclaration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "default_values" in value:
        import aws_sdk_quicksight.types.date_time_default_values

        out["DefaultValues"] = (
            aws_sdk_quicksight.types.date_time_default_values.serialize_json(
                value["default_values"]
            )
        )
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "value_when_unset" in value:
        import aws_sdk_quicksight.types.date_time_value_when_unset_configuration

        out["ValueWhenUnset"] = (
            aws_sdk_quicksight.types.date_time_value_when_unset_configuration.serialize_json(
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


def deserialize_json(data: dict) -> DateTimeParameterDeclaration:
    out: DateTimeParameterDeclaration = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DateTimeParameterDeclaration.name required")
    if "DefaultValues" in data:
        import aws_sdk_quicksight.types.date_time_default_values

        out["default_values"] = (
            aws_sdk_quicksight.types.date_time_default_values.deserialize_json(
                data["DefaultValues"]
            )
        )
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "ValueWhenUnset" in data:
        import aws_sdk_quicksight.types.date_time_value_when_unset_configuration

        out["value_when_unset"] = (
            aws_sdk_quicksight.types.date_time_value_when_unset_configuration.deserialize_json(
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
