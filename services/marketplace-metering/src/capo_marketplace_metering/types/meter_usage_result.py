"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#MeterUsageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_metering.types.string


class MeterUsageResult(TypedDict, closed=True):
    metering_record_id: NotRequired["capo_marketplace_metering.types.string.String"]
    """<p>Metering record id.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MeterUsageResult) -> dict:
    out: dict = {}
    if "metering_record_id" in value:
        out["MeteringRecordId"] = value["metering_record_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MeterUsageResult:
    out: MeterUsageResult = {}  # type: ignore[typeddict-item]
    if "MeteringRecordId" in data:
        out["metering_record_id"] = data["MeteringRecordId"]
    return out
