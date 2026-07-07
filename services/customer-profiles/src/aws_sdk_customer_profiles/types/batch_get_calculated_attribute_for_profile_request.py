"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetCalculatedAttributeForProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list
    import aws_sdk_customer_profiles.types.condition_overrides
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.type_name


class BatchGetCalculatedAttributeForProfileRequest(TypedDict, closed=True):
    calculated_attribute_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the calculated attribute.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    profile_ids: "aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list.BatchGetCalculatedAttributeForProfileIdList"
    """<p>List of unique identifiers for customer profiles to retrieve.</p>"""
    condition_overrides: NotRequired[
        "aws_sdk_customer_profiles.types.condition_overrides.ConditionOverrides"
    ]
    """<p>Overrides the condition block within the original calculated attribute definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCalculatedAttributeForProfileRequest) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list

    out["ProfileIds"] = (
        aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list.serialize_json(
            value["profile_ids"]
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


def deserialize_json(data: dict) -> BatchGetCalculatedAttributeForProfileRequest:
    out: BatchGetCalculatedAttributeForProfileRequest = {}  # type: ignore[typeddict-item]
    if "ProfileIds" in data:
        import aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list

        out["profile_ids"] = (
            aws_sdk_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list.deserialize_json(
                data["ProfileIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetCalculatedAttributeForProfileRequest.profile_ids required"
        )
    if "ConditionOverrides" in data:
        import aws_sdk_customer_profiles.types.condition_overrides

        out["condition_overrides"] = (
            aws_sdk_customer_profiles.types.condition_overrides.deserialize_json(
                data["ConditionOverrides"]
            )
        )
    return out
