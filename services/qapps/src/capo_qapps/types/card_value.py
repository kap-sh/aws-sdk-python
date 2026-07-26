"""Generated from Smithy shape ``com.amazonaws.qapps#CardValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.submission_mutation
    import capo_qapps.types.uuid


class CardValue(TypedDict, closed=True):
    card_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the card.</p>"""
    value: "str"
    """<p>The value or result associated with the card.</p>"""
    submission_mutation: NotRequired[
        "capo_qapps.types.submission_mutation.SubmissionMutation"
    ]
    """<p>The structure that describes how the current form card value is mutated. Only applies for form cards when multiple responses are allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CardValue) -> dict:
    out: dict = {}
    out["cardId"] = value["card_id"]
    out["value"] = value["value"]
    if "submission_mutation" in value:
        import capo_qapps.types.submission_mutation

        out["submissionMutation"] = capo_qapps.types.submission_mutation.serialize_json(
            value["submission_mutation"]
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
        import capo_qapps.types.submission_mutation

        out["submission_mutation"] = (
            capo_qapps.types.submission_mutation.deserialize_json(
                data["submissionMutation"]
            )
        )
    return out
