"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.app_configs
    import aws_sdk_opensearch.types.application_name
    import aws_sdk_opensearch.types.client_token
    import aws_sdk_opensearch.types.data_sources
    import aws_sdk_opensearch.types.iam_identity_center_options_input
    import aws_sdk_opensearch.types.kms_key_arn
    import aws_sdk_opensearch.types.tag_list


class CreateApplicationRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_opensearch.types.client_token.ClientToken"]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    name: "aws_sdk_opensearch.types.application_name.ApplicationName"
    """<p>The unique name of the OpenSearch application. Names must be unique within an Amazon Web Services Region for each account.</p>"""
    data_sources: NotRequired["aws_sdk_opensearch.types.data_sources.DataSources"]
    """<p>The data sources to link to the OpenSearch application.</p>"""
    iam_identity_center_options: NotRequired[
        "aws_sdk_opensearch.types.iam_identity_center_options_input.IamIdentityCenterOptionsInput"
    ]
    """<p>Configuration settings for integrating Amazon Web Services IAM Identity Center with the OpenSearch application.</p>"""
    app_configs: NotRequired["aws_sdk_opensearch.types.app_configs.AppConfigs"]
    """<p>Configuration settings for the OpenSearch application, including administrative options.</p>"""
    tag_list: NotRequired["aws_sdk_opensearch.types.tag_list.TagList"]
    kms_key_arn: NotRequired["aws_sdk_opensearch.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the application's data at rest. If provided, the application uses your customer-managed key for encryption. If omitted, the application uses an AWS-managed key. The KMS key must be in the same region as the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "data_sources" in value:
        import aws_sdk_opensearch.types.data_sources

        out["dataSources"] = aws_sdk_opensearch.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "iam_identity_center_options" in value:
        import aws_sdk_opensearch.types.iam_identity_center_options_input

        out["iamIdentityCenterOptions"] = (
            aws_sdk_opensearch.types.iam_identity_center_options_input.serialize_json(
                value["iam_identity_center_options"]
            )
        )
    if "app_configs" in value:
        import aws_sdk_opensearch.types.app_configs

        out["appConfigs"] = aws_sdk_opensearch.types.app_configs.serialize_json(
            value["app_configs"]
        )
    if "tag_list" in value:
        import aws_sdk_opensearch.types.tag_list

        out["tagList"] = aws_sdk_opensearch.types.tag_list.serialize_json(
            value["tag_list"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateApplicationRequest.name required")
    if "dataSources" in data:
        import aws_sdk_opensearch.types.data_sources

        out["data_sources"] = aws_sdk_opensearch.types.data_sources.deserialize_json(
            data["dataSources"]
        )
    if "iamIdentityCenterOptions" in data:
        import aws_sdk_opensearch.types.iam_identity_center_options_input

        out["iam_identity_center_options"] = (
            aws_sdk_opensearch.types.iam_identity_center_options_input.deserialize_json(
                data["iamIdentityCenterOptions"]
            )
        )
    if "appConfigs" in data:
        import aws_sdk_opensearch.types.app_configs

        out["app_configs"] = aws_sdk_opensearch.types.app_configs.deserialize_json(
            data["appConfigs"]
        )
    if "tagList" in data:
        import aws_sdk_opensearch.types.tag_list

        out["tag_list"] = aws_sdk_opensearch.types.tag_list.deserialize_json(
            data["tagList"]
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
