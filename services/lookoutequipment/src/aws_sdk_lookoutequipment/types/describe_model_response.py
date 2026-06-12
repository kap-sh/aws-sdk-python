"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.bounded_length_string
    import aws_sdk_lookoutequipment.types.data_pre_processing_configuration
    import aws_sdk_lookoutequipment.types.dataset_arn
    import aws_sdk_lookoutequipment.types.dataset_name
    import aws_sdk_lookoutequipment.types.iam_role_arn
    import aws_sdk_lookoutequipment.types.integer
    import aws_sdk_lookoutequipment.types.kms_key_arn
    import aws_sdk_lookoutequipment.types.labels_input_configuration
    import aws_sdk_lookoutequipment.types.model_arn
    import aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.model_quality
    import aws_sdk_lookoutequipment.types.model_status
    import aws_sdk_lookoutequipment.types.model_version
    import aws_sdk_lookoutequipment.types.model_version_arn
    import aws_sdk_lookoutequipment.types.model_version_status
    import aws_sdk_lookoutequipment.types.off_condition
    import aws_sdk_lookoutequipment.types.retraining_scheduler_status
    import aws_sdk_lookoutequipment.types.synthesized_json_inline_data_schema
    import aws_sdk_lookoutequipment.types.synthesized_json_model_metrics
    import aws_sdk_lookoutequipment.types.timestamp


