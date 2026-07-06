"""Generated from Smithy shape ``com.amazonaws.guardduty#Anomaly``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.anomaly_profiles
    import aws_sdk_guardduty.types.anomaly_unusual


class Anomaly(TypedDict, closed=True):
    profiles: NotRequired["aws_sdk_guardduty.types.anomaly_profiles.AnomalyProfiles"]
    """<p>Information about the types of profiles.</p>"""
    unusual: NotRequired["aws_sdk_guardduty.types.anomaly_unusual.AnomalyUnusual"]
    """<p>Information about the behavior of the anomalies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Anomaly) -> dict:
    out: dict = {}
    if "profiles" in value:
        import aws_sdk_guardduty.types.anomaly_profiles

        out["profiles"] = aws_sdk_guardduty.types.anomaly_profiles.serialize_json(
            value["profiles"]
        )
    if "unusual" in value:
        import aws_sdk_guardduty.types.anomaly_unusual

        out["unusual"] = aws_sdk_guardduty.types.anomaly_unusual.serialize_json(
            value["unusual"]
        )
    return out


def deserialize_json(data: dict) -> Anomaly:
    out: Anomaly = {}  # type: ignore[typeddict-item]
    if "profiles" in data:
        import aws_sdk_guardduty.types.anomaly_profiles

        out["profiles"] = aws_sdk_guardduty.types.anomaly_profiles.deserialize_json(
            data["profiles"]
        )
    if "unusual" in data:
        import aws_sdk_guardduty.types.anomaly_unusual

        out["unusual"] = aws_sdk_guardduty.types.anomaly_unusual.deserialize_json(
            data["unusual"]
        )
    return out
