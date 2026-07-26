"""Generated from Smithy shape ``com.amazonaws.wafv2#MobileSdkRelease``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.release_notes
    import capo_wafv2.types.tag_list
    import capo_wafv2.types.timestamp
    import capo_wafv2.types.version_key_string


class MobileSdkRelease(TypedDict, closed=True):
    release_version: NotRequired["capo_wafv2.types.version_key_string.VersionKeyString"]
    """<p>The release version. </p>"""
    timestamp: NotRequired["capo_wafv2.types.timestamp.Timestamp"]
    """<p>The timestamp of the release. </p>"""
    release_notes: NotRequired["capo_wafv2.types.release_notes.ReleaseNotes"]
    """<p>Notes describing the release.</p>"""
    tags: NotRequired["capo_wafv2.types.tag_list.TagList"]
    """<p>Tags that are associated with the release. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MobileSdkRelease) -> dict:
    out: dict = {}
    if "release_version" in value:
        out["ReleaseVersion"] = value["release_version"]
    if "timestamp" in value:
        import capo_wafv2.types.timestamp

        out["Timestamp"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    if "release_notes" in value:
        out["ReleaseNotes"] = value["release_notes"]
    if "tags" in value:
        import capo_wafv2.types.tag_list

        out["Tags"] = capo_wafv2.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> MobileSdkRelease:
    out: MobileSdkRelease = {}  # type: ignore[typeddict-item]
    if "ReleaseVersion" in data:
        out["release_version"] = data["ReleaseVersion"]
    if "Timestamp" in data:
        import capo_wafv2.types.timestamp

        out["timestamp"] = capo_wafv2.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    if "ReleaseNotes" in data:
        out["release_notes"] = data["ReleaseNotes"]
    if "Tags" in data:
        import capo_wafv2.types.tag_list

        out["tags"] = capo_wafv2.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