class DescribeModelResponse(TypedDict):
    model_name: NotRequired["aws_sdk_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the machine learning model being described. </p>"""
    model_arn: NotRequired["aws_sdk_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the machine learning model being described. </p>"""
    dataset_name: NotRequired["aws_sdk_lookoutequipment.types.dataset_name.DatasetName"]
    """<p>The name of the dataset being used by the machine learning being described. </p>"""
    dataset_arn: NotRequired["aws_sdk_lookoutequipment.types.dataset_arn.DatasetArn"]
    """<p>The Amazon Resouce Name (ARN) of the dataset used to create the machine learning model being described. </p>"""
    schema: NotRequired[
        "aws_sdk_lookoutequipment.types.synthesized_json_inline_data_schema.SynthesizedJsonInlineDataSchema"
    ]
    """<p>A JSON description of the data that is in each time series dataset, including names, column names, and data types. </p>"""
    labels_input_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
    ]
    """<p>Specifies configuration information about the labels input, including its S3 location. </p>"""
    training_data_start_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p> Indicates the time reference in the dataset that was used to begin the subset of training data for the machine learning model. </p>"""
    training_data_end_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p> Indicates the time reference in the dataset that was used to end the subset of training data for the machine learning model. </p>"""
    evaluation_data_start_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p> Indicates the time reference in the dataset that was used to begin the subset of evaluation data for the machine learning model. </p>"""
    evaluation_data_end_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p> Indicates the time reference in the dataset that was used to end the subset of evaluation data for the machine learning model. </p>"""
    role_arn: NotRequired["aws_sdk_lookoutequipment.types.iam_role_arn.IamRoleArn"]
    """<p> The Amazon Resource Name (ARN) of a role with permission to access the data source for the machine learning model being described. </p>"""
    data_pre_processing_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.data_pre_processing_configuration.DataPreProcessingConfiguration"
    ]
    """<p>The configuration is the <code>TargetSamplingRate</code>, which is the sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the <code>TargetSamplingRate</code> is 1 minute.</p> <p>When providing a value for the <code>TargetSamplingRate</code>, you must attach the prefix \"PT\" to the rate you want. The value for a 1 second rate is therefore <i>PT1S</i>, the value for a 15 minute rate is <i>PT15M</i>, and the value for a 1 hour rate is <i>PT1H</i> </p>"""
    status: NotRequired["aws_sdk_lookoutequipment.types.model_status.ModelStatus"]
    """<p>Specifies the current status of the model being described. Status describes the status of the most recent action of the model. </p>"""
    training_execution_start_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the time at which the training of the machine learning model began. </p>"""
    training_execution_end_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the time at which the training of the machine learning model was completed. </p>"""
    failed_reason: NotRequired[
        "aws_sdk_lookoutequipment.types.bounded_length_string.BoundedLengthString"
    ]
    """<p>If the training of the machine learning model failed, this indicates the reason for that failure. </p>"""
    model_metrics: NotRequired[
        "aws_sdk_lookoutequipment.types.synthesized_json_model_metrics.SynthesizedJsonModelMetrics"
    ]
    """<p>The Model Metrics show an aggregated summary of the model's performance within the evaluation time range. This is the JSON content of the metrics created when evaluating the model. </p>"""
    last_updated_time: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the last time the machine learning model was updated. The type of update is not specified. </p>"""
    created_at: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the time and date at which the machine learning model was created. </p>"""
    server_side_kms_key_id: NotRequired[
        "aws_sdk_lookoutequipment.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>Provides the identifier of the KMS key used to encrypt model data by Amazon Lookout for Equipment. </p>"""
    off_condition: NotRequired[
        "aws_sdk_lookoutequipment.types.off_condition.OffCondition"
    ]
    """<p>Indicates that the asset associated with this sensor has been shut off. As long as this condition is met, Lookout for Equipment will not use data from this asset for training, evaluation, or inference.</p>"""
    source_model_version_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source model version. This field appears if the active model version was imported.</p>"""
    import_job_start_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the import job was started. This field appears if the active model version was imported.</p>"""
    import_job_end_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the import job was completed. This field appears if the active model version was imported.</p>"""
    active_model_version: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>The name of the model version used by the inference schedular when running a scheduled inference execution.</p>"""
    active_model_version_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model version used by the inference scheduler when running a scheduled inference execution.</p>"""
    model_version_activated_at: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date the active model version was activated.</p>"""
    previous_active_model_version: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>The model version that was set as the active model version prior to the current active model version.</p>"""
    previous_active_model_version_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The ARN of the model version that was set as the active model version prior to the current active model version.</p>"""
    previous_model_version_activated_at: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the previous active model version was activated.</p>"""
    prior_model_metrics: NotRequired[
        "aws_sdk_lookoutequipment.types.synthesized_json_model_metrics.SynthesizedJsonModelMetrics"
    ]
    """<p>If the model version was retrained, this field shows a summary of the performance of the prior model on the new training range. You can use the information in this JSON-formatted object to compare the new model version and the prior model version.</p>"""
    latest_scheduled_retraining_failed_reason: NotRequired[
        "aws_sdk_lookoutequipment.types.bounded_length_string.BoundedLengthString"
    ]
    """<p>If the model version was generated by retraining and the training failed, this indicates the reason for that failure. </p>"""
    latest_scheduled_retraining_status: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version_status.ModelVersionStatus"
    ]
    """<p>Indicates the status of the most recent scheduled retraining run. </p>"""
    latest_scheduled_retraining_model_version: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>Indicates the most recent model version that was generated by retraining. </p>"""
    latest_scheduled_retraining_start_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the start time of the most recent scheduled retraining run. </p>"""
    latest_scheduled_retraining_available_data_in_days: NotRequired[
        "aws_sdk_lookoutequipment.types.integer.Integer"
    ]
    """<p>Indicates the number of days of data used in the most recent scheduled retraining run. </p>"""
    next_scheduled_retraining_start_date: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the date and time that the next scheduled retraining run will start on. Lookout for Equipment truncates the time you provide to the nearest UTC day.</p>"""
    accumulated_inference_data_start_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the start time of the inference data that has been accumulated. </p>"""
    accumulated_inference_data_end_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the end time of the inference data that has been accumulated. </p>"""
    retraining_scheduler_status: NotRequired[
        "aws_sdk_lookoutequipment.types.retraining_scheduler_status.RetrainingSchedulerStatus"
    ]
    """<p>Indicates the status of the retraining scheduler. </p>"""
    model_diagnostics_output_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration.ModelDiagnosticsOutputConfiguration"
    ]
    """<p>Configuration information for the model's pointwise model diagnostics.</p>"""
    model_quality: NotRequired[
        "aws_sdk_lookoutequipment.types.model_quality.ModelQuality"
    ]
    """<p>Provides a quality assessment for a model that uses labels. If Lookout for Equipment determines that the model quality is poor based on training metrics, the value is <code>POOR_QUALITY_DETECTED</code>. Otherwise, the value is <code>QUALITY_THRESHOLD_MET</code>.</p> <p>If the model is unlabeled, the model quality can't be assessed and the value of <code>ModelQuality</code> is <code>CANNOT_DETERMINE_QUALITY</code>. In this situation, you can get a model quality assessment by adding labels to the input dataset and retraining the model.</p> <p>For information about using labels with your models, see <a href=\"https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-labeling.html\">Understanding labeling</a>.</p> <p>For information about improving the quality of a model, see <a href=\"https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/best-practices.html\">Best practices with Amazon Lookout for Equipment</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeModelResponse) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "schema" in value:
        out["Schema"] = value["schema"]
    if "labels_input_configuration" in value:
        import aws_sdk_lookoutequipment.types.labels_input_configuration

        out["LabelsInputConfiguration"] = (
            aws_sdk_lookoutequipment.types.labels_input_configuration.serialize_aws_json_1_0(
                value["labels_input_configuration"]
            )
        )
    if "training_data_start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["TrainingDataStartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["training_data_start_time"]
            )
        )
    if "training_data_end_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["TrainingDataEndTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["training_data_end_time"]
            )
        )
    if "evaluation_data_start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["EvaluationDataStartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["evaluation_data_start_time"]
            )
        )
    if "evaluation_data_end_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["EvaluationDataEndTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["evaluation_data_end_time"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "data_pre_processing_configuration" in value:
        import aws_sdk_lookoutequipment.types.data_pre_processing_configuration

        out["DataPreProcessingConfiguration"] = (
            aws_sdk_lookoutequipment.types.data_pre_processing_configuration.serialize_aws_json_1_0(
                value["data_pre_processing_configuration"]
            )
        )
    if "status" in value:
        import aws_sdk_lookoutequipment.types.model_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.model_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "training_execution_start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["TrainingExecutionStartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["training_execution_start_time"]
            )
        )
    if "training_execution_end_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["TrainingExecutionEndTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["training_execution_end_time"]
            )
        )
    if "failed_reason" in value:
        out["FailedReason"] = value["failed_reason"]
    if "model_metrics" in value:
        out["ModelMetrics"] = value["model_metrics"]
    if "last_updated_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["LastUpdatedTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["last_updated_time"]
            )
        )
    if "created_at" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["CreatedAt"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "server_side_kms_key_id" in value:
        out["ServerSideKmsKeyId"] = value["server_side_kms_key_id"]
    if "off_condition" in value:
        out["OffCondition"] = value["off_condition"]
    if "source_model_version_arn" in value:
        out["SourceModelVersionArn"] = value["source_model_version_arn"]
    if "import_job_start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["ImportJobStartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["import_job_start_time"]
            )
        )
    if "import_job_end_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["ImportJobEndTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["import_job_end_time"]
            )
        )
    if "active_model_version" in value:
        out["ActiveModelVersion"] = value["active_model_version"]
    if "active_model_version_arn" in value:
        out["ActiveModelVersionArn"] = value["active_model_version_arn"]
    if "model_version_activated_at" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["ModelVersionActivatedAt"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["model_version_activated_at"]
            )
        )
    if "previous_active_model_version" in value:
        out["PreviousActiveModelVersion"] = value["previous_active_model_version"]
    if "previous_active_model_version_arn" in value:
        out["PreviousActiveModelVersionArn"] = value[
            "previous_active_model_version_arn"
        ]
    if "previous_model_version_activated_at" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["PreviousModelVersionActivatedAt"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["previous_model_version_activated_at"]
            )
        )
    if "prior_model_metrics" in value:
        out["PriorModelMetrics"] = value["prior_model_metrics"]
    if "latest_scheduled_retraining_failed_reason" in value:
        out["LatestScheduledRetrainingFailedReason"] = value[
            "latest_scheduled_retraining_failed_reason"
        ]
    if "latest_scheduled_retraining_status" in value:
        import aws_sdk_lookoutequipment.types.model_version_status

        out["LatestScheduledRetrainingStatus"] = (
            aws_sdk_lookoutequipment.types.model_version_status.serialize_aws_json_1_0(
                value["latest_scheduled_retraining_status"]
            )
        )
    if "latest_scheduled_retraining_model_version" in value:
        out["LatestScheduledRetrainingModelVersion"] = value[
            "latest_scheduled_retraining_model_version"
        ]
    if "latest_scheduled_retraining_start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["LatestScheduledRetrainingStartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["latest_scheduled_retraining_start_time"]
            )
        )
    if "latest_scheduled_retraining_available_data_in_days" in value:
        out["LatestScheduledRetrainingAvailableDataInDays"] = value[
            "latest_scheduled_retraining_available_data_in_days"
        ]
    if "next_scheduled_retraining_start_date" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["NextScheduledRetrainingStartDate"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["next_scheduled_retraining_start_date"]
            )
        )
    if "accumulated_inference_data_start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["AccumulatedInferenceDataStartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["accumulated_inference_data_start_time"]
            )
        )
    if "accumulated_inference_data_end_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["AccumulatedInferenceDataEndTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["accumulated_inference_data_end_time"]
            )
        )
    if "retraining_scheduler_status" in value:
        import aws_sdk_lookoutequipment.types.retraining_scheduler_status

        out["RetrainingSchedulerStatus"] = (
            aws_sdk_lookoutequipment.types.retraining_scheduler_status.serialize_aws_json_1_0(
                value["retraining_scheduler_status"]
            )
        )
    if "model_diagnostics_output_configuration" in value:
        import aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration

        out["ModelDiagnosticsOutputConfiguration"] = (
            aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration.serialize_aws_json_1_0(
                value["model_diagnostics_output_configuration"]
            )
        )
    if "model_quality" in value:
        import aws_sdk_lookoutequipment.types.model_quality

        out["ModelQuality"] = (
            aws_sdk_lookoutequipment.types.model_quality.serialize_aws_json_1_0(
                value["model_quality"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeModelResponse:
    out: DescribeModelResponse = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    if "Schema" in data:
        out["schema"] = data["Schema"]
    if "LabelsInputConfiguration" in data:
        import aws_sdk_lookoutequipment.types.labels_input_configuration

        out["labels_input_configuration"] = (
            aws_sdk_lookoutequipment.types.labels_input_configuration.deserialize_aws_json_1_0(
                data["LabelsInputConfiguration"]
            )
        )
    if "TrainingDataStartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["training_data_start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["TrainingDataStartTime"]
            )
        )
    if "TrainingDataEndTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["training_data_end_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["TrainingDataEndTime"]
            )
        )
    if "EvaluationDataStartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["evaluation_data_start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["EvaluationDataStartTime"]
            )
        )
    if "EvaluationDataEndTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["evaluation_data_end_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["EvaluationDataEndTime"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "DataPreProcessingConfiguration" in data:
        import aws_sdk_lookoutequipment.types.data_pre_processing_configuration

        out["data_pre_processing_configuration"] = (
            aws_sdk_lookoutequipment.types.data_pre_processing_configuration.deserialize_aws_json_1_0(
                data["DataPreProcessingConfiguration"]
            )
        )
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.model_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.model_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "TrainingExecutionStartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["training_execution_start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["TrainingExecutionStartTime"]
            )
        )
    if "TrainingExecutionEndTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["training_execution_end_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["TrainingExecutionEndTime"]
            )
        )
    if "FailedReason" in data:
        out["failed_reason"] = data["FailedReason"]
    if "ModelMetrics" in data:
        out["model_metrics"] = data["ModelMetrics"]
    if "LastUpdatedTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTime"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["created_at"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "ServerSideKmsKeyId" in data:
        out["server_side_kms_key_id"] = data["ServerSideKmsKeyId"]
    if "OffCondition" in data:
        out["off_condition"] = data["OffCondition"]
    if "SourceModelVersionArn" in data:
        out["source_model_version_arn"] = data["SourceModelVersionArn"]
    if "ImportJobStartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["import_job_start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["ImportJobStartTime"]
            )
        )
    if "ImportJobEndTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["import_job_end_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["ImportJobEndTime"]
            )
        )
    if "ActiveModelVersion" in data:
        out["active_model_version"] = data["ActiveModelVersion"]
    if "ActiveModelVersionArn" in data:
        out["active_model_version_arn"] = data["ActiveModelVersionArn"]
    if "ModelVersionActivatedAt" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["model_version_activated_at"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["ModelVersionActivatedAt"]
            )
        )
    if "PreviousActiveModelVersion" in data:
        out["previous_active_model_version"] = data["PreviousActiveModelVersion"]
    if "PreviousActiveModelVersionArn" in data:
        out["previous_active_model_version_arn"] = data["PreviousActiveModelVersionArn"]
    if "PreviousModelVersionActivatedAt" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["previous_model_version_activated_at"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["PreviousModelVersionActivatedAt"]
            )
        )
    if "PriorModelMetrics" in data:
        out["prior_model_metrics"] = data["PriorModelMetrics"]
    if "LatestScheduledRetrainingFailedReason" in data:
        out["latest_scheduled_retraining_failed_reason"] = data[
            "LatestScheduledRetrainingFailedReason"
        ]
    if "LatestScheduledRetrainingStatus" in data:
        import aws_sdk_lookoutequipment.types.model_version_status

        out["latest_scheduled_retraining_status"] = (
            aws_sdk_lookoutequipment.types.model_version_status.deserialize_aws_json_1_0(
                data["LatestScheduledRetrainingStatus"]
            )
        )
    if "LatestScheduledRetrainingModelVersion" in data:
        out["latest_scheduled_retraining_model_version"] = data[
            "LatestScheduledRetrainingModelVersion"
        ]
    if "LatestScheduledRetrainingStartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["latest_scheduled_retraining_start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["LatestScheduledRetrainingStartTime"]
            )
        )
    if "LatestScheduledRetrainingAvailableDataInDays" in data:
        out["latest_scheduled_retraining_available_data_in_days"] = data[
            "LatestScheduledRetrainingAvailableDataInDays"
        ]
    if "NextScheduledRetrainingStartDate" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["next_scheduled_retraining_start_date"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["NextScheduledRetrainingStartDate"]
            )
        )
    if "AccumulatedInferenceDataStartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["accumulated_inference_data_start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["AccumulatedInferenceDataStartTime"]
            )
        )
    if "AccumulatedInferenceDataEndTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["accumulated_inference_data_end_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["AccumulatedInferenceDataEndTime"]
            )
        )
    if "RetrainingSchedulerStatus" in data:
        import aws_sdk_lookoutequipment.types.retraining_scheduler_status

        out["retraining_scheduler_status"] = (
            aws_sdk_lookoutequipment.types.retraining_scheduler_status.deserialize_aws_json_1_0(
                data["RetrainingSchedulerStatus"]
            )
        )
    if "ModelDiagnosticsOutputConfiguration" in data:
        import aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration

        out["model_diagnostics_output_configuration"] = (
            aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration.deserialize_aws_json_1_0(
                data["ModelDiagnosticsOutputConfiguration"]
            )
        )
    if "ModelQuality" in data:
        import aws_sdk_lookoutequipment.types.model_quality

        out["model_quality"] = (
            aws_sdk_lookoutequipment.types.model_quality.deserialize_aws_json_1_0(
                data["ModelQuality"]
            )
        )
    return out
