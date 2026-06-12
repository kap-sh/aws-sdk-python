"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetCalculatedAttributeForProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list
    import aws_sdk_customer_profiles.types.calculated_attribute_value_list
    import aws_sdk_customer_profiles.types.condition_overrides


class BatchGetCalculatedAttributeForProfileResponse(TypedDict):
    errors: NotRequired[
        "aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list.BatchGetCalculatedAttributeForProfileErrorList"
    ]
    """<p>List of errors for calculated attribute values that could not be retrieved.</p>"""
    calculated_attribute_values: NotRequired[
        "aws_sdk_customer_profiles.types.calculated_attribute_value_list.CalculatedAttributeValueList"
    ]
    """<p>List of calculated attribute values retrieved.</p>"""
    condition_overrides: NotRequired[
        "aws_sdk_customer_profiles.types.condition_overrides.ConditionOverrides"
    ]
    """<p>Overrides the condition block within the original calculated attribute definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCalculatedAttributeForProfileResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list

        out["Errors"] = (
            aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list.serialize_json(
                value["errors"]
            )
        )
    if "calculated_attribute_values" in value:
        import aws_sdk_customer_profiles.types.calculated_attribute_value_list

        out["CalculatedAttributeValues"] = (
            aws_sdk_customer_profiles.types.calculated_attribute_value_list.serialize_json(
                value["calculated_attribute_values"]
            )
        )
    if "condition_overrides" in value:
        import aws_sdk_customer_profiles.types.condition_overrides

        out["ConditionOverrides"] = (
            aws_sdk_customer_profiles.types.condition_overrides.serialize_json(
                value["condition_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetCalculatedAttributeForProfileResponse:
    out: BatchGetCalculatedAttributeForProfileResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list

        out["errors"] = (
            aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list.deserialize_json(
                data["Errors"]
            )
        )
    if "CalculatedAttributeValues" in data:
        import aws_sdk_customer_profiles.types.calculated_attribute_value_list

        out["calculated_attribute_values"] = (
            aws_sdk_customer_profiles.types.calculated_attribute_value_list.deserialize_json(
                data["CalculatedAttributeValues"]
            )
        )
    if "ConditionOverrides" in data:
        import aws_sdk_customer_profiles.types.condition_overrides

        out["condition_overrides"] = (
            aws_sdk_customer_profiles.types.condition_overrides.deserialize_json(
                data["ConditionOverrides"]
            )
        )
    return out
