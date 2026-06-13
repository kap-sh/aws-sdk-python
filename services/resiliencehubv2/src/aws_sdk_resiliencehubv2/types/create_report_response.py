"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateReportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.report_generation_result


class CreateReportResponse(TypedDict):
    report_generation_result: (
        "aws_sdk_resiliencehubv2.types.report_generation_result.ReportGenerationResult"
    )
    """<p>The result of the report generation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReportResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.report_generation_result

    out["reportGenerationResult"] = (
        aws_sdk_resiliencehubv2.types.report_generation_result.serialize_json(
            value["report_generation_result"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateReportResponse:
    out: CreateReportResponse = {}  # type: ignore[typeddict-item]
    if "reportGenerationResult" in data:
        import aws_sdk_resiliencehubv2.types.report_generation_result

        out["report_generation_result"] = (
            aws_sdk_resiliencehubv2.types.report_generation_result.deserialize_json(
                data["reportGenerationResult"]
            )
        )
    else:
        raise DeserializationError(
            "CreateReportResponse.report_generation_result required"
        )
    return out
