"""Generated from Smithy shape ``com.amazonaws.qapps#Submission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.q_apps_timestamp
    import capo_qapps.types.uuid


class Submission(TypedDict, closed=True):
    value: NotRequired["object"]
    """<p>The data submitted by the user.</p>"""
    submission_id: NotRequired["capo_qapps.types.uuid.UUID"]
    """<p>The unique identifier of the submission.</p>"""
    timestamp: NotRequired["capo_qapps.types.q_apps_timestamp.QAppsTimestamp"]
    """<p>The date and time when the card is submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Submission) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "submission_id" in value:
        out["submissionId"] = value["submission_id"]
    if "timestamp" in value:
        import capo_qapps.types.q_apps_timestamp

        out["timestamp"] = capo_qapps.types.q_apps_timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> Submission:
    out: Submission = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "submissionId" in data:
        out["submission_id"] = data["submissionId"]
    if "timestamp" in data:
        import capo_qapps.types.q_apps_timestamp

        out["timestamp"] = capo_qapps.types.q_apps_timestamp.deserialize_json(
            data["timestamp"]
        )
    return out
