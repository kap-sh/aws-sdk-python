"""Generated from Smithy shape ``com.amazonaws.guardduty#AnomalyUnusual``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.behavior


class AnomalyUnusual(TypedDict):
    behavior: NotRequired["aws_sdk_guardduty.types.behavior.Behavior"]
    """<p>The behavior of the anomalous activity that caused GuardDuty to generate the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyUnusual) -> dict:
    out: dict = {}
    if "behavior" in value:
        import aws_sdk_guardduty.types.behavior

        out["behavior"] = aws_sdk_guardduty.types.behavior.serialize_json(
            value["behavior"]
        )
    return out


def deserialize_json(data: dict) -> AnomalyUnusual:
    out: AnomalyUnusual = {}  # type: ignore[typeddict-item]
    if "behavior" in data:
        import aws_sdk_guardduty.types.behavior

        out["behavior"] = aws_sdk_guardduty.types.behavior.deserialize_json(
            data["behavior"]
        )
    return out
