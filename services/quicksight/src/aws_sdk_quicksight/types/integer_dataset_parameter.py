"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerDatasetParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dataset_parameter_id
    import aws_sdk_quicksight.types.dataset_parameter_name
    import aws_sdk_quicksight.types.dataset_parameter_value_type
    import aws_sdk_quicksight.types.integer_dataset_parameter_default_values


class IntegerDatasetParameter(TypedDict):
    id: "aws_sdk_quicksight.types.dataset_parameter_id.DatasetParameterId"
    """<p>An identifier for the integer parameter created in the dataset.</p>"""
    name: "aws_sdk_quicksight.types.dataset_parameter_name.DatasetParameterName"
    """<p>The name of the integer parameter that is created in the dataset.</p>"""
    value_type: "aws_sdk_quicksight.types.dataset_parameter_value_type.DatasetParameterValueType"
    """<p>The value type of the dataset parameter. Valid values are <code>single value</code> or <code>multi value</code>.</p>"""
    default_values: NotRequired[
        "aws_sdk_quicksight.types.integer_dataset_parameter_default_values.IntegerDatasetParameterDefaultValues"
    ]
    """<p>A list of default values for a given integer parameter. This structure only accepts static values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerDatasetParameter) -> dict:
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
        import aws_sdk_quicksight.types.integer_dataset_parameter_default_values

        out["DefaultValues"] = (
            aws_sdk_quicksight.types.integer_dataset_parameter_default_values.serialize_json(
                value["default_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntegerDatasetParameter:
    out: IntegerDatasetParameter = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("IntegerDatasetParameter.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("IntegerDatasetParameter.name required")
    if "ValueType" in data:
        import aws_sdk_quicksight.types.dataset_parameter_value_type

        out["value_type"] = (
            aws_sdk_quicksight.types.dataset_parameter_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    else:
        raise DeserializationError("IntegerDatasetParameter.value_type required")
    if "DefaultValues" in data:
        import aws_sdk_quicksight.types.integer_dataset_parameter_default_values

        out["default_values"] = (
            aws_sdk_quicksight.types.integer_dataset_parameter_default_values.deserialize_json(
                data["DefaultValues"]
            )
        )
    return out
