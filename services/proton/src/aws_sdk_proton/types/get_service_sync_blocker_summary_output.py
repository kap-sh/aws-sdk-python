"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceSyncBlockerSummaryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_sync_blocker_summary


class GetServiceSyncBlockerSummaryOutput(TypedDict):
    service_sync_blocker_summary: NotRequired[
        "aws_sdk_proton.types.service_sync_blocker_summary.ServiceSyncBlockerSummary"
    ]
    """<p>The detailed data of the requested service sync blocker summary.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceSyncBlockerSummaryOutput) -> dict:
    out: dict = {}
    if "service_sync_blocker_summary" in value:
        import aws_sdk_proton.types.service_sync_blocker_summary

        out["serviceSyncBlockerSummary"] = (
            aws_sdk_proton.types.service_sync_blocker_summary.serialize_aws_json_1_0(
                value["service_sync_blocker_summary"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceSyncBlockerSummaryOutput:
    out: GetServiceSyncBlockerSummaryOutput = {}  # type: ignore[typeddict-item]
    if "serviceSyncBlockerSummary" in data:
        import aws_sdk_proton.types.service_sync_blocker_summary

        out["service_sync_blocker_summary"] = (
            aws_sdk_proton.types.service_sync_blocker_summary.deserialize_aws_json_1_0(
                data["serviceSyncBlockerSummary"]
            )
        )
    return out
