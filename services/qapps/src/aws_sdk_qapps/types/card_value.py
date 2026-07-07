"""Generated from Smithy shape ``com.amazonaws.qapps#CardValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.submission_mutation
    import aws_sdk_qapps.types.uuid


class CardValue(TypedDict, closed=True):
    card_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the card.</p>"""
    value: "str"
    """<p>The value or result associated with the card.</p>"""
    submission_mutation: NotRequired[
        "aws_sdk_qapps.types.submission_mutation.SubmissionMutation"
    ]
    """<p>The structure that describes how the current form card value is mutated. Only applies for form cards when multiple responses are allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CardValue) -> dict:
    out: dict = {}
    out["cardId"] = value["card_id"]
    out["value"] = value["value"]
    if "submission_mutation" in value:
        import aws_sdk_qapps.types.submission_mutation

        out["submissionMutation"] = (
            aws_sdk_qapps.types.submission_mutation.serialize_json(
                value["submission_mutation"]
            )
        )
    return out


def deserialize_json(data: dict) -> CardValue:
    out: CardValue = {}  # type: ignore[typeddict-item]
    if "cardId" in data:
        out["card_id"] = data["cardId"]
    else:
        raise DeserializationError("CardValue.card_id required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("CardValue.value required")
    if "submissionMutation" in data:
        import aws_sdk_qapps.types.submission_mutation

        out["submission_mutation"] = (
            aws_sdk_qapps.types.submission_mutation.deserialize_json(
                data["submissionMutation"]
            )
        )
    return out
