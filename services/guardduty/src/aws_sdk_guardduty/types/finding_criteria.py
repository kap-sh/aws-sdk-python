"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.criterion


class FindingCriteria(TypedDict):
    criterion: NotRequired["aws_sdk_guardduty.types.criterion.Criterion"]
    """<p>Represents a map of finding properties that match specified conditions and values when querying findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingCriteria) -> dict:
    out: dict = {}
    if "criterion" in value:
        import aws_sdk_guardduty.types.criterion

        out["criterion"] = aws_sdk_guardduty.types.criterion.serialize_json(
            value["criterion"]
        )
    return out


def deserialize_json(data: dict) -> FindingCriteria:
    out: FindingCriteria = {}  # type: ignore[typeddict-item]
    if "criterion" in data:
        import aws_sdk_guardduty.types.criterion

        out["criterion"] = aws_sdk_guardduty.types.criterion.deserialize_json(
            data["criterion"]
        )
    return out
