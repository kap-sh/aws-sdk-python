"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#Collector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.collector_health
    import aws_sdk_migrationhubstrategy.types.configuration_summary
    import aws_sdk_migrationhubstrategy.types.string


class Collector(TypedDict):
    collector_id: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> The ID of the collector. </p>"""
    ip_address: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> IP address of the server that is hosting the collector. </p>"""
    host_name: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> Hostname of the server that is hosting the collector. </p>"""
    collector_health: NotRequired[
        "aws_sdk_migrationhubstrategy.types.collector_health.CollectorHealth"
    ]
    """<p> Indicates the health of a collector. </p>"""
    collector_version: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> Current version of the collector that is running in the environment that you specify. </p>"""
    registered_time_stamp: NotRequired[
        "aws_sdk_migrationhubstrategy.types.string.String"
    ]
    """<p> Time when the collector registered with the service. </p>"""
    last_activity_time_stamp: NotRequired[
        "aws_sdk_migrationhubstrategy.types.string.String"
    ]
    """<p> Time when the collector last pinged the service. </p>"""
    configuration_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.configuration_summary.ConfigurationSummary"
    ]
    """<p>Summary of the collector configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Collector) -> dict:
    out: dict = {}
    if "collector_id" in value:
        out["collectorId"] = value["collector_id"]
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "host_name" in value:
        out["hostName"] = value["host_name"]
    if "collector_health" in value:
        out["collectorHealth"] = value["collector_health"]
    if "collector_version" in value:
        out["collectorVersion"] = value["collector_version"]
    if "registered_time_stamp" in value:
        out["registeredTimeStamp"] = value["registered_time_stamp"]
    if "last_activity_time_stamp" in value:
        out["lastActivityTimeStamp"] = value["last_activity_time_stamp"]
    if "configuration_summary" in value:
        import aws_sdk_migrationhubstrategy.types.configuration_summary

        out["configurationSummary"] = (
            aws_sdk_migrationhubstrategy.types.configuration_summary.serialize_json(
                value["configuration_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> Collector:
    out: Collector = {}  # type: ignore[typeddict-item]
    if "collectorId" in data:
        out["collector_id"] = data["collectorId"]
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    if "hostName" in data:
        out["host_name"] = data["hostName"]
    if "collectorHealth" in data:
        out["collector_health"] = data["collectorHealth"]
    if "collectorVersion" in data:
        out["collector_version"] = data["collectorVersion"]
    if "registeredTimeStamp" in data:
        out["registered_time_stamp"] = data["registeredTimeStamp"]
    if "lastActivityTimeStamp" in data:
        out["last_activity_time_stamp"] = data["lastActivityTimeStamp"]
    if "configurationSummary" in data:
        import aws_sdk_migrationhubstrategy.types.configuration_summary

        out["configuration_summary"] = (
            aws_sdk_migrationhubstrategy.types.configuration_summary.deserialize_json(
                data["configurationSummary"]
            )
        )
    return out
