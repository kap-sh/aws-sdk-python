"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StartRxNormInferenceJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.client_request_token_string
    import aws_sdk_comprehendmedical.types.iam_role_arn
    import aws_sdk_comprehendmedical.types.input_data_config
    import aws_sdk_comprehendmedical.types.job_name
    import aws_sdk_comprehendmedical.types.kms_key
    import aws_sdk_comprehendmedical.types.language_code
    import aws_sdk_comprehendmedical.types.output_data_config


class StartRxNormInferenceJobRequest(TypedDict):
    input_data_config: (
        "aws_sdk_comprehendmedical.types.input_data_config.InputDataConfig"
    )
    """<p>Specifies the format and location of the input data for the job.</p>"""
    output_data_config: (
        "aws_sdk_comprehendmedical.types.output_data_config.OutputDataConfig"
    )
    """<p>Specifies where to send the output files.</p>"""
    data_access_role_arn: "aws_sdk_comprehendmedical.types.iam_role_arn.IamRoleArn"
    r"""<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions-med.html#auth-role-permissions-med\"> Role-Based Permissions Required for Asynchronous Operations</a>.</p>"""
    job_name: NotRequired["aws_sdk_comprehendmedical.types.job_name.JobName"]
    """<p>The identifier of the job.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_comprehendmedical.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend Medical generates one.</p>"""
    kms_key: NotRequired["aws_sdk_comprehendmedical.types.kms_key.KMSKey"]
    """<p>An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.</p>"""
    language_code: "aws_sdk_comprehendmedical.types.language_code.LanguageCode"
    """<p>The language of the input documents. All documents must be in the same language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRxNormInferenceJobRequest) -> dict:
    out: dict = {}
    import aws_sdk_comprehendmedical.types.input_data_config

    out["InputDataConfig"] = (
        aws_sdk_comprehendmedical.types.input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    import aws_sdk_comprehendmedical.types.output_data_config

    out["OutputDataConfig"] = (
        aws_sdk_comprehendmedical.types.output_data_config.serialize_aws_json_1_1(
            value["output_data_config"]
        )
    )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    import aws_sdk_comprehendmedical.types.language_code

    out["LanguageCode"] = (
        aws_sdk_comprehendmedical.types.language_code.serialize_aws_json_1_1(
            value["language_code"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRxNormInferenceJobRequest:
    out: StartRxNormInferenceJobRequest = {}  # type: ignore[typeddict-item]
    if "InputDataConfig" in data:
        import aws_sdk_comprehendmedical.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_comprehendmedical.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartRxNormInferenceJobRequest.input_data_config required"
        )
    if "OutputDataConfig" in data:
        import aws_sdk_comprehendmedical.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_comprehendmedical.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartRxNormInferenceJobRequest.output_data_config required"
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartRxNormInferenceJobRequest.data_access_role_arn required"
        )
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "KMSKey" in data:
        out["kms_key"] = data["KMSKey"]
    if "LanguageCode" in data:
        import aws_sdk_comprehendmedical.types.language_code

        out["language_code"] = (
            aws_sdk_comprehendmedical.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "StartRxNormInferenceJobRequest.language_code required"
        )
    return out
