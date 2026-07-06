"""Generated from Smithy shape ``com.amazonaws.qbusiness#StringAttributeBoostingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_attribute_boosting_level
    import aws_sdk_qbusiness.types.string_attribute_value_boosting


class StringAttributeBoostingConfiguration(TypedDict, closed=True):
    boosting_level: "aws_sdk_qbusiness.types.document_attribute_boosting_level.DocumentAttributeBoostingLevel"
    """<p>Specifies the priority tier ranking of boosting applied to document attributes. For version 2, this parameter indicates the relative ranking between boosted fields (ONE being highest priority, TWO being second highest, etc.) and determines the order in which attributes influence document ranking in search results. For version 1, this parameter specifies the boosting intensity. For version 2, boosting intensity (VERY HIGH, HIGH, MEDIUM, LOW, NONE) are not supported. Note that in version 2, you are not allowed to boost on only one field and make this value TWO.</p>"""
    attribute_value_boosting: NotRequired[
        "aws_sdk_qbusiness.types.string_attribute_value_boosting.StringAttributeValueBoosting"
    ]
    """<p>Specifies specific values of a <code>STRING</code> type document attribute being boosted. When using <code>NativeIndexConfiguration</code> version 2, you can specify up to five values in order of priority.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringAttributeBoostingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.document_attribute_boosting_level

    out["boostingLevel"] = (
        aws_sdk_qbusiness.types.document_attribute_boosting_level.serialize_json(
            value["boosting_level"]
        )
    )
    if "attribute_value_boosting" in value:
        import aws_sdk_qbusiness.types.string_attribute_value_boosting

        out["attributeValueBoosting"] = (
            aws_sdk_qbusiness.types.string_attribute_value_boosting.serialize_json(
                value["attribute_value_boosting"]
            )
        )
    return out


def deserialize_json(data: dict) -> StringAttributeBoostingConfiguration:
    out: StringAttributeBoostingConfiguration = {}  # type: ignore[typeddict-item]
    if "boostingLevel" in data:
        import aws_sdk_qbusiness.types.document_attribute_boosting_level

        out["boosting_level"] = (
            aws_sdk_qbusiness.types.document_attribute_boosting_level.deserialize_json(
                data["boostingLevel"]
            )
        )
    else:
        raise DeserializationError(
            "StringAttributeBoostingConfiguration.boosting_level required"
        )
    if "attributeValueBoosting" in data:
        import aws_sdk_qbusiness.types.string_attribute_value_boosting

        out["attribute_value_boosting"] = (
            aws_sdk_qbusiness.types.string_attribute_value_boosting.deserialize_json(
                data["attributeValueBoosting"]
            )
        )
    return out
