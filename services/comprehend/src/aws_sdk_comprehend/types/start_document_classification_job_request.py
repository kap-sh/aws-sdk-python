"""Generated from Smithy shape ``com.amazonaws.comprehend#StartDocumentClassificationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.client_request_token_string
    import aws_sdk_comprehend.types.comprehend_flywheel_arn
    import aws_sdk_comprehend.types.document_classifier_arn
    import aws_sdk_comprehend.types.iam_role_arn
    import aws_sdk_comprehend.types.input_data_config
    import aws_sdk_comprehend.types.job_name
    import aws_sdk_comprehend.types.kms_key_id
    import aws_sdk_comprehend.types.output_data_config
    import aws_sdk_comprehend.types.tag_list
    import aws_sdk_comprehend.types.vpc_config


class StartDocumentClassificationJobRequest(TypedDict, closed=True):
    job_name: NotRequired["aws_sdk_comprehend.types.job_name.JobName"]
    """<p>The identifier of the job.</p>"""
    document_classifier_arn: NotRequired[
        "aws_sdk_comprehend.types.document_classifier_arn.DocumentClassifierArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the document classifier to use to process the job.</p>"""
    input_data_config: "aws_sdk_comprehend.types.input_data_config.InputDataConfig"
    """<p>Specifies the format and location of the input data for the job.</p>"""
    output_data_config: "aws_sdk_comprehend.types.output_data_config.OutputDataConfig"
    """<p>Specifies where to send the output files.</p>"""
    data_access_role_arn: "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.</p>"""
    volume_kms_key_id: NotRequired["aws_sdk_comprehend.types.kms_key_id.KmsKeyId"]
    r"""<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>"""
    vpc_config: NotRequired["aws_sdk_comprehend.types.vpc_config.VpcConfig"]
    r"""<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your document classification job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>"""
    tags: NotRequired["aws_sdk_comprehend.types.tag_list.TagList"]
    r"""<p>Tags to associate with the document classification job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department.</p>"""
    flywheel_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel associated with the model to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDocumentClassificationJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "document_classifier_arn" in value:
        out["DocumentClassifierArn"] = value["document_classifier_arn"]
    import aws_sdk_comprehend.types.input_data_config

    out["InputDataConfig"] = (
        aws_sdk_comprehend.types.input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    import aws_sdk_comprehend.types.output_data_config

    out["OutputDataConfig"] = (
        aws_sdk_comprehend.types.output_data_config.serialize_aws_json_1_1(
            value["output_data_config"]
        )
    )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import aws_sdk_comprehend.types.vpc_config

        out["VpcConfig"] = aws_sdk_comprehend.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "tags" in value:
        import aws_sdk_comprehend.types.tag_list

        out["Tags"] = aws_sdk_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDocumentClassificationJobRequest:
    out: StartDocumentClassificationJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "DocumentClassifierArn" in data:
        out["document_classifier_arn"] = data["DocumentClassifierArn"]
    if "InputDataConfig" in data:
        import aws_sdk_comprehend.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_comprehend.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartDocumentClassificationJobRequest.input_data_config required"
        )
    if "OutputDataConfig" in data:
        import aws_sdk_comprehend.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_comprehend.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartDocumentClassificationJobRequest.output_data_config required"
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartDocumentClassificationJobRequest.data_access_role_arn required"
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "VolumeKmsKeyId" in data:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if "VpcConfig" in data:
        import aws_sdk_comprehend.types.vpc_config

        out["vpc_config"] = (
            aws_sdk_comprehend.types.vpc_config.deserialize_aws_json_1_1(
                data["VpcConfig"]
            )
        )
    if "Tags" in data:
        import aws_sdk_comprehend.types.tag_list

        out["tags"] = aws_sdk_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out
