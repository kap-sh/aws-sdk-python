"""Generated from Smithy shape ``com.amazonaws.guardduty#FlowLogsConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.data_source_status


class FlowLogsConfigurationResult(TypedDict, closed=True):
    status: NotRequired["capo_guardduty.types.data_source_status.DataSourceStatus"]
    """<p>Denotes whether VPC flow logs is enabled as a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowLogsConfigurationResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_guardduty.types.data_source_status

        out["status"] = capo_guardduty.types.data_source_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> FlowLogsConfigurationResult:
    out: FlowLogsConfigurationResult = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_guardduty.types.data_source_status

        out["status"] = capo_guardduty.types.data_source_status.deserialize_json(
            data["status"]
        )
    return out
