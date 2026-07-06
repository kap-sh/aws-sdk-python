"""Generated from Smithy shape ``com.amazonaws.pi#CreatePerformanceAnalysisReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.identifier_string
    import aws_sdk_pi.types.iso_timestamp
    import aws_sdk_pi.types.service_type
    import aws_sdk_pi.types.tag_list


class CreatePerformanceAnalysisReportRequest(TypedDict, closed=True):
    service_type: "aws_sdk_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights will return metrics. Valid value is <code>RDS</code>.</p>"""
    identifier: "aws_sdk_pi.types.identifier_string.IdentifierString"
    """<p>An immutable, Amazon Web Services Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.</p> <p>To use an Amazon RDS instance as a data source, you specify its <code>DbiResourceId</code> value. For example, specify <code>db-ADECBTYHKTSAUMUZQYPDS2GW4A</code>.</p>"""
    start_time: "aws_sdk_pi.types.iso_timestamp.ISOTimestamp"
    """<p>The start time defined for the analysis report.</p>"""
    end_time: NotRequired["aws_sdk_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The end time defined for the analysis report.</p>"""
    tags: NotRequired["aws_sdk_pi.types.tag_list.TagList"]
    """<p>The metadata assigned to the analysis report consisting of a key-value pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePerformanceAnalysisReportRequest) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.service_type

    out["ServiceType"] = aws_sdk_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    import aws_sdk_pi.types.iso_timestamp

    out["StartTime"] = aws_sdk_pi.types.iso_timestamp.serialize_aws_json_1_1(
        value["start_time"]
    )
    if "end_time" in value:
        import aws_sdk_pi.types.iso_timestamp

        out["EndTime"] = aws_sdk_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "tags" in value:
        import aws_sdk_pi.types.tag_list

        out["Tags"] = aws_sdk_pi.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePerformanceAnalysisReportRequest:
    out: CreatePerformanceAnalysisReportRequest = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        import aws_sdk_pi.types.service_type

        out["service_type"] = aws_sdk_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError(
            "CreatePerformanceAnalysisReportRequest.service_type required"
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "CreatePerformanceAnalysisReportRequest.identifier required"
        )
    if "StartTime" in data:
        import aws_sdk_pi.types.iso_timestamp

        out["start_time"] = aws_sdk_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    else:
        raise DeserializationError(
            "CreatePerformanceAnalysisReportRequest.start_time required"
        )
    if "EndTime" in data:
        import aws_sdk_pi.types.iso_timestamp

        out["end_time"] = aws_sdk_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Tags" in data:
        import aws_sdk_pi.types.tag_list

        out["tags"] = aws_sdk_pi.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
