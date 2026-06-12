"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateEntityRecognizerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.client_request_token_string
    import aws_sdk_comprehend.types.comprehend_arn_name
    import aws_sdk_comprehend.types.entity_recognizer_input_data_config
    import aws_sdk_comprehend.types.iam_role_arn
    import aws_sdk_comprehend.types.kms_key_id
    import aws_sdk_comprehend.types.language_code
    import aws_sdk_comprehend.types.policy
    import aws_sdk_comprehend.types.tag_list
    import aws_sdk_comprehend.types.version_name
    import aws_sdk_comprehend.types.vpc_config


class CreateEntityRecognizerRequest(TypedDict):
    recognizer_name: "aws_sdk_comprehend.types.comprehend_arn_name.ComprehendArnName"
    """<p>The name given to the newly created recognizer. Recognizer names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The name must be unique in the account/Region.</p>"""
    version_name: NotRequired["aws_sdk_comprehend.types.version_name.VersionName"]
    """<p>The version name given to the newly created recognizer. Version names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same recognizer name in the account/Region.</p>"""
    data_access_role_arn: "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    tags: NotRequired["aws_sdk_comprehend.types.tag_list.TagList"]
    """<p>Tags to associate with the entity recognizer. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department. </p>"""
    input_data_config: "aws_sdk_comprehend.types.entity_recognizer_input_data_config.EntityRecognizerInputDataConfig"
    """<p>Specifies the format and location of the input data. The S3 bucket containing the input data must be located in the same Region as the entity recognizer being created. </p>"""
    client_request_token: NotRequired[
        "aws_sdk_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p> A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""
    language_code: "aws_sdk_comprehend.types.language_code.LanguageCode"
    """<p> You can specify any of the following languages: English (\"en\"), Spanish (\"es\"), French (\"fr\"), Italian (\"it\"), German (\"de\"), or Portuguese (\"pt\"). If you plan to use this entity recognizer with PDF, Word, or image input files, you must specify English as the language. All training documents must be in the same language.</p>"""
    volume_kms_key_id: NotRequired["aws_sdk_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>"""
    vpc_config: NotRequired["aws_sdk_comprehend.types.vpc_config.VpcConfig"]
    """<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your custom entity recognizer. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>"""
    model_kms_key_id: NotRequired["aws_sdk_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>"""
    model_policy: NotRequired["aws_sdk_comprehend.types.policy.Policy"]
    """<p>The JSON resource-based policy to attach to your custom entity recognizer model. You can use this policy to allow another Amazon Web Services account to import your custom model.</p> <p>Provide your JSON as a UTF-8 encoded string without line breaks. To provide valid JSON for your policy, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>\"{\\"attribute\\": \\"value\\", \\"attribute\\": [\\"value\\"]}\"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{\"attribute\": \"value\", \"attribute\": [\"value\"]}'</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEntityRecognizerRequest) -> dict:
    out: dict = {}
    out["RecognizerName"] = value["recognizer_name"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "tags" in value:
        import aws_sdk_comprehend.types.tag_list

        out["Tags"] = aws_sdk_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    import aws_sdk_comprehend.types.entity_recognizer_input_data_config

    out["InputDataConfig"] = (
        aws_sdk_comprehend.types.entity_recognizer_input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    import aws_sdk_comprehend.types.language_code

    out["LanguageCode"] = aws_sdk_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import aws_sdk_comprehend.types.vpc_config

        out["VpcConfig"] = aws_sdk_comprehend.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "model_kms_key_id" in value:
        out["ModelKmsKeyId"] = value["model_kms_key_id"]
    if "model_policy" in value:
        out["ModelPolicy"] = value["model_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEntityRecognizerRequest:
    out: CreateEntityRecognizerRequest = {}  # type: ignore[typeddict-item]
    if "RecognizerName" in data:
        out["recognizer_name"] = data["RecognizerName"]
    else:
        raise DeserializationError(
            "CreateEntityRecognizerRequest.recognizer_name required"
        )
    if "VersionName" in data:
        out["version_name"] = data["VersionName"]
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "CreateEntityRecognizerRequest.data_access_role_arn required"
        )
    if "Tags" in data:
        import aws_sdk_comprehend.types.tag_list

        out["tags"] = aws_sdk_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "InputDataConfig" in data:
        import aws_sdk_comprehend.types.entity_recognizer_input_data_config

        out["input_data_config"] = (
            aws_sdk_comprehend.types.entity_recognizer_input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEntityRecognizerRequest.input_data_config required"
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "LanguageCode" in data:
        import aws_sdk_comprehend.types.language_code

        out["language_code"] = (
            aws_sdk_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEntityRecognizerRequest.language_code required"
        )
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
    if "ModelPolicy" in data:
        out["model_policy"] = data["ModelPolicy"]
    return out
