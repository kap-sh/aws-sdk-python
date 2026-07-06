"""Generated from Smithy shape ``com.amazonaws.qbusiness#DateAttributeBoostingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.boosting_duration_in_seconds
    import aws_sdk_qbusiness.types.document_attribute_boosting_level


class DateAttributeBoostingConfiguration(TypedDict, closed=True):
    boosting_level: "aws_sdk_qbusiness.types.document_attribute_boosting_level.DocumentAttributeBoostingLevel"
    """<p>Specifies the priority tier ranking of boosting applied to document attributes. For version 2, this parameter indicates the relative ranking between boosted fields (ONE being highest priority, TWO being second highest, etc.) and determines the order in which attributes influence document ranking in search results. For version 1, this parameter specifies the boosting intensity. For version 2, boosting intensity (VERY HIGH, HIGH, MEDIUM, LOW, NONE) are not supported. Note that in version 2, you are not allowed to boost on only one field and make this value TWO.</p>"""
    boosting_duration_in_seconds: NotRequired[
        "aws_sdk_qbusiness.types.boosting_duration_in_seconds.BoostingDurationInSeconds"
    ]
    """<p>Specifies the duration, in seconds, of a boost applies to a <code>DATE</code> type document attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateAttributeBoostingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.document_attribute_boosting_level

    out["boostingLevel"] = (
        aws_sdk_qbusiness.types.document_attribute_boosting_level.serialize_json(
            value["boosting_level"]
        )
    )
    if "boosting_duration_in_seconds" in value:
        out["boostingDurationInSeconds"] = value["boosting_duration_in_seconds"]
    return out


def deserialize_json(data: dict) -> DateAttributeBoostingConfiguration:
    out: DateAttributeBoostingConfiguration = {}  # type: ignore[typeddict-item]
    if "boostingLevel" in data:
        import aws_sdk_qbusiness.types.document_attribute_boosting_level

        out["boosting_level"] = (
            aws_sdk_qbusiness.types.document_attribute_boosting_level.deserialize_json(
                data["boostingLevel"]
            )
        )
    else:
        raise DeserializationError(
            "DateAttributeBoostingConfiguration.boosting_level required"
        )
    if "boostingDurationInSeconds" in data:
        out["boosting_duration_in_seconds"] = data["boostingDurationInSeconds"]
    return out
