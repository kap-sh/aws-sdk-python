"""Generated from Smithy shape ``com.amazonaws.odb#DbServerPatchingDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_server_patching_status


class DbServerPatchingDetails(TypedDict):
    estimated_patch_duration: NotRequired["int"]
    """<p>Estimated time, in minutes, to patch one database server.</p>"""
    patching_status: NotRequired[
        "aws_sdk_odb.types.db_server_patching_status.DbServerPatchingStatus"
    ]
    """<p>The status of the patching operation. Possible values are <code>SCHEDULED</code>, <code>MAINTENANCE_IN_PROGRESS</code>, <code>FAILED</code>, and <code>COMPLETE</code>.</p>"""
    time_patching_ended: NotRequired["str"]
    """<p>The time when the patching operation ended.</p>"""
    time_patching_started: NotRequired["str"]
    """<p>The time when the patching operation started.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbServerPatchingDetails) -> dict:
    out: dict = {}
    if "estimated_patch_duration" in value:
        out["estimatedPatchDuration"] = value["estimated_patch_duration"]
    if "patching_status" in value:
        import aws_sdk_odb.types.db_server_patching_status

        out["patchingStatus"] = (
            aws_sdk_odb.types.db_server_patching_status.serialize_aws_json_1_0(
                value["patching_status"]
            )
        )
    if "time_patching_ended" in value:
        out["timePatchingEnded"] = value["time_patching_ended"]
    if "time_patching_started" in value:
        out["timePatchingStarted"] = value["time_patching_started"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DbServerPatchingDetails:
    out: DbServerPatchingDetails = {}  # type: ignore[typeddict-item]
    if "estimatedPatchDuration" in data:
        out["estimated_patch_duration"] = data["estimatedPatchDuration"]
    if "patchingStatus" in data:
        import aws_sdk_odb.types.db_server_patching_status

        out["patching_status"] = (
            aws_sdk_odb.types.db_server_patching_status.deserialize_aws_json_1_0(
                data["patchingStatus"]
            )
        )
    if "timePatchingEnded" in data:
        out["time_patching_ended"] = data["timePatchingEnded"]
    if "timePatchingStarted" in data:
        out["time_patching_started"] = data["timePatchingStarted"]
    return out
