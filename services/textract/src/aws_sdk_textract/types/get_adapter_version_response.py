"""Generated from Smithy shape ``com.amazonaws.textract#GetAdapterVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_id
    import aws_sdk_textract.types.adapter_version
    import aws_sdk_textract.types.adapter_version_dataset_config
    import aws_sdk_textract.types.adapter_version_evaluation_metrics
    import aws_sdk_textract.types.adapter_version_status
    import aws_sdk_textract.types.adapter_version_status_message
    import aws_sdk_textract.types.date_time
    import aws_sdk_textract.types.feature_types
    import aws_sdk_textract.types.kms_key_id
    import aws_sdk_textract.types.output_config
    import aws_sdk_textract.types.tag_map


class GetAdapterVersionResponse(TypedDict):
    adapter_id: NotRequired["aws_sdk_textract.types.adapter_id.AdapterId"]
    """<p>A string containing a unique ID for the adapter version being retrieved.</p>"""
    adapter_version: NotRequired[
        "aws_sdk_textract.types.adapter_version.AdapterVersion"
    ]
    """<p>A string containing the adapter version that has been retrieved.</p>"""
    creation_time: NotRequired["aws_sdk_textract.types.date_time.DateTime"]
    """<p>The time that the adapter version was created.</p>"""
    feature_types: NotRequired["aws_sdk_textract.types.feature_types.FeatureTypes"]
    """<p>List of the targeted feature types for the requested adapter version.</p>"""
    status: NotRequired[
        "aws_sdk_textract.types.adapter_version_status.AdapterVersionStatus"
    ]
    """<p>The status of the adapter version that has been requested.</p>"""
    status_message: NotRequired[
        "aws_sdk_textract.types.adapter_version_status_message.AdapterVersionStatusMessage"
    ]
    """<p>A message that describes the status of the requested adapter version.</p>"""
    dataset_config: NotRequired[
        "aws_sdk_textract.types.adapter_version_dataset_config.AdapterVersionDatasetConfig"
    ]
    """<p>Specifies a dataset used to train a new adapter version. Takes a ManifestS3Objec as the value.</p>"""
    kms_key_id: NotRequired["aws_sdk_textract.types.kms_key_id.KMSKeyId"]
    """<p>The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt your documents.</p>"""
    output_config: NotRequired["aws_sdk_textract.types.output_config.OutputConfig"]
    evaluation_metrics: NotRequired[
        "aws_sdk_textract.types.adapter_version_evaluation_metrics.AdapterVersionEvaluationMetrics"
    ]
    """<p>The evaluation metrics (F1 score, Precision, and Recall) for the requested version, grouped by baseline metrics and adapter version.</p>"""
    tags: NotRequired["aws_sdk_textract.types.tag_map.TagMap"]
    """<p>A set of tags (key-value pairs) that are associated with the adapter version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdapterVersionResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_version" in value:
        out["AdapterVersion"] = value["adapter_version"]
    if "creation_time" in value:
        import aws_sdk_textract.types.date_time

        out["CreationTime"] = aws_sdk_textract.types.date_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "feature_types" in value:
        import aws_sdk_textract.types.feature_types

        out["FeatureTypes"] = (
            aws_sdk_textract.types.feature_types.serialize_aws_json_1_1(
                value["feature_types"]
            )
        )
    if "status" in value:
        import aws_sdk_textract.types.adapter_version_status

        out["Status"] = (
            aws_sdk_textract.types.adapter_version_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "dataset_config" in value:
        import aws_sdk_textract.types.adapter_version_dataset_config

        out["DatasetConfig"] = (
            aws_sdk_textract.types.adapter_version_dataset_config.serialize_aws_json_1_1(
                value["dataset_config"]
            )
        )
    if "kms_key_id" in value:
        out["KMSKeyId"] = value["kms_key_id"]
    if "output_config" in value:
        import aws_sdk_textract.types.output_config

        out["OutputConfig"] = (
            aws_sdk_textract.types.output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "evaluation_metrics" in value:
        import aws_sdk_textract.types.adapter_version_evaluation_metrics

        out["EvaluationMetrics"] = (
            aws_sdk_textract.types.adapter_version_evaluation_metrics.serialize_aws_json_1_1(
                value["evaluation_metrics"]
            )
        )
    if "tags" in value:
        import aws_sdk_textract.types.tag_map

        out["Tags"] = aws_sdk_textract.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdapterVersionResponse:
    out: GetAdapterVersionResponse = {}  # type: ignore[typeddict-item]
    if "AdapterId" in data:
        out["adapter_id"] = data["AdapterId"]
    if "AdapterVersion" in data:
        out["adapter_version"] = data["AdapterVersion"]
    if "CreationTime" in data:
        import aws_sdk_textract.types.date_time

        out["creation_time"] = (
            aws_sdk_textract.types.date_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "FeatureTypes" in data:
        import aws_sdk_textract.types.feature_types

        out["feature_types"] = (
            aws_sdk_textract.types.feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    if "Status" in data:
        import aws_sdk_textract.types.adapter_version_status

        out["status"] = (
            aws_sdk_textract.types.adapter_version_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "DatasetConfig" in data:
        import aws_sdk_textract.types.adapter_version_dataset_config

        out["dataset_config"] = (
            aws_sdk_textract.types.adapter_version_dataset_config.deserialize_aws_json_1_1(
                data["DatasetConfig"]
            )
        )
    if "KMSKeyId" in data:
        out["kms_key_id"] = data["KMSKeyId"]
    if "OutputConfig" in data:
        import aws_sdk_textract.types.output_config

        out["output_config"] = (
            aws_sdk_textract.types.output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "EvaluationMetrics" in data:
        import aws_sdk_textract.types.adapter_version_evaluation_metrics

        out["evaluation_metrics"] = (
            aws_sdk_textract.types.adapter_version_evaluation_metrics.deserialize_aws_json_1_1(
                data["EvaluationMetrics"]
            )
        )
    if "Tags" in data:
        import aws_sdk_textract.types.tag_map

        out["tags"] = aws_sdk_textract.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
