"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.any_length_string
    import aws_sdk_comprehend.types.comprehend_flywheel_arn
    import aws_sdk_comprehend.types.entity_recognizer_arn
    import aws_sdk_comprehend.types.entity_recognizer_input_data_config
    import aws_sdk_comprehend.types.entity_recognizer_metadata
    import aws_sdk_comprehend.types.entity_recognizer_output_data_config
    import aws_sdk_comprehend.types.iam_role_arn
    import aws_sdk_comprehend.types.kms_key_id
    import aws_sdk_comprehend.types.language_code
    import aws_sdk_comprehend.types.model_status
    import aws_sdk_comprehend.types.timestamp
    import aws_sdk_comprehend.types.version_name
    import aws_sdk_comprehend.types.vpc_config


class EntityRecognizerProperties(TypedDict, closed=True):
    entity_recognizer_arn: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_arn.EntityRecognizerArn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the entity recognizer.</p>"""
    language_code: NotRequired["aws_sdk_comprehend.types.language_code.LanguageCode"]
    r"""<p> The language of the input documents. All documents must be in the same language. Only English (\"en\") is currently supported.</p>"""
    status: NotRequired["aws_sdk_comprehend.types.model_status.ModelStatus"]
    """<p>Provides the status of the entity recognizer.</p>"""
    message: NotRequired["aws_sdk_comprehend.types.any_length_string.AnyLengthString"]
    """<p> A description of the status of the recognizer.</p>"""
    submit_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the recognizer was submitted for processing.</p>"""
    end_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the recognizer creation completed.</p>"""
    training_start_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time that training of the entity recognizer started.</p>"""
    training_end_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time that training of the entity recognizer was completed.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_input_data_config.EntityRecognizerInputDataConfig"
    ]
    """<p>The input data properties of an entity recognizer.</p>"""
    recognizer_metadata: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_metadata.EntityRecognizerMetadata"
    ]
    """<p> Provides information about an entity recognizer.</p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    volume_kms_key_id: NotRequired["aws_sdk_comprehend.types.kms_key_id.KmsKeyId"]
    r"""<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>"""
    vpc_config: NotRequired["aws_sdk_comprehend.types.vpc_config.VpcConfig"]
    r"""<p> Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your custom entity recognizer. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>"""
    model_kms_key_id: NotRequired["aws_sdk_comprehend.types.kms_key_id.KmsKeyId"]
    r"""<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>"""
    version_name: NotRequired["aws_sdk_comprehend.types.version_name.VersionName"]
    """<p>The version name you assigned to the entity recognizer.</p>"""
    source_model_arn: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_arn.EntityRecognizerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source model. This model was imported from a different Amazon Web Services account to create the entity recognizer model in your Amazon Web Services account.</p>"""
    flywheel_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel</p>"""
    output_data_config: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_output_data_config.EntityRecognizerOutputDataConfig"
    ]
    """<p>Output data configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerProperties) -> dict:
    out: dict = {}
    if "entity_recognizer_arn" in value:
        out["EntityRecognizerArn"] = value["entity_recognizer_arn"]
    if "language_code" in value:
        import aws_sdk_comprehend.types.language_code

        out["LanguageCode"] = (
            aws_sdk_comprehend.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "status" in value:
        import aws_sdk_comprehend.types.model_status

        out["Status"] = aws_sdk_comprehend.types.model_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "submit_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["SubmitTime"] = aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["submit_time"]
        )
    if "end_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["EndTime"] = aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "training_start_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["TrainingStartTime"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["training_start_time"]
            )
        )
    if "training_end_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["TrainingEndTime"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["training_end_time"]
            )
        )
    if "input_data_config" in value:
        import aws_sdk_comprehend.types.entity_recognizer_input_data_config

        out["InputDataConfig"] = (
            aws_sdk_comprehend.types.entity_recognizer_input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "recognizer_metadata" in value:
        import aws_sdk_comprehend.types.entity_recognizer_metadata

        out["RecognizerMetadata"] = (
            aws_sdk_comprehend.types.entity_recognizer_metadata.serialize_aws_json_1_1(
                value["recognizer_metadata"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import aws_sdk_comprehend.types.vpc_config

        out["VpcConfig"] = aws_sdk_comprehend.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "model_kms_key_id" in value:
        out["ModelKmsKeyId"] = value["model_kms_key_id"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "source_model_arn" in value:
        out["SourceModelArn"] = value["source_model_arn"]
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "output_data_config" in value:
        import aws_sdk_comprehend.types.entity_recognizer_output_data_config

        out["OutputDataConfig"] = (
            aws_sdk_comprehend.types.entity_recognizer_output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerProperties:
    out: EntityRecognizerProperties = {}  # type: ignore[typeddict-item]
    if "EntityRecognizerArn" in data:
        out["entity_recognizer_arn"] = data["EntityRecognizerArn"]
    if "LanguageCode" in data:
        import aws_sdk_comprehend.types.language_code

        out["language_code"] = (
            aws_sdk_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if "Status" in data:
        import aws_sdk_comprehend.types.model_status

        out["status"] = aws_sdk_comprehend.types.model_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "SubmitTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["submit_time"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["end_time"] = aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "TrainingStartTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["training_start_time"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingStartTime"]
            )
        )
    if "TrainingEndTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["training_end_time"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingEndTime"]
            )
        )
    if "InputDataConfig" in data:
        import aws_sdk_comprehend.types.entity_recognizer_input_data_config

        out["input_data_config"] = (
            aws_sdk_comprehend.types.entity_recognizer_input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if "RecognizerMetadata" in data:
        import aws_sdk_comprehend.types.entity_recognizer_metadata

        out["recognizer_metadata"] = (
            aws_sdk_comprehend.types.entity_recognizer_metadata.deserialize_aws_json_1_1(
                data["RecognizerMetadata"]
            )
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "VolumeKmsKeyId" in data:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if "VpcConfig" in data:
        import aws_sdk_comprehend.types.vpc_config

        out["vpc_config"] = (
            aws_sdk_comprehend.types.vpc_config.deserialize_aws_json_1_1(
                data["VpcConfig"]
            )
        )
    if "ModelKmsKeyId" in data:
        out["model_kms_key_id"] = data["ModelKmsKeyId"]
    if "VersionName" in data:
        out["version_name"] = data["VersionName"]
    if "SourceModelArn" in data:
        out["source_model_arn"] = data["SourceModelArn"]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    if "OutputDataConfig" in data:
        import aws_sdk_comprehend.types.entity_recognizer_output_data_config

        out["output_data_config"] = (
            aws_sdk_comprehend.types.entity_recognizer_output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    return out
