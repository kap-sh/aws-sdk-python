"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeEnvironmentHealthResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_metrics
    import aws_sdk_elastic_beanstalk.types.causes
    import aws_sdk_elastic_beanstalk.types.environment_health
    import aws_sdk_elastic_beanstalk.types.environment_name
    import aws_sdk_elastic_beanstalk.types.instance_health_summary
    import aws_sdk_elastic_beanstalk.types.refreshed_at
    import aws_sdk_elastic_beanstalk.types.string


class DescribeEnvironmentHealthResult(TypedDict, closed=True):
    environment_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The environment's name.</p>"""
    health_status: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html\">health status</a> of the environment. For example, <code>Ok</code>.</p>"""
    status: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_health.EnvironmentHealth"
    ]
    """<p>The environment's operational status. <code>Ready</code>, <code>Launching</code>, <code>Updating</code>, <code>Terminating</code>, or <code>Terminated</code>.</p>"""
    color: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html\">health color</a> of the environment.</p>"""
    causes: NotRequired["aws_sdk_elastic_beanstalk.types.causes.Causes"]
    """<p>Descriptions of the data that contributed to the environment's current health status.</p>"""
    application_metrics: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_metrics.ApplicationMetrics"
    ]
    """<p>Application request metrics for the environment.</p>"""
    instances_health: NotRequired[
        "aws_sdk_elastic_beanstalk.types.instance_health_summary.InstanceHealthSummary"
    ]
    """<p>Summary health information for the instances in the environment.</p>"""
    refreshed_at: NotRequired[
        "aws_sdk_elastic_beanstalk.types.refreshed_at.RefreshedAt"
    ]
    """<p>The date and time that the health information was retrieved.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEnvironmentHealthResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "environment_name" in value:
        pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))
    if "health_status" in value:
        pairs.append((f"{prefix}.HealthStatus", str(value["health_status"])))
    if "status" in value:
        import aws_sdk_elastic_beanstalk.types.environment_health

        aws_sdk_elastic_beanstalk.types.environment_health.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "color" in value:
        pairs.append((f"{prefix}.Color", str(value["color"])))
    if "causes" in value:
        import aws_sdk_elastic_beanstalk.types.causes

        aws_sdk_elastic_beanstalk.types.causes.serialize_query(
            value["causes"], pairs, f"{prefix}.Causes"
        )
    if "application_metrics" in value:
        import aws_sdk_elastic_beanstalk.types.application_metrics

        aws_sdk_elastic_beanstalk.types.application_metrics.serialize_query(
            value["application_metrics"], pairs, f"{prefix}.ApplicationMetrics"
        )
    if "instances_health" in value:
        import aws_sdk_elastic_beanstalk.types.instance_health_summary

        aws_sdk_elastic_beanstalk.types.instance_health_summary.serialize_query(
            value["instances_health"], pairs, f"{prefix}.InstancesHealth"
        )
    if "refreshed_at" in value:
        import aws_sdk_elastic_beanstalk.types.refreshed_at

        aws_sdk_elastic_beanstalk.types.refreshed_at.serialize_query(
            value["refreshed_at"], pairs, f"{prefix}.RefreshedAt"
        )


def deserialize_query(el: Element) -> DescribeEnvironmentHealthResult:
    out: DescribeEnvironmentHealthResult = {}  # type: ignore[typeddict-item]
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_health_status = el.find("HealthStatus")
    if child_health_status is not None:
        out["health_status"] = str(child_health_status.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_elastic_beanstalk.types.environment_health

        out["status"] = (
            aws_sdk_elastic_beanstalk.types.environment_health.deserialize_query(
                child_status
            )
        )
    child_color = el.find("Color")
    if child_color is not None:
        out["color"] = str(child_color.text or "")
    child_causes = el.find("Causes")
    if child_causes is not None:
        import aws_sdk_elastic_beanstalk.types.causes

        out["causes"] = aws_sdk_elastic_beanstalk.types.causes.deserialize_query(
            child_causes
        )
    child_application_metrics = el.find("ApplicationMetrics")
    if child_application_metrics is not None:
        import aws_sdk_elastic_beanstalk.types.application_metrics

        out["application_metrics"] = (
            aws_sdk_elastic_beanstalk.types.application_metrics.deserialize_query(
                child_application_metrics
            )
        )
    child_instances_health = el.find("InstancesHealth")
    if child_instances_health is not None:
        import aws_sdk_elastic_beanstalk.types.instance_health_summary

        out["instances_health"] = (
            aws_sdk_elastic_beanstalk.types.instance_health_summary.deserialize_query(
                child_instances_health
            )
        )
    child_refreshed_at = el.find("RefreshedAt")
    if child_refreshed_at is not None:
        import aws_sdk_elastic_beanstalk.types.refreshed_at

        out["refreshed_at"] = (
            aws_sdk_elastic_beanstalk.types.refreshed_at.deserialize_query(
                child_refreshed_at
            )
        )
    return out
