"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ReportStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.last_delivery
    import capo_cost_and_usage_report_service.types.last_status


class ReportStatus(TypedDict, closed=True):
    last_delivery: NotRequired[
        "capo_cost_and_usage_report_service.types.last_delivery.LastDelivery"
    ]
    """<p>A timestamp that gives the date of a report delivery.</p>"""
    last_status: NotRequired[
        "capo_cost_and_usage_report_service.types.last_status.LastStatus"
    ]
    """<p>An enum that gives the status of a report delivery.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportStatus) -> dict:
    out: dict = {}
    if "last_delivery" in value:
        out["lastDelivery"] = value["last_delivery"]
    if "last_status" in value:
        import capo_cost_and_usage_report_service.types.last_status

        out["lastStatus"] = (
            capo_cost_and_usage_report_service.types.last_status.serialize_aws_json_1_1(
                value["last_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportStatus:
    out: ReportStatus = {}  # type: ignore[typeddict-item]
    if "lastDelivery" in data:
        out["last_delivery"] = data["lastDelivery"]
    if "lastStatus" in data:
        import capo_cost_and_usage_report_service.types.last_status

        out["last_status"] = (
            capo_cost_and_usage_report_service.types.last_status.deserialize_aws_json_1_1(
                data["lastStatus"]
            )
        )
    return out
