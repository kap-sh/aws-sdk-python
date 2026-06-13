"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerDatasetParameterDefaultValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.integer_dataset_parameter_value_list


class IntegerDatasetParameterDefaultValues(TypedDict):
    static_values: NotRequired[
        "aws_sdk_quicksight.types.integer_dataset_parameter_value_list.IntegerDatasetParameterValueList"
    ]
    """<p>A list of static default values for a given integer parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerDatasetParameterDefaultValues) -> dict:
    out: dict = {}
    if "static_values" in value:
        import aws_sdk_quicksight.types.integer_dataset_parameter_value_list

        out["StaticValues"] = (
            aws_sdk_quicksight.types.integer_dataset_parameter_value_list.serialize_json(
                value["static_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntegerDatasetParameterDefaultValues:
    out: IntegerDatasetParameterDefaultValues = {}  # type: ignore[typeddict-item]
    if "StaticValues" in data:
        import aws_sdk_quicksight.types.integer_dataset_parameter_value_list

        out["static_values"] = (
            aws_sdk_quicksight.types.integer_dataset_parameter_value_list.deserialize_json(
                data["StaticValues"]
            )
        )
    return out
