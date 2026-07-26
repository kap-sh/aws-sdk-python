"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateDocumentClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.client_request_token_string
    import capo_comprehend.types.comprehend_arn_name
    import capo_comprehend.types.document_classifier_input_data_config
    import capo_comprehend.types.document_classifier_mode
    import capo_comprehend.types.document_classifier_output_data_config
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.kms_key_id
    import capo_comprehend.types.language_code
    import capo_comprehend.types.policy
    import capo_comprehend.types.tag_list
    import capo_comprehend.types.version_name
    import capo_comprehend.types.vpc_config


class CreateDocumentClassifierRequest(TypedDict, closed=True):
    document_classifier_name: (
        "capo_comprehend.types.comprehend_arn_name.ComprehendArnName"
    )
    """<p>The name of the document classifier.</p>"""
    version_name: NotRequired["capo_comprehend.types.version_name.VersionName"]
    """<p>The version name given to the newly created classifier. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the Amazon Web Services account/Amazon Web Services Region.</p>"""
    data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    tags: NotRequired["capo_comprehend.types.tag_list.TagList"]
    r"""<p>Tags to associate with the document classifier. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department. </p>"""
    input_data_config: "capo_comprehend.types.document_classifier_input_data_config.DocumentClassifierInputDataConfig"
    """<p>Specifies the format and location of the input data for the job.</p>"""
    output_data_config: NotRequired[
        "capo_comprehend.types.document_classifier_output_data_config.DocumentClassifierOutputDataConfig"
    ]
    """<p>Specifies the location for the output files from a custom classifier job. This parameter is required for a request that creates a native document model.</p>"""
    client_request_token: NotRequired[
        "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""
    language_code: "capo_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input documents. You can specify any of the languages supported by Amazon Comprehend. All documents must be in the same language.</p>"""
    volume_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    r"""<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>"""
    vpc_config: NotRequired["capo_comprehend.types.vpc_config.VpcConfig"]
    r"""<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your custom classifier. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>"""
    mode: NotRequired[
        "capo_comprehend.types.document_classifier_mode.DocumentClassifierMode"
    ]
    """<p>Indicates the mode in which the classifier will be trained. The classifier can be trained in multi-class (single-label) mode or multi-label mode. Multi-class mode identifies a single class label for each document and multi-label mode identifies one or more class labels for each document. Multiple labels for an individual document are separated by a delimiter. The default delimiter between labels is a pipe (|).</p>"""
    model_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    r"""<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>"""
    model_policy: NotRequired["capo_comprehend.types.policy.Policy"]
    r"""<p>The resource-based policy to attach to your custom document classifier model. You can use this policy to allow another Amazon Web Services account to import your custom model.</p> <p>Provide your policy as a JSON body that you enter as a UTF-8 encoded string without line breaks. To provide valid JSON, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>\"{\\"attribute\\": \\"value\\", \\"attribute\\": [\\"value\\"]}\"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{\"attribute\": \"value\", \"attribute\": [\"value\"]}'</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDocumentClassifierRequest) -> dict:
    out: dict = {}
    out["DocumentClassifierName"] = value["document_classifier_name"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "tags" in value:
        import capo_comprehend.types.tag_list

        out["Tags"] = capo_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    import capo_comprehend.types.document_classifier_input_data_config

    out["InputDataConfig"] = (
        capo_comprehend.types.document_classifier_input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    if "output_data_config" in value:
        import capo_comprehend.types.document_classifier_output_data_config

        out["OutputDataConfig"] = (
            capo_comprehend.types.document_classifier_output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    import capo_comprehend.types.language_code

    out["LanguageCode"] = capo_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import capo_comprehend.types.vpc_config

        out["VpcConfig"] = capo_comprehend.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "mode" in value:
        import capo_comprehend.types.document_classifier_mode

        out["Mode"] = (
            capo_comprehend.types.document_classifier_mode.serialize_aws_json_1_1(
                value["mode"]
            )
        )
    if "model_kms_key_id" in value:
        out["ModelKmsKeyId"] = value["model_kms_key_id"]
    if "model_policy" in value:
        out["ModelPolicy"] = value["model_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDocumentClassifierRequest:
    out: CreateDocumentClassifierRequest = {}  # type: ignore[typeddict-item]
    if "DocumentClassifierName" in data:
        out["document_classifier_name"] = data["DocumentClassifierName"]
    else:
        raise DeserializationError(
            "CreateDocumentClassifierRequest.document_classifier_name required"
        )
    if "VersionName" in data:
        out["version_name"] = data["VersionName"]
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "CreateDocumentClassifierRequest.data_access_role_arn required"
        )
    if "Tags" in data:
        import capo_comprehend.types.tag_list

        out["tags"] = capo_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "InputDataConfig" in data:
        import capo_comprehend.types.document_classifier_input_data_config

        out["input_data_config"] = (
            capo_comprehend.types.document_classifier_input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDocumentClassifierRequest.input_data_config required"
        )
    if "OutputDataConfig" in data:
        import capo_comprehend.types.document_classifier_output_data_config

        out["output_data_config"] = (
            capo_comprehend.types.document_classifier_output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "LanguageCode" in data:
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDocumentClassifierRequest.language_code required"
        )
    if "VolumeKmsKeyId" in data:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if "VpcConfig" in data:
        import capo_comprehend.types.vpc_config

        out["vpc_config"] = capo_comprehend.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if "Mode" in data:
        import capo_comprehend.types.document_classifier_mode

        out["mode"] = (
            capo_comprehend.types.document_classifier_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    if "ModelKmsKeyId" in data:
        out["model_kms_key_id"] = data["ModelKmsKeyId"]
    if "ModelPolicy" in data:
        out["model_policy"] = data["ModelPolicy"]
    return out
