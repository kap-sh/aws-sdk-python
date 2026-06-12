"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeEventsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.configuration_template_name
    import aws_sdk_elastic_beanstalk.types.environment_id
    import aws_sdk_elastic_beanstalk.types.environment_name
    import aws_sdk_elastic_beanstalk.types.event_severity
    import aws_sdk_elastic_beanstalk.types.max_records
    import aws_sdk_elastic_beanstalk.types.platform_arn
    import aws_sdk_elastic_beanstalk.types.request_id
    import aws_sdk_elastic_beanstalk.types.time_filter_end
    import aws_sdk_elastic_beanstalk.types.time_filter_start
    import aws_sdk_elastic_beanstalk.types.token
    import aws_sdk_elastic_beanstalk.types.version_label


class DescribeEventsMessage(TypedDict):
    application_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those associated with this application.</p>"""
    version_label: NotRequired[
        "aws_sdk_elastic_beanstalk.types.version_label.VersionLabel"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this application version.</p>"""
    template_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that are associated with this environment configuration.</p>"""
    environment_id: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.</p>"""
    environment_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.</p>"""
    platform_arn: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_arn.PlatformArn"
    ]
    """<p>The ARN of a custom platform version. If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this custom platform version.</p>"""
    request_id: NotRequired["aws_sdk_elastic_beanstalk.types.request_id.RequestId"]
    """<p>If specified, AWS Elastic Beanstalk restricts the described events to include only those associated with this request ID.</p>"""
    severity: NotRequired[
        "aws_sdk_elastic_beanstalk.types.event_severity.EventSeverity"
    ]
    """<p>If specified, limits the events returned from this call to include only those with the specified severity or higher.</p>"""
    start_time: NotRequired[
        "aws_sdk_elastic_beanstalk.types.time_filter_start.TimeFilterStart"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur on or after this time.</p>"""
    end_time: NotRequired[
        "aws_sdk_elastic_beanstalk.types.time_filter_end.TimeFilterEnd"
    ]
    """<p> If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur up to, but not including, the <code>EndTime</code>. </p>"""
    max_records: NotRequired["aws_sdk_elastic_beanstalk.types.max_records.MaxRecords"]
    """<p>Specifies the maximum number of events that can be returned, beginning with the most recent event.</p>"""
    next_token: NotRequired["aws_sdk_elastic_beanstalk.types.token.Token"]
    """<p>Pagination token. If specified, the events return the next batch of results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "application_name" in value:
        pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    if "version_label" in value:
        pairs.append((f"{prefix}.VersionLabel", str(value["version_label"])))
    if "template_name" in value:
        pairs.append((f"{prefix}.TemplateName", str(value["template_name"])))
    if "environment_id" in value:
        pairs.append((f"{prefix}.EnvironmentId", str(value["environment_id"])))
    if "environment_name" in value:
        pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))
    if "platform_arn" in value:
        pairs.append((f"{prefix}.PlatformArn", str(value["platform_arn"])))
    if "request_id" in value:
        pairs.append((f"{prefix}.RequestId", str(value["request_id"])))
    if "severity" in value:
        import aws_sdk_elastic_beanstalk.types.event_severity

        aws_sdk_elastic_beanstalk.types.event_severity.serialize_query(
            value["severity"], pairs, f"{prefix}.Severity"
        )
    if "start_time" in value:
        import aws_sdk_elastic_beanstalk.types.time_filter_start

        aws_sdk_elastic_beanstalk.types.time_filter_start.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import aws_sdk_elastic_beanstalk.types.time_filter_end

        aws_sdk_elastic_beanstalk.types.time_filter_end.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeEventsMessage:
    out: DescribeEventsMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    child_request_id = el.find("RequestId")
    if child_request_id is not None:
        out["request_id"] = str(child_request_id.text or "")
    child_severity = el.find("Severity")
    if child_severity is not None:
        import aws_sdk_elastic_beanstalk.types.event_severity

        out["severity"] = (
            aws_sdk_elastic_beanstalk.types.event_severity.deserialize_query(
                child_severity
            )
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_elastic_beanstalk.types.time_filter_start

        out["start_time"] = (
            aws_sdk_elastic_beanstalk.types.time_filter_start.deserialize_query(
                child_start_time
            )
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import aws_sdk_elastic_beanstalk.types.time_filter_end

        out["end_time"] = (
            aws_sdk_elastic_beanstalk.types.time_filter_end.deserialize_query(
                child_end_time
            )
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
