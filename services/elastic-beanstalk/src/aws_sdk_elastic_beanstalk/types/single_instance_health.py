"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SingleInstanceHealth``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_metrics
    import aws_sdk_elastic_beanstalk.types.causes
    import aws_sdk_elastic_beanstalk.types.deployment
    import aws_sdk_elastic_beanstalk.types.instance_id
    import aws_sdk_elastic_beanstalk.types.launched_at
    import aws_sdk_elastic_beanstalk.types.string
    import aws_sdk_elastic_beanstalk.types.system_status


class SingleInstanceHealth(TypedDict):
    instance_id: NotRequired["aws_sdk_elastic_beanstalk.types.instance_id.InstanceId"]
    """<p>The ID of the Amazon EC2 instance.</p>"""
    health_status: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    r"""<p>Returns the health status of the specified instance. For more information, see <a href=\"https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html\">Health Colors and Statuses</a>.</p>"""
    color: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    r"""<p>Represents the color indicator that gives you information about the health of the EC2 instance. For more information, see <a href=\"https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html\">Health Colors and Statuses</a>.</p>"""
    causes: NotRequired["aws_sdk_elastic_beanstalk.types.causes.Causes"]
    """<p>Represents the causes, which provide more information about the current health status.</p>"""
    launched_at: NotRequired["aws_sdk_elastic_beanstalk.types.launched_at.LaunchedAt"]
    """<p>The time at which the EC2 instance was launched.</p>"""
    application_metrics: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_metrics.ApplicationMetrics"
    ]
    """<p>Request metrics from your application.</p>"""
    system: NotRequired["aws_sdk_elastic_beanstalk.types.system_status.SystemStatus"]
    """<p>Operating system metrics from the instance.</p>"""
    deployment: NotRequired["aws_sdk_elastic_beanstalk.types.deployment.Deployment"]
    """<p>Information about the most recent deployment to an instance.</p>"""
    availability_zone: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>The availability zone in which the instance runs.</p>"""
    instance_type: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>The instance's type.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SingleInstanceHealth, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "health_status" in value:
        pairs.append((f"{prefix}.HealthStatus", str(value["health_status"])))
    if "color" in value:
        pairs.append((f"{prefix}.Color", str(value["color"])))
    if "causes" in value:
        import aws_sdk_elastic_beanstalk.types.causes

        aws_sdk_elastic_beanstalk.types.causes.serialize_query(
            value["causes"], pairs, f"{prefix}.Causes"
        )
    if "launched_at" in value:
        import aws_sdk_elastic_beanstalk.types.launched_at

        aws_sdk_elastic_beanstalk.types.launched_at.serialize_query(
            value["launched_at"], pairs, f"{prefix}.LaunchedAt"
        )
    if "application_metrics" in value:
        import aws_sdk_elastic_beanstalk.types.application_metrics

        aws_sdk_elastic_beanstalk.types.application_metrics.serialize_query(
            value["application_metrics"], pairs, f"{prefix}.ApplicationMetrics"
        )
    if "system" in value:
        import aws_sdk_elastic_beanstalk.types.system_status

        aws_sdk_elastic_beanstalk.types.system_status.serialize_query(
            value["system"], pairs, f"{prefix}.System"
        )
    if "deployment" in value:
        import aws_sdk_elastic_beanstalk.types.deployment

        aws_sdk_elastic_beanstalk.types.deployment.serialize_query(
            value["deployment"], pairs, f"{prefix}.Deployment"
        )
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))


def deserialize_query(el: Element) -> SingleInstanceHealth:
    out: SingleInstanceHealth = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_health_status = el.find("HealthStatus")
    if child_health_status is not None:
        out["health_status"] = str(child_health_status.text or "")
    child_color = el.find("Color")
    if child_color is not None:
        out["color"] = str(child_color.text or "")
    child_causes = el.find("Causes")
    if child_causes is not None:
        import aws_sdk_elastic_beanstalk.types.causes

        out["causes"] = aws_sdk_elastic_beanstalk.types.causes.deserialize_query(
            child_causes
        )
    child_launched_at = el.find("LaunchedAt")
    if child_launched_at is not None:
        import aws_sdk_elastic_beanstalk.types.launched_at

        out["launched_at"] = (
            aws_sdk_elastic_beanstalk.types.launched_at.deserialize_query(
                child_launched_at
            )
        )
    child_application_metrics = el.find("ApplicationMetrics")
    if child_application_metrics is not None:
        import aws_sdk_elastic_beanstalk.types.application_metrics

        out["application_metrics"] = (
            aws_sdk_elastic_beanstalk.types.application_metrics.deserialize_query(
                child_application_metrics
            )
        )
    child_system = el.find("System")
    if child_system is not None:
        import aws_sdk_elastic_beanstalk.types.system_status

        out["system"] = aws_sdk_elastic_beanstalk.types.system_status.deserialize_query(
            child_system
        )
    child_deployment = el.find("Deployment")
    if child_deployment is not None:
        import aws_sdk_elastic_beanstalk.types.deployment

        out["deployment"] = (
            aws_sdk_elastic_beanstalk.types.deployment.deserialize_query(
                child_deployment
            )
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    return out
