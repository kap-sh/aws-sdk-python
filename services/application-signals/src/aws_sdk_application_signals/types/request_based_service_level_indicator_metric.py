"""Generated from Smithy shape ``com.amazonaws.applicationsignals#RequestBasedServiceLevelIndicatorMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.attributes
    import aws_sdk_application_signals.types.composite_sli_config
    import aws_sdk_application_signals.types.dependency_config
    import aws_sdk_application_signals.types.metric_data_queries
    import aws_sdk_application_signals.types.metric_source
    import aws_sdk_application_signals.types.monitored_request_count_metric_data_queries
    import aws_sdk_application_signals.types.operation_name
    import aws_sdk_application_signals.types.service_level_indicator_metric_type


class RequestBasedServiceLevelIndicatorMetric(TypedDict):
    key_attributes: NotRequired[
        "aws_sdk_application_signals.types.attributes.Attributes"
    ]
    """<p>This is a string-to-string map that contains information about the type of object that this SLO is related to. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object that this SLO is related to.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>"""
    operation_name: NotRequired[
        "aws_sdk_application_signals.types.operation_name.OperationName"
    ]
    """<p>If the SLO monitors a specific operation of the service, this field displays that operation name.</p>"""
    metric_type: NotRequired[
        "aws_sdk_application_signals.types.service_level_indicator_metric_type.ServiceLevelIndicatorMetricType"
    ]
    """<p>If the SLO monitors either the <code>LATENCY</code> or <code>AVAILABILITY</code> metric that Application Signals collects, this field displays which of those metrics is used.</p>"""
    total_request_count_metric: (
        "aws_sdk_application_signals.types.metric_data_queries.MetricDataQueries"
    )
    r"""<p>This structure defines the metric that is used as the \"total requests\" number for a request-based SLO. The number observed for this metric is divided by the number of \"good requests\" or \"bad requests\" that is observed for the metric defined in <code>MonitoredRequestCountMetric</code>.</p>"""
    monitored_request_count_metric: "aws_sdk_application_signals.types.monitored_request_count_metric_data_queries.MonitoredRequestCountMetricDataQueries"
    r"""<p>This structure defines the metric that is used as the \"good request\" or \"bad request\" value for a request-based SLO. This value observed for the metric defined in <code>TotalRequestCountMetric</code> is divided by the number found for <code>MonitoredRequestCountMetric</code> to determine the percentage of successful requests that this SLO tracks.</p>"""
    dependency_config: NotRequired[
        "aws_sdk_application_signals.types.dependency_config.DependencyConfig"
    ]
    """<p>Identifies the dependency using the <code>DependencyKeyAttributes</code> and <code>DependencyOperationName</code>. </p>"""
    metric_source: NotRequired[
        "aws_sdk_application_signals.types.metric_source.MetricSource"
    ]
    """<p>Identifies the metric source for SLOs on resources other than Application Signals services.</p>"""
    composite_sli_config: NotRequired[
        "aws_sdk_application_signals.types.composite_sli_config.CompositeSliConfig"
    ]
    """<p>The composite SLI configuration for service-level SLOs that monitor multiple operations of a service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestBasedServiceLevelIndicatorMetric) -> dict:
    out: dict = {}
    if "key_attributes" in value:
        import aws_sdk_application_signals.types.attributes

        out["KeyAttributes"] = (
            aws_sdk_application_signals.types.attributes.serialize_json(
                value["key_attributes"]
            )
        )
    if "operation_name" in value:
        out["OperationName"] = value["operation_name"]
    if "metric_type" in value:
        import aws_sdk_application_signals.types.service_level_indicator_metric_type

        out["MetricType"] = (
            aws_sdk_application_signals.types.service_level_indicator_metric_type.serialize_json(
                value["metric_type"]
            )
        )
    import aws_sdk_application_signals.types.metric_data_queries

    out["TotalRequestCountMetric"] = (
        aws_sdk_application_signals.types.metric_data_queries.serialize_json(
            value["total_request_count_metric"]
        )
    )
    import aws_sdk_application_signals.types.monitored_request_count_metric_data_queries

    out["MonitoredRequestCountMetric"] = (
        aws_sdk_application_signals.types.monitored_request_count_metric_data_queries.serialize_json(
            value["monitored_request_count_metric"]
        )
    )
    if "dependency_config" in value:
        import aws_sdk_application_signals.types.dependency_config

        out["DependencyConfig"] = (
            aws_sdk_application_signals.types.dependency_config.serialize_json(
                value["dependency_config"]
            )
        )
    if "metric_source" in value:
        import aws_sdk_application_signals.types.metric_source

        out["MetricSource"] = (
            aws_sdk_application_signals.types.metric_source.serialize_json(
                value["metric_source"]
            )
        )
    if "composite_sli_config" in value:
        import aws_sdk_application_signals.types.composite_sli_config

        out["CompositeSliConfig"] = (
            aws_sdk_application_signals.types.composite_sli_config.serialize_json(
                value["composite_sli_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> RequestBasedServiceLevelIndicatorMetric:
    out: RequestBasedServiceLevelIndicatorMetric = {}  # type: ignore[typeddict-item]
    if "KeyAttributes" in data:
        import aws_sdk_application_signals.types.attributes

        out["key_attributes"] = (
            aws_sdk_application_signals.types.attributes.deserialize_json(
                data["KeyAttributes"]
            )
        )
    if "OperationName" in data:
        out["operation_name"] = data["OperationName"]
    if "MetricType" in data:
        import aws_sdk_application_signals.types.service_level_indicator_metric_type

        out["metric_type"] = (
            aws_sdk_application_signals.types.service_level_indicator_metric_type.deserialize_json(
                data["MetricType"]
            )
        )
    if "TotalRequestCountMetric" in data:
        import aws_sdk_application_signals.types.metric_data_queries

        out["total_request_count_metric"] = (
            aws_sdk_application_signals.types.metric_data_queries.deserialize_json(
                data["TotalRequestCountMetric"]
            )
        )
    else:
        raise DeserializationError(
            "RequestBasedServiceLevelIndicatorMetric.total_request_count_metric required"
        )
    if "MonitoredRequestCountMetric" in data:
        import aws_sdk_application_signals.types.monitored_request_count_metric_data_queries

        out["monitored_request_count_metric"] = (
            aws_sdk_application_signals.types.monitored_request_count_metric_data_queries.deserialize_json(
                data["MonitoredRequestCountMetric"]
            )
        )
    else:
        raise DeserializationError(
            "RequestBasedServiceLevelIndicatorMetric.monitored_request_count_metric required"
        )
    if "DependencyConfig" in data:
        import aws_sdk_application_signals.types.dependency_config

        out["dependency_config"] = (
            aws_sdk_application_signals.types.dependency_config.deserialize_json(
                data["DependencyConfig"]
            )
        )
    if "MetricSource" in data:
        import aws_sdk_application_signals.types.metric_source

        out["metric_source"] = (
            aws_sdk_application_signals.types.metric_source.deserialize_json(
                data["MetricSource"]
            )
        )
    if "CompositeSliConfig" in data:
        import aws_sdk_application_signals.types.composite_sli_config

        out["composite_sli_config"] = (
            aws_sdk_application_signals.types.composite_sli_config.deserialize_json(
                data["CompositeSliConfig"]
            )
        )
    return out
