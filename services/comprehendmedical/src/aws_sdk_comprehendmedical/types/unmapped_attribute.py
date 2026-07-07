"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#UnmappedAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.attribute
    import aws_sdk_comprehendmedical.types.entity_type


class UnmappedAttribute(TypedDict, closed=True):
    type: NotRequired["aws_sdk_comprehendmedical.types.entity_type.EntityType"]
    r"""<p> The type of the unmapped attribute, could be one of the following values: \"MEDICATION\", \"MEDICAL_CONDITION\", \"ANATOMY\", \"TEST_AND_TREATMENT_PROCEDURE\" or \"PROTECTED_HEALTH_INFORMATION\". </p>"""
    attribute: NotRequired["aws_sdk_comprehendmedical.types.attribute.Attribute"]
    """<p> The specific attribute that has been extracted but not mapped to an entity. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnmappedAttribute) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_comprehendmedical.types.entity_type

        out["Type"] = (
            aws_sdk_comprehendmedical.types.entity_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "attribute" in value:
        import aws_sdk_comprehendmedical.types.attribute

        out["Attribute"] = (
            aws_sdk_comprehendmedical.types.attribute.serialize_aws_json_1_1(
                value["attribute"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnmappedAttribute:
    out: UnmappedAttribute = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_comprehendmedical.types.entity_type

        out["type"] = (
            aws_sdk_comprehendmedical.types.entity_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Attribute" in data:
        import aws_sdk_comprehendmedical.types.attribute

        out["attribute"] = (
            aws_sdk_comprehendmedical.types.attribute.deserialize_aws_json_1_1(
                data["Attribute"]
            )
        )
    return out
