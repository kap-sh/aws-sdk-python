"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomValuesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean_object
    import aws_sdk_quicksight.types.custom_parameter_values


class CustomValuesConfiguration(TypedDict, closed=True):
    include_null_value: NotRequired[
        "aws_sdk_quicksight.types.boolean_object.BooleanObject"
    ]
    """<p>Includes the null value in custom action parameter values.</p>"""
    custom_values: (
        "aws_sdk_quicksight.types.custom_parameter_values.CustomParameterValues"
    )


# --- restJson1 ser/de ---
def serialize_json(value: CustomValuesConfiguration) -> dict:
    out: dict = {}
    if "include_null_value" in value:
        out["IncludeNullValue"] = value["include_null_value"]
    import aws_sdk_quicksight.types.custom_parameter_values

    out["CustomValues"] = (
        aws_sdk_quicksight.types.custom_parameter_values.serialize_json(
            value["custom_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomValuesConfiguration:
    out: CustomValuesConfiguration = {}  # type: ignore[typeddict-item]
    if "IncludeNullValue" in data:
        out["include_null_value"] = data["IncludeNullValue"]
    if "CustomValues" in data:
        import aws_sdk_quicksight.types.custom_parameter_values

        out["custom_values"] = (
            aws_sdk_quicksight.types.custom_parameter_values.deserialize_json(
                data["CustomValues"]
            )
        )
    else:
        raise DeserializationError("CustomValuesConfiguration.custom_values required")
    return out
