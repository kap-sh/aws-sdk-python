"""Generated from Smithy shape ``com.amazonaws.mediatailor#ConfigureLogsForPlaybackConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer
    import aws_sdk_mediatailor.types.__list_of_logging_strategies
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.ads_interaction_log
    import aws_sdk_mediatailor.types.manifest_service_interaction_log


class ConfigureLogsForPlaybackConfigurationResponse(TypedDict, closed=True):
    percent_enabled: "aws_sdk_mediatailor.types.__integer.__integer"
    """<p>The percentage of session logs that MediaTailor sends to your Cloudwatch Logs account.</p>"""
    playback_configuration_name: NotRequired[
        "aws_sdk_mediatailor.types.__string.__string"
    ]
    """<p>The name of the playback configuration.</p>"""
    enabled_logging_strategies: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_logging_strategies.__listOfLoggingStrategies"
    ]
    """<p>The method used for collecting logs from AWS Elemental MediaTailor. <code>LEGACY_CLOUDWATCH</code> indicates that MediaTailor is sending logs directly to Amazon CloudWatch Logs. <code>VENDED_LOGS</code> indicates that MediaTailor is sending logs to CloudWatch, which then vends the logs to your destination of choice. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream. </p>"""
    ads_interaction_log: NotRequired[
        "aws_sdk_mediatailor.types.ads_interaction_log.AdsInteractionLog"
    ]
    """<p>The event types that MediaTailor emits in logs for interactions with the ADS.</p>"""
    manifest_service_interaction_log: NotRequired[
        "aws_sdk_mediatailor.types.manifest_service_interaction_log.ManifestServiceInteractionLog"
    ]
    """<p>The event types that MediaTailor emits in logs for interactions with the origin server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureLogsForPlaybackConfigurationResponse) -> dict:
    out: dict = {}
    out["PercentEnabled"] = value.get("percent_enabled", 0)
    if "playback_configuration_name" in value:
        out["PlaybackConfigurationName"] = value["playback_configuration_name"]
    if "enabled_logging_strategies" in value:
        import aws_sdk_mediatailor.types.__list_of_logging_strategies

        out["EnabledLoggingStrategies"] = (
            aws_sdk_mediatailor.types.__list_of_logging_strategies.serialize_json(
                value["enabled_logging_strategies"]
            )
        )
    if "ads_interaction_log" in value:
        import aws_sdk_mediatailor.types.ads_interaction_log

        out["AdsInteractionLog"] = (
            aws_sdk_mediatailor.types.ads_interaction_log.serialize_json(
                value["ads_interaction_log"]
            )
        )
    if "manifest_service_interaction_log" in value:
        import aws_sdk_mediatailor.types.manifest_service_interaction_log

        out["ManifestServiceInteractionLog"] = (
            aws_sdk_mediatailor.types.manifest_service_interaction_log.serialize_json(
                value["manifest_service_interaction_log"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigureLogsForPlaybackConfigurationResponse:
    out: ConfigureLogsForPlaybackConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "PercentEnabled" in data:
        out["percent_enabled"] = data["PercentEnabled"]
    else:
        out["percent_enabled"] = 0
    if "PlaybackConfigurationName" in data:
        out["playback_configuration_name"] = data["PlaybackConfigurationName"]
    if "EnabledLoggingStrategies" in data:
        import aws_sdk_mediatailor.types.__list_of_logging_strategies

        out["enabled_logging_strategies"] = (
            aws_sdk_mediatailor.types.__list_of_logging_strategies.deserialize_json(
                data["EnabledLoggingStrategies"]
            )
        )
    if "AdsInteractionLog" in data:
        import aws_sdk_mediatailor.types.ads_interaction_log

        out["ads_interaction_log"] = (
            aws_sdk_mediatailor.types.ads_interaction_log.deserialize_json(
                data["AdsInteractionLog"]
            )
        )
    if "ManifestServiceInteractionLog" in data:
        import aws_sdk_mediatailor.types.manifest_service_interaction_log

        out["manifest_service_interaction_log"] = (
            aws_sdk_mediatailor.types.manifest_service_interaction_log.deserialize_json(
                data["ManifestServiceInteractionLog"]
            )
        )
    return out
