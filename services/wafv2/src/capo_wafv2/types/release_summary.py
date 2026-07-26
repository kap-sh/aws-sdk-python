"""Generated from Smithy shape ``com.amazonaws.wafv2#ReleaseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.timestamp
    import capo_wafv2.types.version_key_string


class ReleaseSummary(TypedDict, closed=True):
    release_version: NotRequired["capo_wafv2.types.version_key_string.VersionKeyString"]
    """<p>The release version. </p>"""
    timestamp: NotRequired["capo_wafv2.types.timestamp.Timestamp"]
    """<p>The timestamp of the release. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseSummary) -> dict:
    out: dict = {}
    if "release_version" in value:
        out["ReleaseVersion"] = value["release_version"]
    if "timestamp" in value:
        import capo_wafv2.types.timestamp

        out["Timestamp"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReleaseSummary:
    out: ReleaseSummary = {}  # type: ignore[typeddict-item]
    if "ReleaseVersion" in data:
        out["release_version"] = data["ReleaseVersion"]
    if "Timestamp" in data:
        import capo_wafv2.types.timestamp

        out["timestamp"] = capo_wafv2.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    return out
