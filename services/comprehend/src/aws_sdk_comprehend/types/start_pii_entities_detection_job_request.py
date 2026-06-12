"""Generated from Smithy shape ``com.amazonaws.comprehend#StartPiiEntitiesDetectionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.client_request_token_string
    import aws_sdk_comprehend.types.iam_role_arn
    import aws_sdk_comprehend.types.input_data_config
    import aws_sdk_comprehend.types.job_name
    import aws_sdk_comprehend.types.language_code
    import aws_sdk_comprehend.types.output_data_config
    import aws_sdk_comprehend.types.pii_entities_detection_mode
    import aws_sdk_comprehend.types.redaction_config
    import aws_sdk_comprehend.types.tag_list


class StartPiiEntitiesDetectionJobRequest(TypedDict):
    input_data_config: "aws_sdk_comprehend.types.input_data_config.InputDataConfig"
    """<p>The input properties for a PII entities detection job.</p>"""
    output_data_config: "aws_sdk_comprehend.types.output_data_config.OutputDataConfig"
    """<p>Provides conﬁguration parameters for the output of PII entity detection jobs.</p>"""
    mode: (
        "aws_sdk_comprehend.types.pii_entities_detection_mode.PiiEntitiesDetectionMode"
    )
    """<p>Specifies whether the output provides the locations (offsets) of PII entities or a file in which PII entities are redacted.</p>"""
    redaction_config: NotRequired[
        "aws_sdk_comprehend.types.redaction_config.RedactionConfig"
    ]
    """<p>Provides configuration parameters for PII entity redaction.</p> <p>This parameter is required if you set the <code>Mode</code> parameter to <code>ONLY_REDACTION</code>. In that case, you must provide a <code>RedactionConfig</code> definition that includes the <code>PiiEntityTypes</code> parameter.</p>"""
    data_access_role_arn: "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    job_name: NotRequired["aws_sdk_comprehend.types.job_name.JobName"]
    """<p>The identifier of the job.</p>"""
    language_code: "aws_sdk_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input documents. Enter the language code for English (en) or Spanish (es).</p>"""
    client_request_token: NotRequired[
        "aws_sdk_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""
    tags: NotRequired["aws_sdk_comprehend.types.tag_list.TagList"]
    """<p>Tags to associate with the PII entities detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartPiiEntitiesDetectionJobRequest) -> dict:
    out: dict = {}
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
    import aws_sdk_comprehend.types.pii_entities_detection_mode

    out["Mode"] = (
        aws_sdk_comprehend.types.pii_entities_detection_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    )
    if "redaction_config" in value:
        import aws_sdk_comprehend.types.redaction_config

        out["RedactionConfig"] = (
            aws_sdk_comprehend.types.redaction_config.serialize_aws_json_1_1(
                value["redaction_config"]
            )
        )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import aws_sdk_comprehend.types.language_code

    out["LanguageCode"] = aws_sdk_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_comprehend.types.tag_list

        out["Tags"] = aws_sdk_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartPiiEntitiesDetectionJobRequest:
    out: StartPiiEntitiesDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if "InputDataConfig" in data:
        import aws_sdk_comprehend.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_comprehend.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartPiiEntitiesDetectionJobRequest.input_data_config required"
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
            "StartPiiEntitiesDetectionJobRequest.output_data_config required"
        )
    if "Mode" in data:
        import aws_sdk_comprehend.types.pii_entities_detection_mode

        out["mode"] = (
            aws_sdk_comprehend.types.pii_entities_detection_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    else:
        raise DeserializationError("StartPiiEntitiesDetectionJobRequest.mode required")
    if "RedactionConfig" in data:
        import aws_sdk_comprehend.types.redaction_config

        out["redaction_config"] = (
            aws_sdk_comprehend.types.redaction_config.deserialize_aws_json_1_1(
                data["RedactionConfig"]
            )
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartPiiEntitiesDetectionJobRequest.data_access_role_arn required"
        )
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "LanguageCode" in data:
        import aws_sdk_comprehend.types.language_code

        out["language_code"] = (
            aws_sdk_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "StartPiiEntitiesDetectionJobRequest.language_code required"
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import aws_sdk_comprehend.types.tag_list

        out["tags"] = aws_sdk_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
