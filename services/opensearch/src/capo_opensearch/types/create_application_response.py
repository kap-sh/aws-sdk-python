"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.app_configs
    import capo_opensearch.types.application_name
    import capo_opensearch.types.arn
    import capo_opensearch.types.data_sources
    import capo_opensearch.types.iam_identity_center_options
    import capo_opensearch.types.id
    import capo_opensearch.types.kms_key_arn
    import capo_opensearch.types.tag_list
    import capo_opensearch.types.timestamp


class CreateApplicationResponse(TypedDict, closed=True):
    id: NotRequired["capo_opensearch.types.id.Id"]
    """<p>The unique identifier assigned to the OpenSearch application.</p>"""
    name: NotRequired["capo_opensearch.types.application_name.ApplicationName"]
    """<p>The name of the OpenSearch application.</p>"""
    arn: NotRequired["capo_opensearch.types.arn.ARN"]
    data_sources: NotRequired["capo_opensearch.types.data_sources.DataSources"]
    """<p>The data sources linked to the OpenSearch application.</p>"""
    iam_identity_center_options: NotRequired[
        "capo_opensearch.types.iam_identity_center_options.IamIdentityCenterOptions"
    ]
    """<p>The IAM Identity Center settings configured for the OpenSearch application.</p>"""
    app_configs: NotRequired["capo_opensearch.types.app_configs.AppConfigs"]
    """<p>Configuration settings for the OpenSearch application, including administrative options.</p>"""
    tag_list: NotRequired["capo_opensearch.types.tag_list.TagList"]
    created_at: NotRequired["capo_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp indicating when the OpenSearch application was created.</p>"""
    kms_key_arn: NotRequired["capo_opensearch.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the application's data at rest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "data_sources" in value:
        import capo_opensearch.types.data_sources

        out["dataSources"] = capo_opensearch.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "iam_identity_center_options" in value:
        import capo_opensearch.types.iam_identity_center_options

        out["iamIdentityCenterOptions"] = (
            capo_opensearch.types.iam_identity_center_options.serialize_json(
                value["iam_identity_center_options"]
            )
        )
    if "app_configs" in value:
        import capo_opensearch.types.app_configs

        out["appConfigs"] = capo_opensearch.types.app_configs.serialize_json(
            value["app_configs"]
        )
    if "tag_list" in value:
        import capo_opensearch.types.tag_list

        out["tagList"] = capo_opensearch.types.tag_list.serialize_json(
            value["tag_list"]
        )
    if "created_at" in value:
        import capo_opensearch.types.timestamp

        out["createdAt"] = capo_opensearch.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "dataSources" in data:
        import capo_opensearch.types.data_sources

        out["data_sources"] = capo_opensearch.types.data_sources.deserialize_json(
            data["dataSources"]
        )
    if "iamIdentityCenterOptions" in data:
        import capo_opensearch.types.iam_identity_center_options

        out["iam_identity_center_options"] = (
            capo_opensearch.types.iam_identity_center_options.deserialize_json(
                data["iamIdentityCenterOptions"]
            )
        )
    if "appConfigs" in data:
        import capo_opensearch.types.app_configs

        out["app_configs"] = capo_opensearch.types.app_configs.deserialize_json(
            data["appConfigs"]
        )
    if "tagList" in data:
        import capo_opensearch.types.tag_list

        out["tag_list"] = capo_opensearch.types.tag_list.deserialize_json(
            data["tagList"]
        )
    if "createdAt" in data:
        import capo_opensearch.types.timestamp

        out["created_at"] = capo_opensearch.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
