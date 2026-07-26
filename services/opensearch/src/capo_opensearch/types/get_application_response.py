"""Generated from Smithy shape ``com.amazonaws.opensearch#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.app_configs
    import capo_opensearch.types.application_name
    import capo_opensearch.types.application_status
    import capo_opensearch.types.arn
    import capo_opensearch.types.data_sources
    import capo_opensearch.types.iam_identity_center_options
    import capo_opensearch.types.id
    import capo_opensearch.types.kms_key_arn
    import capo_opensearch.types.string
    import capo_opensearch.types.timestamp


class GetApplicationResponse(TypedDict, closed=True):
    id: NotRequired["capo_opensearch.types.id.Id"]
    """<p>The unique identifier of the OpenSearch application.</p>"""
    arn: NotRequired["capo_opensearch.types.arn.ARN"]
    name: NotRequired["capo_opensearch.types.application_name.ApplicationName"]
    """<p>The name of the OpenSearch application.</p>"""
    endpoint: NotRequired["capo_opensearch.types.string.String"]
    """<p>The endpoint URL of the OpenSearch application.</p>"""
    status: NotRequired["capo_opensearch.types.application_status.ApplicationStatus"]
    """<p>The current status of the OpenSearch application. Possible values: <code>CREATING</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>FAILED</code>, <code>ACTIVE</code>, and <code>DELETED</code>.</p>"""
    iam_identity_center_options: NotRequired[
        "capo_opensearch.types.iam_identity_center_options.IamIdentityCenterOptions"
    ]
    """<p>The IAM Identity Center settings configured for the OpenSearch application.</p>"""
    data_sources: NotRequired["capo_opensearch.types.data_sources.DataSources"]
    """<p>The data sources associated with the OpenSearch application.</p>"""
    app_configs: NotRequired["capo_opensearch.types.app_configs.AppConfigs"]
    """<p>The configuration settings of the OpenSearch application.</p>"""
    created_at: NotRequired["capo_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp when the OpenSearch application was created.</p>"""
    last_updated_at: NotRequired["capo_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp of the last update to the OpenSearch application.</p>"""
    kms_key_arn: NotRequired["capo_opensearch.types.kms_key_arn.KmsKeyArn"]
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
        import capo_opensearch.types.application_status

        out["status"] = capo_opensearch.types.application_status.serialize_json(
            value["status"]
        )
    if "iam_identity_center_options" in value:
        import capo_opensearch.types.iam_identity_center_options

        out["iamIdentityCenterOptions"] = (
            capo_opensearch.types.iam_identity_center_options.serialize_json(
                value["iam_identity_center_options"]
            )
        )
    if "data_sources" in value:
        import capo_opensearch.types.data_sources

        out["dataSources"] = capo_opensearch.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "app_configs" in value:
        import capo_opensearch.types.app_configs

        out["appConfigs"] = capo_opensearch.types.app_configs.serialize_json(
            value["app_configs"]
        )
    if "created_at" in value:
        import capo_opensearch.types.timestamp

        out["createdAt"] = capo_opensearch.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_opensearch.types.timestamp

        out["lastUpdatedAt"] = capo_opensearch.types.timestamp.serialize_json(
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
        import capo_opensearch.types.application_status

        out["status"] = capo_opensearch.types.application_status.deserialize_json(
            data["status"]
        )
    if "iamIdentityCenterOptions" in data:
        import capo_opensearch.types.iam_identity_center_options

        out["iam_identity_center_options"] = (
            capo_opensearch.types.iam_identity_center_options.deserialize_json(
                data["iamIdentityCenterOptions"]
            )
        )
    if "dataSources" in data:
        import capo_opensearch.types.data_sources

        out["data_sources"] = capo_opensearch.types.data_sources.deserialize_json(
            data["dataSources"]
        )
    if "appConfigs" in data:
        import capo_opensearch.types.app_configs

        out["app_configs"] = capo_opensearch.types.app_configs.deserialize_json(
            data["appConfigs"]
        )
    if "createdAt" in data:
        import capo_opensearch.types.timestamp

        out["created_at"] = capo_opensearch.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_opensearch.types.timestamp

        out["last_updated_at"] = capo_opensearch.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
