"""Generated from Smithy shape ``com.amazonaws.macie2#FindingCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.criterion


class FindingCriteria(TypedDict, closed=True):
    criterion: NotRequired["capo_macie2.types.criterion.Criterion"]
    """<p>A condition that specifies the property, operator, and one or more values to use to filter the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingCriteria) -> dict:
    out: dict = {}
    if "criterion" in value:
        import capo_macie2.types.criterion

        out["criterion"] = capo_macie2.types.criterion.serialize_json(
            value["criterion"]
        )
    return out


def deserialize_json(data: dict) -> FindingCriteria:
    out: FindingCriteria = {}  # type: ignore[typeddict-item]
    if "criterion" in data:
        import capo_macie2.types.criterion

        out["criterion"] = capo_macie2.types.criterion.deserialize_json(
            data["criterion"]
        )
    return out
