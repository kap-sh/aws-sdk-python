"""Generated from Smithy shape ``com.amazonaws.comprehend#StartTargetedSentimentDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.client_request_token_string
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.input_data_config
    import capo_comprehend.types.job_name
    import capo_comprehend.types.kms_key_id
    import capo_comprehend.types.language_code
    import capo_comprehend.types.output_data_config
    import capo_comprehend.types.tag_list
    import capo_comprehend.types.vpc_config


class StartTargetedSentimentDetectionJobRequest(TypedDict, closed=True):
    input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig"
    output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig"
    """<p>Specifies where to send the output files. </p>"""
    data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn"
    r"""<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions\">Role-based permissions</a>.</p>"""
    job_name: NotRequired["capo_comprehend.types.job_name.JobName"]
    """<p>The identifier of the job.</p>"""
    language_code: "capo_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input documents. Currently, English is the only supported language.</p>"""
    client_request_token: NotRequired[
        "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""
    volume_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    r"""<p>ID for the KMS key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>"""
    vpc_config: NotRequired["capo_comprehend.types.vpc_config.VpcConfig"]
    tags: NotRequired["capo_comprehend.types.tag_list.TagList"]
    r"""<p>Tags to associate with the targeted sentiment detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTargetedSentimentDetectionJobRequest) -> dict:
    out: dict = {}
    import capo_comprehend.types.input_data_config

    out["InputDataConfig"] = (
        capo_comprehend.types.input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    import capo_comprehend.types.output_data_config

    out["OutputDataConfig"] = (
        capo_comprehend.types.output_data_config.serialize_aws_json_1_1(
            value["output_data_config"]
        )
    )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import capo_comprehend.types.language_code

    out["LanguageCode"] = capo_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import capo_comprehend.types.vpc_config

        out["VpcConfig"] = capo_comprehend.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "tags" in value:
        import capo_comprehend.types.tag_list

        out["Tags"] = capo_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTargetedSentimentDetectionJobRequest:
    out: StartTargetedSentimentDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if "InputDataConfig" in data:
        import capo_comprehend.types.input_data_config

        out["input_data_config"] = (
            capo_comprehend.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartTargetedSentimentDetectionJobRequest.input_data_config required"
        )
    if "OutputDataConfig" in data:
        import capo_comprehend.types.output_data_config

        out["output_data_config"] = (
            capo_comprehend.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartTargetedSentimentDetectionJobRequest.output_data_config required"
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartTargetedSentimentDetectionJobRequest.data_access_role_arn required"
        )
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "LanguageCode" in data:
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "StartTargetedSentimentDetectionJobRequest.language_code required"
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "VolumeKmsKeyId" in data:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if "VpcConfig" in data:
        import capo_comprehend.types.vpc_config

        out["vpc_config"] = capo_comprehend.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if "Tags" in data:
        import capo_comprehend.types.tag_list

        out["tags"] = capo_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
