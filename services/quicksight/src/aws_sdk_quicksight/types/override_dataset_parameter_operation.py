"""Generated from Smithy shape ``com.amazonaws.quicksight#OverrideDatasetParameterOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dataset_parameter_name
    import aws_sdk_quicksight.types.new_default_values


class OverrideDatasetParameterOperation(TypedDict):
    parameter_name: (
        "aws_sdk_quicksight.types.dataset_parameter_name.DatasetParameterName"
    )
    """<p>The name of the parameter to be overridden with different values.</p>"""
    new_parameter_name: NotRequired[
        "aws_sdk_quicksight.types.dataset_parameter_name.DatasetParameterName"
    ]
    """<p>The new name for the parameter.</p>"""
    new_default_values: NotRequired[
        "aws_sdk_quicksight.types.new_default_values.NewDefaultValues"
    ]
    """<p>The new default values for the parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverrideDatasetParameterOperation) -> dict:
    out: dict = {}
    out["ParameterName"] = value["parameter_name"]
    if "new_parameter_name" in value:
        out["NewParameterName"] = value["new_parameter_name"]
    if "new_default_values" in value:
        import aws_sdk_quicksight.types.new_default_values

        out["NewDefaultValues"] = (
            aws_sdk_quicksight.types.new_default_values.serialize_json(
                value["new_default_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> OverrideDatasetParameterOperation:
    out: OverrideDatasetParameterOperation = {}  # type: ignore[typeddict-item]
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    else:
        raise DeserializationError(
            "OverrideDatasetParameterOperation.parameter_name required"
        )
    if "NewParameterName" in data:
        out["new_parameter_name"] = data["NewParameterName"]
    if "NewDefaultValues" in data:
        import aws_sdk_quicksight.types.new_default_values

        out["new_default_values"] = (
            aws_sdk_quicksight.types.new_default_values.deserialize_json(
                data["NewDefaultValues"]
            )
        )
    return out
