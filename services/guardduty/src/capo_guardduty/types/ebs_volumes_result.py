"""Generated from Smithy shape ``com.amazonaws.guardduty#EbsVolumesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.data_source_status
    import capo_guardduty.types.string


class EbsVolumesResult(TypedDict, closed=True):
    status: NotRequired["capo_guardduty.types.data_source_status.DataSourceStatus"]
    """<p>Describes whether scanning EBS volumes is enabled as a data source.</p>"""
    reason: NotRequired["capo_guardduty.types.string.String"]
    """<p>Specifies the reason why scanning EBS volumes (Malware Protection) was not enabled as a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsVolumesResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_guardduty.types.data_source_status

        out["status"] = capo_guardduty.types.data_source_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> EbsVolumesResult:
    out: EbsVolumesResult = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_guardduty.types.data_source_status

        out["status"] = capo_guardduty.types.data_source_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
