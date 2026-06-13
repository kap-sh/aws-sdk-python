"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateFindingsReportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.destination
    import aws_sdk_inspector2.types.filter_criteria
    import aws_sdk_inspector2.types.report_format


class CreateFindingsReportRequest(TypedDict):
    filter_criteria: NotRequired[
        "aws_sdk_inspector2.types.filter_criteria.FilterCriteria"
    ]
    """<p>The filter criteria to apply to the results of the finding report.</p>"""
    report_format: "aws_sdk_inspector2.types.report_format.ReportFormat"
    """<p>The format to generate the report in.</p>"""
    s3_destination: "aws_sdk_inspector2.types.destination.Destination"
    """<p>The Amazon S3 export destination for the report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFindingsReportRequest) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import aws_sdk_inspector2.types.filter_criteria

        out["filterCriteria"] = aws_sdk_inspector2.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    out["reportFormat"] = value["report_format"]
    import aws_sdk_inspector2.types.destination

    out["s3Destination"] = aws_sdk_inspector2.types.destination.serialize_json(
        value["s3_destination"]
    )
    return out


def deserialize_json(data: dict) -> CreateFindingsReportRequest:
    out: CreateFindingsReportRequest = {}  # type: ignore[typeddict-item]
    if "filterCriteria" in data:
        import aws_sdk_inspector2.types.filter_criteria

        out["filter_criteria"] = (
            aws_sdk_inspector2.types.filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if "reportFormat" in data:
        out["report_format"] = data["reportFormat"]
    else:
        raise DeserializationError("CreateFindingsReportRequest.report_format required")
    if "s3Destination" in data:
        import aws_sdk_inspector2.types.destination

        out["s3_destination"] = aws_sdk_inspector2.types.destination.deserialize_json(
            data["s3Destination"]
        )
    else:
        raise DeserializationError(
            "CreateFindingsReportRequest.s3_destination required"
        )
    return out
