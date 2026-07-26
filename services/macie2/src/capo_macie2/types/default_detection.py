"""Generated from Smithy shape ``com.amazonaws.macie2#DefaultDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__long
    import capo_macie2.types.__string
    import capo_macie2.types.occurrences


class DefaultDetection(TypedDict, closed=True):
    count: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of occurrences of the type of sensitive data that was detected.</p>"""
    occurrences: NotRequired["capo_macie2.types.occurrences.Occurrences"]
    """<p>The location of 1-15 occurrences of the sensitive data that was detected. A finding includes location data for a maximum of 15 occurrences of sensitive data.</p>"""
    type: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The type of sensitive data that was detected. For example, AWS_CREDENTIALS, PHONE_NUMBER, or ADDRESS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultDetection) -> dict:
    out: dict = {}
    if "count" in value:
        out["count"] = value["count"]
    if "occurrences" in value:
        import capo_macie2.types.occurrences

        out["occurrences"] = capo_macie2.types.occurrences.serialize_json(
            value["occurrences"]
        )
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> DefaultDetection:
    out: DefaultDetection = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    if "occurrences" in data:
        import capo_macie2.types.occurrences

        out["occurrences"] = capo_macie2.types.occurrences.deserialize_json(
            data["occurrences"]
        )
    if "type" in data:
        out["type"] = data["type"]
    return out
