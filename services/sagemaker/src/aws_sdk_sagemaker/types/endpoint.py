"""Generated from Smithy shape ``com.amazonaws.sagemaker#Endpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.data_capture_config_summary
    import aws_sdk_sagemaker.types.endpoint_arn
    import aws_sdk_sagemaker.types.endpoint_config_name
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.endpoint_status
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.monitoring_schedule_list
    import aws_sdk_sagemaker.types.production_variant_summary_list
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.timestamp


class Endpoint(TypedDict):
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint.</p>"""
    endpoint_arn: NotRequired["aws_sdk_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""
    endpoint_config_name: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    """<p>The endpoint configuration associated with the endpoint.</p>"""
    production_variants: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_summary_list.ProductionVariantSummaryList"
    ]
    """<p>A list of the production variants hosted on the endpoint. Each production variant is a model.</p>"""
    data_capture_config: NotRequired[
        "aws_sdk_sagemaker.types.data_capture_config_summary.DataCaptureConfigSummary"
    ]
    endpoint_status: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_status.EndpointStatus"
    ]
    """<p>The status of the endpoint.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the endpoint failed, the reason it failed.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the endpoint was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The last time the endpoint was modified.</p>"""
    monitoring_schedules: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_list.MonitoringScheduleList"
    ]
    r"""<p>A list of monitoring schedules for the endpoint. For information about model monitoring, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html\">Amazon SageMaker Model Monitor</a>.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>A list of the tags associated with the endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""
    shadow_production_variants: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_summary_list.ProductionVariantSummaryList"
    ]
    """<p>A list of the shadow variants hosted on the endpoint. Each shadow variant is a model in shadow mode with production traffic replicated from the production variant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoint) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
    if "production_variants" in value:
        import aws_sdk_sagemaker.types.production_variant_summary_list

        out["ProductionVariants"] = (
            aws_sdk_sagemaker.types.production_variant_summary_list.serialize_aws_json_1_1(
                value["production_variants"]
            )
        )
    if "data_capture_config" in value:
        import aws_sdk_sagemaker.types.data_capture_config_summary

        out["DataCaptureConfig"] = (
            aws_sdk_sagemaker.types.data_capture_config_summary.serialize_aws_json_1_1(
                value["data_capture_config"]
            )
        )
    if "endpoint_status" in value:
        import aws_sdk_sagemaker.types.endpoint_status

        out["EndpointStatus"] = (
            aws_sdk_sagemaker.types.endpoint_status.serialize_aws_json_1_1(
                value["endpoint_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "monitoring_schedules" in value:
        import aws_sdk_sagemaker.types.monitoring_schedule_list

        out["MonitoringSchedules"] = (
            aws_sdk_sagemaker.types.monitoring_schedule_list.serialize_aws_json_1_1(
                value["monitoring_schedules"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "shadow_production_variants" in value:
        import aws_sdk_sagemaker.types.production_variant_summary_list

        out["ShadowProductionVariants"] = (
            aws_sdk_sagemaker.types.production_variant_summary_list.serialize_aws_json_1_1(
                value["shadow_production_variants"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    if "EndpointConfigName" in data:
        out["endpoint_config_name"] = data["EndpointConfigName"]
    if "ProductionVariants" in data:
        import aws_sdk_sagemaker.types.production_variant_summary_list

        out["production_variants"] = (
            aws_sdk_sagemaker.types.production_variant_summary_list.deserialize_aws_json_1_1(
                data["ProductionVariants"]
            )
        )
    if "DataCaptureConfig" in data:
        import aws_sdk_sagemaker.types.data_capture_config_summary

        out["data_capture_config"] = (
            aws_sdk_sagemaker.types.data_capture_config_summary.deserialize_aws_json_1_1(
                data["DataCaptureConfig"]
            )
        )
    if "EndpointStatus" in data:
        import aws_sdk_sagemaker.types.endpoint_status

        out["endpoint_status"] = (
            aws_sdk_sagemaker.types.endpoint_status.deserialize_aws_json_1_1(
                data["EndpointStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "MonitoringSchedules" in data:
        import aws_sdk_sagemaker.types.monitoring_schedule_list

        out["monitoring_schedules"] = (
            aws_sdk_sagemaker.types.monitoring_schedule_list.deserialize_aws_json_1_1(
                data["MonitoringSchedules"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ShadowProductionVariants" in data:
        import aws_sdk_sagemaker.types.production_variant_summary_list

        out["shadow_production_variants"] = (
            aws_sdk_sagemaker.types.production_variant_summary_list.deserialize_aws_json_1_1(
                data["ShadowProductionVariants"]
            )
        )
    return out
