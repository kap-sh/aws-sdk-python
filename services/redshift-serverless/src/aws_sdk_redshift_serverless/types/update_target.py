"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.track_name


class UpdateTarget(TypedDict):
    track_name: NotRequired["aws_sdk_redshift_serverless.types.track_name.TrackName"]
    """<p>The name of the new track.</p>"""
    workgroup_version: NotRequired["str"]
    """<p>The workgroup version for the new track.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTarget) -> dict:
    out: dict = {}
    if "track_name" in value:
        out["trackName"] = value["track_name"]
    if "workgroup_version" in value:
        out["workgroupVersion"] = value["workgroup_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTarget:
    out: UpdateTarget = {}  # type: ignore[typeddict-item]
    if "trackName" in data:
        out["track_name"] = data["trackName"]
    if "workgroupVersion" in data:
        out["workgroup_version"] = data["workgroupVersion"]
    return out
