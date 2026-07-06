"""Generated from Smithy shape ``com.amazonaws.guardduty#Detection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.anomaly
    import aws_sdk_guardduty.types.sequence


class Detection(TypedDict, closed=True):
    anomaly: NotRequired["aws_sdk_guardduty.types.anomaly.Anomaly"]
    """<p>The details about the anomalous activity that caused GuardDuty to generate the finding.</p>"""
    sequence: NotRequired["aws_sdk_guardduty.types.sequence.Sequence"]
    """<p>The details about the attack sequence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Detection) -> dict:
    out: dict = {}
    if "anomaly" in value:
        import aws_sdk_guardduty.types.anomaly

        out["anomaly"] = aws_sdk_guardduty.types.anomaly.serialize_json(
            value["anomaly"]
        )
    if "sequence" in value:
        import aws_sdk_guardduty.types.sequence

        out["sequence"] = aws_sdk_guardduty.types.sequence.serialize_json(
            value["sequence"]
        )
    return out


def deserialize_json(data: dict) -> Detection:
    out: Detection = {}  # type: ignore[typeddict-item]
    if "anomaly" in data:
        import aws_sdk_guardduty.types.anomaly

        out["anomaly"] = aws_sdk_guardduty.types.anomaly.deserialize_json(
            data["anomaly"]
        )
    if "sequence" in data:
        import aws_sdk_guardduty.types.sequence

        out["sequence"] = aws_sdk_guardduty.types.sequence.deserialize_json(
            data["sequence"]
        )
    return out
