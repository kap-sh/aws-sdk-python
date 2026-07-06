"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.client_token
    import aws_sdk_resiliencehubv2.types.report_type


class CreateReportRequest(TypedDict, closed=True):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    report_type: "aws_sdk_resiliencehubv2.types.report_type.ReportType"
    """<p>The type of report to generate.</p>"""
    client_token: NotRequired["aws_sdk_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateReportRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    import aws_sdk_resiliencehubv2.types.report_type

    out["reportType"] = aws_sdk_resiliencehubv2.types.report_type.serialize_json(
        value["report_type"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateReportRequest:
    out: CreateReportRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("CreateReportRequest.service_arn required")
    if "reportType" in data:
        import aws_sdk_resiliencehubv2.types.report_type

        out["report_type"] = aws_sdk_resiliencehubv2.types.report_type.deserialize_json(
            data["reportType"]
        )
    else:
        raise DeserializationError("CreateReportRequest.report_type required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
