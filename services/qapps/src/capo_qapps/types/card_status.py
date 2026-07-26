"""Generated from Smithy shape ``com.amazonaws.qapps#CardStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.execution_status
    import capo_qapps.types.submission_list


class CardStatus(TypedDict, closed=True):
    current_state: "capo_qapps.types.execution_status.ExecutionStatus"
    """<p>The current state of the card.</p>"""
    current_value: "str"
    """<p>The current value or result associated with the card.</p>"""
    submissions: NotRequired["capo_qapps.types.submission_list.SubmissionList"]
    """<p>A list of previous submissions, if the card is a form card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CardStatus) -> dict:
    out: dict = {}
    import capo_qapps.types.execution_status

    out["currentState"] = capo_qapps.types.execution_status.serialize_json(
        value["current_state"]
    )
    out["currentValue"] = value["current_value"]
    if "submissions" in value:
        import capo_qapps.types.submission_list

        out["submissions"] = capo_qapps.types.submission_list.serialize_json(
            value["submissions"]
        )
    return out


def deserialize_json(data: dict) -> CardStatus:
    out: CardStatus = {}  # type: ignore[typeddict-item]
    if "currentState" in data:
        import capo_qapps.types.execution_status

        out["current_state"] = capo_qapps.types.execution_status.deserialize_json(
            data["currentState"]
        )
    else:
        raise DeserializationError("CardStatus.current_state required")
    if "currentValue" in data:
        out["current_value"] = data["currentValue"]
    else:
        raise DeserializationError("CardStatus.current_value required")
    if "submissions" in data:
        import capo_qapps.types.submission_list

        out["submissions"] = capo_qapps.types.submission_list.deserialize_json(
            data["submissions"]
        )
    return out
