"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobRefreshScheduleOverrideParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.string
    import capo_quicksight.types.timestamp


class AssetBundleImportJobRefreshScheduleOverrideParameters(TypedDict, closed=True):
    data_set_id: "capo_quicksight.types.resource_id.ResourceId"
    """<p>A partial identifier for the specific <code>RefreshSchedule</code> resource that is being overridden. This structure is used together with the <code>ScheduleID</code> structure.</p>"""
    schedule_id: "capo_quicksight.types.string.String"
    """<p>A partial identifier for the specific <code>RefreshSchedule</code> resource being overridden. This structure is used together with the <code>DataSetId</code> structure.</p>"""
    start_after_date_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>An override for the <code>StartAfterDateTime</code> of a <code>RefreshSchedule</code>. Make sure that the <code>StartAfterDateTime</code> is set to a time that takes place in the future.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleImportJobRefreshScheduleOverrideParameters,
) -> dict:
    out: dict = {}
    out["DataSetId"] = value["data_set_id"]
    out["ScheduleId"] = value["schedule_id"]
    if "start_after_date_time" in value:
        import capo_quicksight.types.timestamp

        out["StartAfterDateTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["start_after_date_time"]
        )
    return out


def deserialize_json(
    data: dict,
) -> AssetBundleImportJobRefreshScheduleOverrideParameters:
    out: AssetBundleImportJobRefreshScheduleOverrideParameters = {}  # type: ignore[typeddict-item]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "AssetBundleImportJobRefreshScheduleOverrideParameters.data_set_id required"
        )
    if "ScheduleId" in data:
        out["schedule_id"] = data["ScheduleId"]
    else:
        raise DeserializationError(
            "AssetBundleImportJobRefreshScheduleOverrideParameters.schedule_id required"
        )
    if "StartAfterDateTime" in data:
        import capo_quicksight.types.timestamp

        out["start_after_date_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["StartAfterDateTime"]
        )
    return out
