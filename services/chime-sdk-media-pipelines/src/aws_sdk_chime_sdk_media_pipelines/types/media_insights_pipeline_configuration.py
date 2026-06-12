"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.arn
    import aws_sdk_chime_sdk_media_pipelines.types.guid_string
    import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string
    import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_configuration


class MediaInsightsPipelineConfiguration(TypedDict):
    media_insights_pipeline_configuration_name: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string.MediaInsightsPipelineConfigurationNameString"
    ]
    """<p>The name of the configuration.</p>"""
    media_insights_pipeline_configuration_arn: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.arn.Arn"
    ]
    """<p>The ARN of the configuration.</p>"""
    resource_access_role_arn: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.arn.Arn"
    ]
    """<p>The ARN of the role used by the service to access Amazon Web Services resources.</p>"""
    real_time_alert_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_configuration.RealTimeAlertConfiguration"
    ]
    """<p>Lists the rules that trigger a real-time alert.</p>"""
    elements: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.MediaInsightsPipelineConfigurationElements"
    ]
    """<p>The elements in the configuration.</p>"""
    media_insights_pipeline_configuration_id: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.guid_string.GuidString"
    ]
    """<p>The ID of the configuration.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the configuration was created.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the configuration was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineConfiguration) -> dict:
    out: dict = {}
    if "media_insights_pipeline_configuration_name" in value:
        out["MediaInsightsPipelineConfigurationName"] = value[
            "media_insights_pipeline_configuration_name"
        ]
    if "media_insights_pipeline_configuration_arn" in value:
        out["MediaInsightsPipelineConfigurationArn"] = value[
            "media_insights_pipeline_configuration_arn"
        ]
    if "resource_access_role_arn" in value:
        out["ResourceAccessRoleArn"] = value["resource_access_role_arn"]
    if "real_time_alert_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_configuration

        out["RealTimeAlertConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_configuration.serialize_json(
                value["real_time_alert_configuration"]
            )
        )
    if "elements" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements

        out["Elements"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.serialize_json(
                value["elements"]
            )
        )
    if "media_insights_pipeline_configuration_id" in value:
        out["MediaInsightsPipelineConfigurationId"] = value[
            "media_insights_pipeline_configuration_id"
        ]
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaInsightsPipelineConfiguration:
    out: MediaInsightsPipelineConfiguration = {}  # type: ignore[typeddict-item]
    if "MediaInsightsPipelineConfigurationName" in data:
        out["media_insights_pipeline_configuration_name"] = data[
            "MediaInsightsPipelineConfigurationName"
        ]
    if "MediaInsightsPipelineConfigurationArn" in data:
        out["media_insights_pipeline_configuration_arn"] = data[
            "MediaInsightsPipelineConfigurationArn"
        ]
    if "ResourceAccessRoleArn" in data:
        out["resource_access_role_arn"] = data["ResourceAccessRoleArn"]
    if "RealTimeAlertConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_configuration

        out["real_time_alert_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_configuration.deserialize_json(
                data["RealTimeAlertConfiguration"]
            )
        )
    if "Elements" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements

        out["elements"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.deserialize_json(
                data["Elements"]
            )
        )
    if "MediaInsightsPipelineConfigurationId" in data:
        out["media_insights_pipeline_configuration_id"] = data[
            "MediaInsightsPipelineConfigurationId"
        ]
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["updated_timestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    return out
