"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.exclude_features_attribute
    import aws_sdk_sagemaker.types.monitoring_time_offset_string
    import aws_sdk_sagemaker.types.probability_threshold_attribute
    import aws_sdk_sagemaker.types.processing_local_path
    import aws_sdk_sagemaker.types.processing_s3_data_distribution_type
    import aws_sdk_sagemaker.types.processing_s3_input_mode
    import aws_sdk_sagemaker.types.string


class EndpointInput(TypedDict, closed=True):
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p>An endpoint in customer's account which has enabled <code>DataCaptureConfig</code> enabled.</p>"""
    local_path: NotRequired[
        "aws_sdk_sagemaker.types.processing_local_path.ProcessingLocalPath"
    ]
    """<p>Path to the filesystem where the endpoint data is available to the container.</p>"""
    s3_input_mode: NotRequired[
        "aws_sdk_sagemaker.types.processing_s3_input_mode.ProcessingS3InputMode"
    ]
    """<p>Whether the <code>Pipe</code> or <code>File</code> is used as the input mode for transferring data for the monitoring job. <code>Pipe</code> mode is recommended for large datasets. <code>File</code> mode is useful for small files that fit in memory. Defaults to <code>File</code>.</p>"""
    s3_data_distribution_type: NotRequired[
        "aws_sdk_sagemaker.types.processing_s3_data_distribution_type.ProcessingS3DataDistributionType"
    ]
    """<p>Whether input data distributed in Amazon S3 is fully replicated or sharded by an Amazon S3 key. Defaults to <code>FullyReplicated</code> </p>"""
    features_attribute: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The attributes of the input data that are the input features.</p>"""
    inference_attribute: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The attribute of the input data that represents the ground truth label.</p>"""
    probability_attribute: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>In a classification problem, the attribute that represents the class probability.</p>"""
    probability_threshold_attribute: NotRequired[
        "aws_sdk_sagemaker.types.probability_threshold_attribute.ProbabilityThresholdAttribute"
    ]
    """<p>The threshold for the class probability to be evaluated as a positive result.</p>"""
    start_time_offset: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_time_offset_string.MonitoringTimeOffsetString"
    ]
    r"""<p>If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html\">Schedule Model Quality Monitoring Jobs</a>.</p>"""
    end_time_offset: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_time_offset_string.MonitoringTimeOffsetString"
    ]
    r"""<p>If specified, monitoring jobs substract this time from the end time. For information about using offsets for scheduling monitoring jobs, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html\">Schedule Model Quality Monitoring Jobs</a>.</p>"""
    exclude_features_attribute: NotRequired[
        "aws_sdk_sagemaker.types.exclude_features_attribute.ExcludeFeaturesAttribute"
    ]
    """<p>The attributes of the input data to exclude from the analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointInput) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    if "s3_input_mode" in value:
        import aws_sdk_sagemaker.types.processing_s3_input_mode

        out["S3InputMode"] = (
            aws_sdk_sagemaker.types.processing_s3_input_mode.serialize_aws_json_1_1(
                value["s3_input_mode"]
            )
        )
    if "s3_data_distribution_type" in value:
        import aws_sdk_sagemaker.types.processing_s3_data_distribution_type

        out["S3DataDistributionType"] = (
            aws_sdk_sagemaker.types.processing_s3_data_distribution_type.serialize_aws_json_1_1(
                value["s3_data_distribution_type"]
            )
        )
    if "features_attribute" in value:
        out["FeaturesAttribute"] = value["features_attribute"]
    if "inference_attribute" in value:
        out["InferenceAttribute"] = value["inference_attribute"]
    if "probability_attribute" in value:
        out["ProbabilityAttribute"] = value["probability_attribute"]
    if "probability_threshold_attribute" in value:
        out["ProbabilityThresholdAttribute"] = value["probability_threshold_attribute"]
    if "start_time_offset" in value:
        out["StartTimeOffset"] = value["start_time_offset"]
    if "end_time_offset" in value:
        out["EndTimeOffset"] = value["end_time_offset"]
    if "exclude_features_attribute" in value:
        out["ExcludeFeaturesAttribute"] = value["exclude_features_attribute"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointInput:
    out: EndpointInput = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "LocalPath" in data:
        out["local_path"] = data["LocalPath"]
    if "S3InputMode" in data:
        import aws_sdk_sagemaker.types.processing_s3_input_mode

        out["s3_input_mode"] = (
            aws_sdk_sagemaker.types.processing_s3_input_mode.deserialize_aws_json_1_1(
                data["S3InputMode"]
            )
        )
    if "S3DataDistributionType" in data:
        import aws_sdk_sagemaker.types.processing_s3_data_distribution_type

        out["s3_data_distribution_type"] = (
            aws_sdk_sagemaker.types.processing_s3_data_distribution_type.deserialize_aws_json_1_1(
                data["S3DataDistributionType"]
            )
        )
    if "FeaturesAttribute" in data:
        out["features_attribute"] = data["FeaturesAttribute"]
    if "InferenceAttribute" in data:
        out["inference_attribute"] = data["InferenceAttribute"]
    if "ProbabilityAttribute" in data:
        out["probability_attribute"] = data["ProbabilityAttribute"]
    if "ProbabilityThresholdAttribute" in data:
        out["probability_threshold_attribute"] = data["ProbabilityThresholdAttribute"]
    if "StartTimeOffset" in data:
        out["start_time_offset"] = data["StartTimeOffset"]
    if "EndTimeOffset" in data:
        out["end_time_offset"] = data["EndTimeOffset"]
    if "ExcludeFeaturesAttribute" in data:
        out["exclude_features_attribute"] = data["ExcludeFeaturesAttribute"]
    return out
