"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_internetmonitor.types.health_events_config
    import capo_internetmonitor.types.internet_measurements_log_delivery
    import capo_internetmonitor.types.max_city_networks_to_monitor
    import capo_internetmonitor.types.monitor_arn
    import capo_internetmonitor.types.monitor_config_state
    import capo_internetmonitor.types.monitor_processing_status_code
    import capo_internetmonitor.types.resource_name
    import capo_internetmonitor.types.set_of_ar_ns
    import capo_internetmonitor.types.tag_map
    import capo_internetmonitor.types.traffic_percentage_to_monitor


class GetMonitorOutput(TypedDict, closed=True):
    monitor_name: "capo_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    monitor_arn: "capo_internetmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    resources: "capo_internetmonitor.types.set_of_ar_ns.SetOfARNs"
    """<p>The resources monitored by the monitor. Resources are listed by their Amazon Resource Names (ARNs).</p>"""
    status: "capo_internetmonitor.types.monitor_config_state.MonitorConfigState"
    """<p>The status of the monitor.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the monitor was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The last time that the monitor was modified.</p>"""
    processing_status: NotRequired[
        "capo_internetmonitor.types.monitor_processing_status_code.MonitorProcessingStatusCode"
    ]
    """<p>The health of the data processing for the monitor.</p>"""
    processing_status_info: NotRequired["str"]
    """<p>Additional information about the health of the data processing for the monitor.</p>"""
    tags: NotRequired["capo_internetmonitor.types.tag_map.TagMap"]
    """<p>The tags that have been added to monitor.</p>"""
    max_city_networks_to_monitor: NotRequired[
        "capo_internetmonitor.types.max_city_networks_to_monitor.MaxCityNetworksToMonitor"
    ]
    r"""<p>The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. This limit can help control billing costs.</p> <p>To learn more, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html\">Choosing a city-network maximum value </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""
    internet_measurements_log_delivery: NotRequired[
        "capo_internetmonitor.types.internet_measurements_log_delivery.InternetMeasurementsLogDelivery"
    ]
    """<p>Publish internet measurements for Internet Monitor to another location, such as an Amazon S3 bucket. The measurements are also published to Amazon CloudWatch Logs.</p>"""
    traffic_percentage_to_monitor: NotRequired[
        "capo_internetmonitor.types.traffic_percentage_to_monitor.TrafficPercentageToMonitor"
    ]
    r"""<p>The percentage of the internet-facing traffic for your application to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.</p> <p>To learn more, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html\">Choosing an application traffic percentage to monitor </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""
    health_events_config: NotRequired[
        "capo_internetmonitor.types.health_events_config.HealthEventsConfig"
    ]
    r"""<p>The list of health event threshold configurations. The threshold percentage for a health score determines, along with other configuration information, when Internet Monitor creates a health event when there's an internet issue that affects your application end users.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview\"> Change health event thresholds</a> in the Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorOutput) -> dict:
    out: dict = {}
    out["MonitorName"] = value["monitor_name"]
    out["MonitorArn"] = value["monitor_arn"]
    import capo_internetmonitor.types.set_of_ar_ns

    out["Resources"] = capo_internetmonitor.types.set_of_ar_ns.serialize_json(
        value["resources"]
    )
    out["Status"] = value["status"]
    import capo_internetmonitor.types._prelude.timestamp

    out["CreatedAt"] = capo_internetmonitor.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_internetmonitor.types._prelude.timestamp

    out["ModifiedAt"] = capo_internetmonitor.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    if "processing_status" in value:
        out["ProcessingStatus"] = value["processing_status"]
    if "processing_status_info" in value:
        out["ProcessingStatusInfo"] = value["processing_status_info"]
    if "tags" in value:
        import capo_internetmonitor.types.tag_map

        out["Tags"] = capo_internetmonitor.types.tag_map.serialize_json(value["tags"])
    if "max_city_networks_to_monitor" in value:
        out["MaxCityNetworksToMonitor"] = value["max_city_networks_to_monitor"]
    if "internet_measurements_log_delivery" in value:
        import capo_internetmonitor.types.internet_measurements_log_delivery

        out["InternetMeasurementsLogDelivery"] = (
            capo_internetmonitor.types.internet_measurements_log_delivery.serialize_json(
                value["internet_measurements_log_delivery"]
            )
        )
    if "traffic_percentage_to_monitor" in value:
        out["TrafficPercentageToMonitor"] = value["traffic_percentage_to_monitor"]
    if "health_events_config" in value:
        import capo_internetmonitor.types.health_events_config

        out["HealthEventsConfig"] = (
            capo_internetmonitor.types.health_events_config.serialize_json(
                value["health_events_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMonitorOutput:
    out: GetMonitorOutput = {}  # type: ignore[typeddict-item]
    if "MonitorName" in data:
        out["monitor_name"] = data["MonitorName"]
    else:
        raise DeserializationError("GetMonitorOutput.monitor_name required")
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        raise DeserializationError("GetMonitorOutput.monitor_arn required")
    if "Resources" in data:
        import capo_internetmonitor.types.set_of_ar_ns

        out["resources"] = capo_internetmonitor.types.set_of_ar_ns.deserialize_json(
            data["Resources"]
        )
    else:
        raise DeserializationError("GetMonitorOutput.resources required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("GetMonitorOutput.status required")
    if "CreatedAt" in data:
        import capo_internetmonitor.types._prelude.timestamp

        out["created_at"] = (
            capo_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("GetMonitorOutput.created_at required")
    if "ModifiedAt" in data:
        import capo_internetmonitor.types._prelude.timestamp

        out["modified_at"] = (
            capo_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    else:
        raise DeserializationError("GetMonitorOutput.modified_at required")
    if "ProcessingStatus" in data:
        out["processing_status"] = data["ProcessingStatus"]
    if "ProcessingStatusInfo" in data:
        out["processing_status_info"] = data["ProcessingStatusInfo"]
    if "Tags" in data:
        import capo_internetmonitor.types.tag_map

        out["tags"] = capo_internetmonitor.types.tag_map.deserialize_json(data["Tags"])
    if "MaxCityNetworksToMonitor" in data:
        out["max_city_networks_to_monitor"] = data["MaxCityNetworksToMonitor"]
    if "InternetMeasurementsLogDelivery" in data:
        import capo_internetmonitor.types.internet_measurements_log_delivery

        out["internet_measurements_log_delivery"] = (
            capo_internetmonitor.types.internet_measurements_log_delivery.deserialize_json(
                data["InternetMeasurementsLogDelivery"]
            )
        )
    if "TrafficPercentageToMonitor" in data:
        out["traffic_percentage_to_monitor"] = data["TrafficPercentageToMonitor"]
    if "HealthEventsConfig" in data:
        import capo_internetmonitor.types.health_events_config

        out["health_events_config"] = (
            capo_internetmonitor.types.health_events_config.deserialize_json(
                data["HealthEventsConfig"]
            )
        )
    return out
