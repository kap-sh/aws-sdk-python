"""Generated from Smithy shape ``com.amazonaws.opensearch#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.app_configs
    import aws_sdk_opensearch.types.application_name
    import aws_sdk_opensearch.types.application_status
    import aws_sdk_opensearch.types.arn
    import aws_sdk_opensearch.types.data_sources
    import aws_sdk_opensearch.types.iam_identity_center_options
    import aws_sdk_opensearch.types.id
    import aws_sdk_opensearch.types.kms_key_arn
    import aws_sdk_opensearch.types.string
    import aws_sdk_opensearch.types.timestamp


class GetApplicationResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_opensearch.types.id.Id"]
    """<p>The unique identifier of the OpenSearch application.</p>"""
    arn: NotRequired["aws_sdk_opensearch.types.arn.ARN"]
    name: NotRequired["aws_sdk_opensearch.types.application_name.ApplicationName"]
    """<p>The name of the OpenSearch application.</p>"""
    endpoint: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The endpoint URL of the OpenSearch application.</p>"""
    status: NotRequired["aws_sdk_opensearch.types.application_status.ApplicationStatus"]
    """<p>The current status of the OpenSearch application. Possible values: <code>CREATING</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>FAILED</code>, <code>ACTIVE</code>, and <code>DELETED</code>.</p>"""
    iam_identity_center_options: NotRequired[
        "aws_sdk_opensearch.types.iam_identity_center_options.IamIdentityCenterOptions"
    ]
    """<p>The IAM Identity Center settings configured for the OpenSearch application.</p>"""
    data_sources: NotRequired["aws_sdk_opensearch.types.data_sources.DataSources"]
    """<p>The data sources associated with the OpenSearch application.</p>"""
    app_configs: NotRequired["aws_sdk_opensearch.types.app_configs.AppConfigs"]
    """<p>The configuration settings of the OpenSearch application.</p>"""
    created_at: NotRequired["aws_sdk_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp when the OpenSearch application was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp of the last update to the OpenSearch application.</p>"""
    kms_key_arn: NotRequired["aws_sdk_opensearch.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the application's data at rest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "status" in value:
        import aws_sdk_opensearch.types.application_status

        out["status"] = aws_sdk_opensearch.types.application_status.serialize_json(
            value["status"]
        )
    if "iam_identity_center_options" in value:
        import aws_sdk_opensearch.types.iam_identity_center_options

        out["iamIdentityCenterOptions"] = (
            aws_sdk_opensearch.types.iam_identity_center_options.serialize_json(
                value["iam_identity_center_options"]
            )
        )
    if "data_sources" in value:
        import aws_sdk_opensearch.types.data_sources

        out["dataSources"] = aws_sdk_opensearch.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "app_configs" in value:
        import aws_sdk_opensearch.types.app_configs

        out["appConfigs"] = aws_sdk_opensearch.types.app_configs.serialize_json(
            value["app_configs"]
        )
    if "created_at" in value:
        import aws_sdk_opensearch.types.timestamp

        out["createdAt"] = aws_sdk_opensearch.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_opensearch.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_opensearch.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    if "status" in data:
        import aws_sdk_opensearch.types.application_status

        out["status"] = aws_sdk_opensearch.types.application_status.deserialize_json(
            data["status"]
        )
    if "iamIdentityCenterOptions" in data:
        import aws_sdk_opensearch.types.iam_identity_center_options

        out["iam_identity_center_options"] = (
            aws_sdk_opensearch.types.iam_identity_center_options.deserialize_json(
                data["iamIdentityCenterOptions"]
            )
        )
    if "dataSources" in data:
        import aws_sdk_opensearch.types.data_sources

        out["data_sources"] = aws_sdk_opensearch.types.data_sources.deserialize_json(
            data["dataSources"]
        )
    if "appConfigs" in data:
        import aws_sdk_opensearch.types.app_configs

        out["app_configs"] = aws_sdk_opensearch.types.app_configs.deserialize_json(
            data["appConfigs"]
        )
    if "createdAt" in data:
        import aws_sdk_opensearch.types.timestamp

        out["created_at"] = aws_sdk_opensearch.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_opensearch.types.timestamp

        out["last_updated_at"] = aws_sdk_opensearch.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
