"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaInsightsPipelineConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.arn
    import aws_sdk_chime_sdk_media_pipelines.types.client_request_token
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string
    import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.tag_list


class CreateMediaInsightsPipelineConfigurationRequest(TypedDict):
    media_insights_pipeline_configuration_name: "aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string.MediaInsightsPipelineConfigurationNameString"
    """<p>The name of the media insights pipeline configuration.</p>"""
    resource_access_role_arn: "aws_sdk_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The ARN of the role used by the service to access Amazon Web Services resources, including <code>Transcribe</code> and <code>Transcribe Call Analytics</code>, on the caller’s behalf.</p>"""
    real_time_alert_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_configuration.RealTimeAlertConfiguration"
    ]
    """<p>The configuration settings for the real-time alerts in a media insights pipeline configuration.</p>"""
    elements: "aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.MediaInsightsPipelineConfigurationElements"
    """<p>The elements in the request, such as a processor for Amazon Transcribe or a sink for a Kinesis Data Stream.</p>"""
    tags: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.tag_list.TagList"]
    """<p>The tags assigned to the media insights pipeline configuration.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique identifier for the media insights pipeline configuration request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaInsightsPipelineConfigurationRequest) -> dict:
    out: dict = {}
    out["MediaInsightsPipelineConfigurationName"] = value[
        "media_insights_pipeline_configuration_name"
    ]
    out["ResourceAccessRoleArn"] = value["resource_access_role_arn"]
    if "real_time_alert_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_configuration

        out["RealTimeAlertConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_configuration.serialize_json(
                value["real_time_alert_configuration"]
            )
        )
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements

    out["Elements"] = (
        aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.serialize_json(
            value["elements"]
        )
    )
    if "tags" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.tag_list

        out["Tags"] = aws_sdk_chime_sdk_media_pipelines.types.tag_list.serialize_json(
            value["tags"]
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateMediaInsightsPipelineConfigurationRequest:
    out: CreateMediaInsightsPipelineConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "MediaInsightsPipelineConfigurationName" in data:
        out["media_insights_pipeline_configuration_name"] = data[
            "MediaInsightsPipelineConfigurationName"
        ]
    else:
        raise DeserializationError(
            "CreateMediaInsightsPipelineConfigurationRequest.media_insights_pipeline_configuration_name required"
        )
    if "ResourceAccessRoleArn" in data:
        out["resource_access_role_arn"] = data["ResourceAccessRoleArn"]
    else:
        raise DeserializationError(
            "CreateMediaInsightsPipelineConfigurationRequest.resource_access_role_arn required"
        )
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
    else:
        raise DeserializationError(
            "CreateMediaInsightsPipelineConfigurationRequest.elements required"
        )
    if "Tags" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.tag_list

        out["tags"] = aws_sdk_chime_sdk_media_pipelines.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
