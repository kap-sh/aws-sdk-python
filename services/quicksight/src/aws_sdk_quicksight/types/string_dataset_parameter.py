"""Generated from Smithy shape ``com.amazonaws.quicksight#StringDatasetParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dataset_parameter_id
    import aws_sdk_quicksight.types.dataset_parameter_name
    import aws_sdk_quicksight.types.dataset_parameter_value_type
    import aws_sdk_quicksight.types.string_dataset_parameter_default_values


class StringDatasetParameter(TypedDict, closed=True):
    id: "aws_sdk_quicksight.types.dataset_parameter_id.DatasetParameterId"
    """<p>An identifier for the string parameter that is created in the dataset.</p>"""
    name: "aws_sdk_quicksight.types.dataset_parameter_name.DatasetParameterName"
    """<p>The name of the string parameter that is created in the dataset.</p>"""
    value_type: "aws_sdk_quicksight.types.dataset_parameter_value_type.DatasetParameterValueType"
    """<p>The value type of the dataset parameter. Valid values are <code>single value</code> or <code>multi value</code>.</p>"""
    default_values: NotRequired[
        "aws_sdk_quicksight.types.string_dataset_parameter_default_values.StringDatasetParameterDefaultValues"
    ]
    """<p>A list of default values for a given string dataset parameter type. This structure only accepts static values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringDatasetParameter) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.dataset_parameter_value_type

    out["ValueType"] = (
        aws_sdk_quicksight.types.dataset_parameter_value_type.serialize_json(
            value["value_type"]
        )
    )
    if "default_values" in value:
        import aws_sdk_quicksight.types.string_dataset_parameter_default_values

        out["DefaultValues"] = (
            aws_sdk_quicksight.types.string_dataset_parameter_default_values.serialize_json(
                value["default_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> StringDatasetParameter:
    out: StringDatasetParameter = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("StringDatasetParameter.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StringDatasetParameter.name required")
    if "ValueType" in data:
        import aws_sdk_quicksight.types.dataset_parameter_value_type

        out["value_type"] = (
            aws_sdk_quicksight.types.dataset_parameter_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    else:
        raise DeserializationError("StringDatasetParameter.value_type required")
    if "DefaultValues" in data:
        import aws_sdk_quicksight.types.string_dataset_parameter_default_values

        out["default_values"] = (
            aws_sdk_quicksight.types.string_dataset_parameter_default_values.deserialize_json(
                data["DefaultValues"]
            )
        )
    return out
