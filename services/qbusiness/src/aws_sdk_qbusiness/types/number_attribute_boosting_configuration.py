"""Generated from Smithy shape ``com.amazonaws.qbusiness#NumberAttributeBoostingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_attribute_boosting_level
    import aws_sdk_qbusiness.types.number_attribute_boosting_type


class NumberAttributeBoostingConfiguration(TypedDict):
    boosting_level: "aws_sdk_qbusiness.types.document_attribute_boosting_level.DocumentAttributeBoostingLevel"
    """<p>Specifies the priority of boosted document attributes in relation to other boosted attributes. This parameter determines how strongly the attribute influences document ranking in search results. <code>NUMBER</code> attributes can serve as additional boosting factors when needed, but are not supported when using <code>NativeIndexConfiguration</code> version 2.</p>"""
    boosting_type: NotRequired[
        "aws_sdk_qbusiness.types.number_attribute_boosting_type.NumberAttributeBoostingType"
    ]
    """<p>Specifies whether higher or lower numeric values should be prioritized when boosting. Valid values are ASCENDING (higher numbers are more important) and DESCENDING (lower numbers are more important).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberAttributeBoostingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.document_attribute_boosting_level

    out["boostingLevel"] = (
        aws_sdk_qbusiness.types.document_attribute_boosting_level.serialize_json(
            value["boosting_level"]
        )
    )
    if "boosting_type" in value:
        import aws_sdk_qbusiness.types.number_attribute_boosting_type

        out["boostingType"] = (
            aws_sdk_qbusiness.types.number_attribute_boosting_type.serialize_json(
                value["boosting_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> NumberAttributeBoostingConfiguration:
    out: NumberAttributeBoostingConfiguration = {}  # type: ignore[typeddict-item]
    if "boostingLevel" in data:
        import aws_sdk_qbusiness.types.document_attribute_boosting_level

        out["boosting_level"] = (
            aws_sdk_qbusiness.types.document_attribute_boosting_level.deserialize_json(
                data["boostingLevel"]
            )
        )
    else:
        raise DeserializationError(
            "NumberAttributeBoostingConfiguration.boosting_level required"
        )
    if "boostingType" in data:
        import aws_sdk_qbusiness.types.number_attribute_boosting_type

        out["boosting_type"] = (
            aws_sdk_qbusiness.types.number_attribute_boosting_type.deserialize_json(
                data["boostingType"]
            )
        )
    return out
