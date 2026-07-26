"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.criterion


class FindingCriteria(TypedDict, closed=True):
    criterion: NotRequired["capo_guardduty.types.criterion.Criterion"]
    """<p>Represents a map of finding properties that match specified conditions and values when querying findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingCriteria) -> dict:
    out: dict = {}
    if "criterion" in value:
        import capo_guardduty.types.criterion

        out["criterion"] = capo_guardduty.types.criterion.serialize_json(
            value["criterion"]
        )
    return out


def deserialize_json(data: dict) -> FindingCriteria:
    out: FindingCriteria = {}  # type: ignore[typeddict-item]
    if "criterion" in data:
        import capo_guardduty.types.criterion

        out["criterion"] = capo_guardduty.types.criterion.deserialize_json(
            data["criterion"]
        )
    return out
