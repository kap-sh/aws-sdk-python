"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectVersionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.customization_feature
    import capo_rekognition.types.customization_feature_config
    import capo_rekognition.types.date_time
    import capo_rekognition.types.evaluation_result
    import capo_rekognition.types.ground_truth_manifest
    import capo_rekognition.types.inference_units
    import capo_rekognition.types.kms_key_id
    import capo_rekognition.types.output_config
    import capo_rekognition.types.project_version_arn
    import capo_rekognition.types.project_version_status
    import capo_rekognition.types.status_message
    import capo_rekognition.types.string
    import capo_rekognition.types.testing_data_result
    import capo_rekognition.types.training_data_result
    import capo_rekognition.types.u_long
    import capo_rekognition.types.version_description


class ProjectVersionDescription(TypedDict, closed=True):
    project_version_arn: NotRequired[
        "capo_rekognition.types.project_version_arn.ProjectVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the project version. </p>"""
    creation_timestamp: NotRequired["capo_rekognition.types.date_time.DateTime"]
    """<p>The Unix datetime for the date and time that training started.</p>"""
    min_inference_units: NotRequired[
        "capo_rekognition.types.inference_units.InferenceUnits"
    ]
    """<p>The minimum number of inference units used by the model. Applies only to Custom Labels projects. For more information, see <a>StartProjectVersion</a>.</p>"""
    status: NotRequired[
        "capo_rekognition.types.project_version_status.ProjectVersionStatus"
    ]
    """<p>The current status of the model version.</p>"""
    status_message: NotRequired["capo_rekognition.types.status_message.StatusMessage"]
    """<p>A descriptive message for an error or warning that occurred.</p>"""
    billable_training_time_in_seconds: NotRequired[
        "capo_rekognition.types.u_long.ULong"
    ]
    """<p>The duration, in seconds, that you were billed for a successful training of the model version. This value is only returned if the model version has been successfully trained.</p>"""
    training_end_timestamp: NotRequired["capo_rekognition.types.date_time.DateTime"]
    """<p>The Unix date and time that training of the model ended.</p>"""
    output_config: NotRequired["capo_rekognition.types.output_config.OutputConfig"]
    """<p>The location where training results are saved.</p>"""
    training_data_result: NotRequired[
        "capo_rekognition.types.training_data_result.TrainingDataResult"
    ]
    """<p>Contains information about the training results.</p>"""
    testing_data_result: NotRequired[
        "capo_rekognition.types.testing_data_result.TestingDataResult"
    ]
    """<p>Contains information about the testing results.</p>"""
    evaluation_result: NotRequired[
        "capo_rekognition.types.evaluation_result.EvaluationResult"
    ]
    """<p>The training results. <code>EvaluationResult</code> is only returned if training is successful.</p>"""
    manifest_summary: NotRequired[
        "capo_rekognition.types.ground_truth_manifest.GroundTruthManifest"
    ]
    """<p>The location of the summary manifest. The summary manifest provides aggregate data validation results for the training and test datasets.</p>"""
    kms_key_id: NotRequired["capo_rekognition.types.kms_key_id.KmsKeyId"]
    """<p>The identifer for the AWS Key Management Service key (AWS KMS key) that was used to encrypt the model during training. </p>"""
    max_inference_units: NotRequired[
        "capo_rekognition.types.inference_units.InferenceUnits"
    ]
    """<p>The maximum number of inference units Amazon Rekognition uses to auto-scale the model. Applies only to Custom Labels projects. For more information, see <a>StartProjectVersion</a>.</p>"""
    source_project_version_arn: NotRequired[
        "capo_rekognition.types.project_version_arn.ProjectVersionArn"
    ]
    """<p>If the model version was copied from a different project, <code>SourceProjectVersionArn</code> contains the ARN of the source model version. </p>"""
    version_description: NotRequired[
        "capo_rekognition.types.version_description.VersionDescription"
    ]
    """<p>A user-provided description of the project version.</p>"""
    feature: NotRequired[
        "capo_rekognition.types.customization_feature.CustomizationFeature"
    ]
    """<p>The feature that was customized.</p>"""
    base_model_version: NotRequired["capo_rekognition.types.string.String"]
    """<p>The base detection model version used to create the project version.</p>"""
    feature_config: NotRequired[
        "capo_rekognition.types.customization_feature_config.CustomizationFeatureConfig"
    ]
    """<p>Feature specific configuration that was applied during training.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectVersionDescription) -> dict:
    out: dict = {}
    if "project_version_arn" in value:
        out["ProjectVersionArn"] = value["project_version_arn"]
    if "creation_timestamp" in value:
        import capo_rekognition.types.date_time

        out["CreationTimestamp"] = (
            capo_rekognition.types.date_time.serialize_aws_json_1_1(
                value["creation_timestamp"]
            )
        )
    if "min_inference_units" in value:
        out["MinInferenceUnits"] = value["min_inference_units"]
    if "status" in value:
        import capo_rekognition.types.project_version_status

        out["Status"] = (
            capo_rekognition.types.project_version_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "billable_training_time_in_seconds" in value:
        out["BillableTrainingTimeInSeconds"] = value[
            "billable_training_time_in_seconds"
        ]
    if "training_end_timestamp" in value:
        import capo_rekognition.types.date_time

        out["TrainingEndTimestamp"] = (
            capo_rekognition.types.date_time.serialize_aws_json_1_1(
                value["training_end_timestamp"]
            )
        )
    if "output_config" in value:
        import capo_rekognition.types.output_config

        out["OutputConfig"] = (
            capo_rekognition.types.output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "training_data_result" in value:
        import capo_rekognition.types.training_data_result

        out["TrainingDataResult"] = (
            capo_rekognition.types.training_data_result.serialize_aws_json_1_1(
                value["training_data_result"]
            )
        )
    if "testing_data_result" in value:
        import capo_rekognition.types.testing_data_result

        out["TestingDataResult"] = (
            capo_rekognition.types.testing_data_result.serialize_aws_json_1_1(
                value["testing_data_result"]
            )
        )
    if "evaluation_result" in value:
        import capo_rekognition.types.evaluation_result

        out["EvaluationResult"] = (
            capo_rekognition.types.evaluation_result.serialize_aws_json_1_1(
                value["evaluation_result"]
            )
        )
    if "manifest_summary" in value:
        import capo_rekognition.types.ground_truth_manifest

        out["ManifestSummary"] = (
            capo_rekognition.types.ground_truth_manifest.serialize_aws_json_1_1(
                value["manifest_summary"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "max_inference_units" in value:
        out["MaxInferenceUnits"] = value["max_inference_units"]
    if "source_project_version_arn" in value:
        out["SourceProjectVersionArn"] = value["source_project_version_arn"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "feature" in value:
        import capo_rekognition.types.customization_feature

        out["Feature"] = (
            capo_rekognition.types.customization_feature.serialize_aws_json_1_1(
                value["feature"]
            )
        )
    if "base_model_version" in value:
        out["BaseModelVersion"] = value["base_model_version"]
    if "feature_config" in value:
        import capo_rekognition.types.customization_feature_config

        out["FeatureConfig"] = (
            capo_rekognition.types.customization_feature_config.serialize_aws_json_1_1(
                value["feature_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectVersionDescription:
    out: ProjectVersionDescription = {}  # type: ignore[typeddict-item]
    if "ProjectVersionArn" in data:
        out["project_version_arn"] = data["ProjectVersionArn"]
    if "CreationTimestamp" in data:
        import capo_rekognition.types.date_time

        out["creation_timestamp"] = (
            capo_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CreationTimestamp"]
            )
        )
    if "MinInferenceUnits" in data:
        out["min_inference_units"] = data["MinInferenceUnits"]
    if "Status" in data:
        import capo_rekognition.types.project_version_status

        out["status"] = (
            capo_rekognition.types.project_version_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "BillableTrainingTimeInSeconds" in data:
        out["billable_training_time_in_seconds"] = data["BillableTrainingTimeInSeconds"]
    if "TrainingEndTimestamp" in data:
        import capo_rekognition.types.date_time

        out["training_end_timestamp"] = (
            capo_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["TrainingEndTimestamp"]
            )
        )
    if "OutputConfig" in data:
        import capo_rekognition.types.output_config

        out["output_config"] = (
            capo_rekognition.types.output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "TrainingDataResult" in data:
        import capo_rekognition.types.training_data_result

        out["training_data_result"] = (
            capo_rekognition.types.training_data_result.deserialize_aws_json_1_1(
                data["TrainingDataResult"]
            )
        )
    if "TestingDataResult" in data:
        import capo_rekognition.types.testing_data_result

        out["testing_data_result"] = (
            capo_rekognition.types.testing_data_result.deserialize_aws_json_1_1(
                data["TestingDataResult"]
            )
        )
    if "EvaluationResult" in data:
        import capo_rekognition.types.evaluation_result

        out["evaluation_result"] = (
            capo_rekognition.types.evaluation_result.deserialize_aws_json_1_1(
                data["EvaluationResult"]
            )
        )
    if "ManifestSummary" in data:
        import capo_rekognition.types.ground_truth_manifest

        out["manifest_summary"] = (
            capo_rekognition.types.ground_truth_manifest.deserialize_aws_json_1_1(
                data["ManifestSummary"]
            )
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "MaxInferenceUnits" in data:
        out["max_inference_units"] = data["MaxInferenceUnits"]
    if "SourceProjectVersionArn" in data:
        out["source_project_version_arn"] = data["SourceProjectVersionArn"]
    if "VersionDescription" in data:
        out["version_description"] = data["VersionDescription"]
    if "Feature" in data:
        import capo_rekognition.types.customization_feature

        out["feature"] = (
            capo_rekognition.types.customization_feature.deserialize_aws_json_1_1(
                data["Feature"]
            )
        )
    if "BaseModelVersion" in data:
        out["base_model_version"] = data["BaseModelVersion"]
    if "FeatureConfig" in data:
        import capo_rekognition.types.customization_feature_config

        out["feature_config"] = (
            capo_rekognition.types.customization_feature_config.deserialize_aws_json_1_1(
                data["FeatureConfig"]
            )
        )
    return out
