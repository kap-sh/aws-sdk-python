"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryDestinationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.cloudtrail_parameters
    import aws_sdk_observabilityadmin.types.destination_type
    import aws_sdk_observabilityadmin.types.elb_load_balancer_logging_parameters
    import aws_sdk_observabilityadmin.types.log_delivery_parameters
    import aws_sdk_observabilityadmin.types.msk_monitoring_parameters
    import aws_sdk_observabilityadmin.types.retention_period_in_days
    import aws_sdk_observabilityadmin.types.vpc_flow_log_parameters
    import aws_sdk_observabilityadmin.types.waf_logging_parameters


class TelemetryDestinationConfiguration(TypedDict):
    destination_type: NotRequired[
        "aws_sdk_observabilityadmin.types.destination_type.DestinationType"
    ]
    r"""<p> The type of destination for the telemetry data (e.g., \"Amazon CloudWatch Logs\", \"S3\"). </p>"""
    destination_pattern: NotRequired["str"]
    """<p> The pattern used to generate the destination path or name, supporting macros like &lt;resourceId&gt; and &lt;accountId&gt;. </p>"""
    retention_in_days: NotRequired[
        "aws_sdk_observabilityadmin.types.retention_period_in_days.RetentionPeriodInDays"
    ]
    """<p> The number of days to retain the telemetry data in the destination. </p>"""
    vpc_flow_log_parameters: NotRequired[
        "aws_sdk_observabilityadmin.types.vpc_flow_log_parameters.VPCFlowLogParameters"
    ]
    """<p> Configuration parameters specific to VPC Flow Logs when VPC is the resource type. </p>"""
    cloudtrail_parameters: NotRequired[
        "aws_sdk_observabilityadmin.types.cloudtrail_parameters.CloudtrailParameters"
    ]
    """<p> Configuration parameters specific to Amazon Web Services CloudTrail when CloudTrail is the source type. </p>"""
    elb_load_balancer_logging_parameters: NotRequired[
        "aws_sdk_observabilityadmin.types.elb_load_balancer_logging_parameters.ELBLoadBalancerLoggingParameters"
    ]
    """<p> Configuration parameters specific to ELB load balancer logging when ELB is the resource type. </p>"""
    waf_logging_parameters: NotRequired[
        "aws_sdk_observabilityadmin.types.waf_logging_parameters.WAFLoggingParameters"
    ]
    """<p> Configuration parameters specific to WAF logging when WAF is the resource type. </p>"""
    log_delivery_parameters: NotRequired[
        "aws_sdk_observabilityadmin.types.log_delivery_parameters.LogDeliveryParameters"
    ]
    """<p>Configuration parameters specific to Amazon Bedrock AgentCore logging when Amazon Bedrock AgentCore is the resource type.</p>"""
    msk_monitoring_parameters: NotRequired[
        "aws_sdk_observabilityadmin.types.msk_monitoring_parameters.MskMonitoringParameters"
    ]
    """<p> Configuration parameters specific to MSK monitoring when MSK is the resource type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryDestinationConfiguration) -> dict:
    out: dict = {}
    if "destination_type" in value:
        import aws_sdk_observabilityadmin.types.destination_type

        out["DestinationType"] = (
            aws_sdk_observabilityadmin.types.destination_type.serialize_json(
                value["destination_type"]
            )
        )
    if "destination_pattern" in value:
        out["DestinationPattern"] = value["destination_pattern"]
    if "retention_in_days" in value:
        out["RetentionInDays"] = value["retention_in_days"]
    if "vpc_flow_log_parameters" in value:
        import aws_sdk_observabilityadmin.types.vpc_flow_log_parameters

        out["VPCFlowLogParameters"] = (
            aws_sdk_observabilityadmin.types.vpc_flow_log_parameters.serialize_json(
                value["vpc_flow_log_parameters"]
            )
        )
    if "cloudtrail_parameters" in value:
        import aws_sdk_observabilityadmin.types.cloudtrail_parameters

        out["CloudtrailParameters"] = (
            aws_sdk_observabilityadmin.types.cloudtrail_parameters.serialize_json(
                value["cloudtrail_parameters"]
            )
        )
    if "elb_load_balancer_logging_parameters" in value:
        import aws_sdk_observabilityadmin.types.elb_load_balancer_logging_parameters

        out["ELBLoadBalancerLoggingParameters"] = (
            aws_sdk_observabilityadmin.types.elb_load_balancer_logging_parameters.serialize_json(
                value["elb_load_balancer_logging_parameters"]
            )
        )
    if "waf_logging_parameters" in value:
        import aws_sdk_observabilityadmin.types.waf_logging_parameters

        out["WAFLoggingParameters"] = (
            aws_sdk_observabilityadmin.types.waf_logging_parameters.serialize_json(
                value["waf_logging_parameters"]
            )
        )
    if "log_delivery_parameters" in value:
        import aws_sdk_observabilityadmin.types.log_delivery_parameters

        out["LogDeliveryParameters"] = (
            aws_sdk_observabilityadmin.types.log_delivery_parameters.serialize_json(
                value["log_delivery_parameters"]
            )
        )
    if "msk_monitoring_parameters" in value:
        import aws_sdk_observabilityadmin.types.msk_monitoring_parameters

        out["MskMonitoringParameters"] = (
            aws_sdk_observabilityadmin.types.msk_monitoring_parameters.serialize_json(
                value["msk_monitoring_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> TelemetryDestinationConfiguration:
    out: TelemetryDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "DestinationType" in data:
        import aws_sdk_observabilityadmin.types.destination_type

        out["destination_type"] = (
            aws_sdk_observabilityadmin.types.destination_type.deserialize_json(
                data["DestinationType"]
            )
        )
    if "DestinationPattern" in data:
        out["destination_pattern"] = data["DestinationPattern"]
    if "RetentionInDays" in data:
        out["retention_in_days"] = data["RetentionInDays"]
    if "VPCFlowLogParameters" in data:
        import aws_sdk_observabilityadmin.types.vpc_flow_log_parameters

        out["vpc_flow_log_parameters"] = (
            aws_sdk_observabilityadmin.types.vpc_flow_log_parameters.deserialize_json(
                data["VPCFlowLogParameters"]
            )
        )
    if "CloudtrailParameters" in data:
        import aws_sdk_observabilityadmin.types.cloudtrail_parameters

        out["cloudtrail_parameters"] = (
            aws_sdk_observabilityadmin.types.cloudtrail_parameters.deserialize_json(
                data["CloudtrailParameters"]
            )
        )
    if "ELBLoadBalancerLoggingParameters" in data:
        import aws_sdk_observabilityadmin.types.elb_load_balancer_logging_parameters

        out["elb_load_balancer_logging_parameters"] = (
            aws_sdk_observabilityadmin.types.elb_load_balancer_logging_parameters.deserialize_json(
                data["ELBLoadBalancerLoggingParameters"]
            )
        )
    if "WAFLoggingParameters" in data:
        import aws_sdk_observabilityadmin.types.waf_logging_parameters

        out["waf_logging_parameters"] = (
            aws_sdk_observabilityadmin.types.waf_logging_parameters.deserialize_json(
                data["WAFLoggingParameters"]
            )
        )
    if "LogDeliveryParameters" in data:
        import aws_sdk_observabilityadmin.types.log_delivery_parameters

        out["log_delivery_parameters"] = (
            aws_sdk_observabilityadmin.types.log_delivery_parameters.deserialize_json(
                data["LogDeliveryParameters"]
            )
        )
    if "MskMonitoringParameters" in data:
        import aws_sdk_observabilityadmin.types.msk_monitoring_parameters

        out["msk_monitoring_parameters"] = (
            aws_sdk_observabilityadmin.types.msk_monitoring_parameters.deserialize_json(
                data["MskMonitoringParameters"]
            )
        )
    return out
