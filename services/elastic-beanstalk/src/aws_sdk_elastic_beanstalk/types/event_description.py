"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EventDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.configuration_template_name
    import aws_sdk_elastic_beanstalk.types.environment_name
    import aws_sdk_elastic_beanstalk.types.event_date
    import aws_sdk_elastic_beanstalk.types.event_message
    import aws_sdk_elastic_beanstalk.types.event_severity
    import aws_sdk_elastic_beanstalk.types.platform_arn
    import aws_sdk_elastic_beanstalk.types.request_id
    import aws_sdk_elastic_beanstalk.types.version_label


class EventDescription(TypedDict):
    event_date: NotRequired["aws_sdk_elastic_beanstalk.types.event_date.EventDate"]
    """<p>The date when the event occurred.</p>"""
    message: NotRequired["aws_sdk_elastic_beanstalk.types.event_message.EventMessage"]
    """<p>The event message.</p>"""
    application_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>The application associated with the event.</p>"""
    version_label: NotRequired[
        "aws_sdk_elastic_beanstalk.types.version_label.VersionLabel"
    ]
    """<p>The release label for the application version associated with this event.</p>"""
    template_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    ]
    """<p>The name of the configuration associated with this event.</p>"""
    environment_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment associated with this event.</p>"""
    platform_arn: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_arn.PlatformArn"
    ]
    """<p>The ARN of the platform version.</p>"""
    request_id: NotRequired["aws_sdk_elastic_beanstalk.types.request_id.RequestId"]
    """<p>The web service request ID for the activity of this event.</p>"""
    severity: NotRequired[
        "aws_sdk_elastic_beanstalk.types.event_severity.EventSeverity"
    ]
    """<p>The severity level of this event.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "event_date" in value:
        import aws_sdk_elastic_beanstalk.types.event_date

        aws_sdk_elastic_beanstalk.types.event_date.serialize_query(
            value["event_date"], pairs, f"{prefix}.EventDate"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))
    if "application_name" in value:
        pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    if "version_label" in value:
        pairs.append((f"{prefix}.VersionLabel", str(value["version_label"])))
    if "template_name" in value:
        pairs.append((f"{prefix}.TemplateName", str(value["template_name"])))
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


def deserialize_query(el: Element) -> EventDescription:
    out: EventDescription = {}  # type: ignore[typeddict-item]
    child_event_date = el.find("EventDate")
    if child_event_date is not None:
        import aws_sdk_elastic_beanstalk.types.event_date

        out["event_date"] = (
            aws_sdk_elastic_beanstalk.types.event_date.deserialize_query(
                child_event_date
            )
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
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
    return out
