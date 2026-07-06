"""Generated from Smithy shape ``com.amazonaws.servicequotas#StartQuotaUtilizationReportRequest``."""

from typing_extensions import TypedDict


class StartQuotaUtilizationReportRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartQuotaUtilizationReportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StartQuotaUtilizationReportRequest:
    out: StartQuotaUtilizationReportRequest = {}  # type: ignore[typeddict-item]
    return out
