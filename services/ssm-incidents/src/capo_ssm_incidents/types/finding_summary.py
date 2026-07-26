"""Generated from Smithy shape ``com.amazonaws.ssmincidents#FindingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.finding_id


class FindingSummary(TypedDict, closed=True):
    id: "capo_ssm_incidents.types.finding_id.FindingId"
    """<p>The ID of the finding.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp for when the finding was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_ssm_incidents.types._prelude.timestamp

    out["lastModifiedTime"] = (
        capo_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> FindingSummary:
    out: FindingSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FindingSummary.id required")
    if "lastModifiedTime" in data:
        import capo_ssm_incidents.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("FindingSummary.last_modified_time required")
    return out
