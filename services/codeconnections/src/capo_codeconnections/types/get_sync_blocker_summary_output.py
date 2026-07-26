"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetSyncBlockerSummaryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeconnections.types.sync_blocker_summary


class GetSyncBlockerSummaryOutput(TypedDict, closed=True):
    sync_blocker_summary: (
        "capo_codeconnections.types.sync_blocker_summary.SyncBlockerSummary"
    )
    """<p>The list of sync blockers for a specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSyncBlockerSummaryOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.sync_blocker_summary

    out["SyncBlockerSummary"] = (
        capo_codeconnections.types.sync_blocker_summary.serialize_aws_json_1_0(
            value["sync_blocker_summary"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSyncBlockerSummaryOutput:
    out: GetSyncBlockerSummaryOutput = {}  # type: ignore[typeddict-item]
    if "SyncBlockerSummary" in data:
        import capo_codeconnections.types.sync_blocker_summary

        out["sync_blocker_summary"] = (
            capo_codeconnections.types.sync_blocker_summary.deserialize_aws_json_1_0(
                data["SyncBlockerSummary"]
            )
        )
    else:
        raise DeserializationError(
            "GetSyncBlockerSummaryOutput.sync_blocker_summary required"
        )
    return out
