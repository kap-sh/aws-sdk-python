"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ServerlessTrack``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.track_name
    import capo_redshift_serverless.types.update_targets_list


class ServerlessTrack(TypedDict, closed=True):
    track_name: NotRequired["capo_redshift_serverless.types.track_name.TrackName"]
    """<p>The name of the track. Valid values are <code>current</code> and <code>trailing</code>.</p>"""
    workgroup_version: NotRequired["str"]
    """<p>The workgroup version number for the workgroup release.</p>"""
    update_targets: NotRequired[
        "capo_redshift_serverless.types.update_targets_list.UpdateTargetsList"
    ]
    """<p>An array of <code>UpdateTarget</code> objects to update with the track.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerlessTrack) -> dict:
    out: dict = {}
    if "track_name" in value:
        out["trackName"] = value["track_name"]
    if "workgroup_version" in value:
        out["workgroupVersion"] = value["workgroup_version"]
    if "update_targets" in value:
        import capo_redshift_serverless.types.update_targets_list

        out["updateTargets"] = (
            capo_redshift_serverless.types.update_targets_list.serialize_aws_json_1_1(
                value["update_targets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServerlessTrack:
    out: ServerlessTrack = {}  # type: ignore[typeddict-item]
    if "trackName" in data:
        out["track_name"] = data["trackName"]
    if "workgroupVersion" in data:
        out["workgroup_version"] = data["workgroupVersion"]
    if "updateTargets" in data:
        import capo_redshift_serverless.types.update_targets_list

        out["update_targets"] = (
            capo_redshift_serverless.types.update_targets_list.deserialize_aws_json_1_1(
                data["updateTargets"]
            )
        )
    return out
