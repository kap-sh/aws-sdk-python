"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceOverrideParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_source_credentials
    import aws_sdk_quicksight.types.data_source_parameters
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.resource_name
    import aws_sdk_quicksight.types.ssl_properties
    import aws_sdk_quicksight.types.vpc_connection_properties


class AssetBundleImportJobDataSourceOverrideParameters(TypedDict):
    data_source_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the data source to apply overrides to.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the data source.</p>"""
    data_source_parameters: NotRequired[
        "aws_sdk_quicksight.types.data_source_parameters.DataSourceParameters"
    ]
    vpc_connection_properties: NotRequired[
        "aws_sdk_quicksight.types.vpc_connection_properties.VpcConnectionProperties"
    ]
    ssl_properties: NotRequired["aws_sdk_quicksight.types.ssl_properties.SslProperties"]
    credentials: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_data_source_credentials.AssetBundleImportJobDataSourceCredentials"
    ]
    """<p>An optional structure that provides the credentials to be used to create the imported data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSourceOverrideParameters) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "data_source_parameters" in value:
        import aws_sdk_quicksight.types.data_source_parameters

        out["DataSourceParameters"] = (
            aws_sdk_quicksight.types.data_source_parameters.serialize_json(
                value["data_source_parameters"]
            )
        )
    if "vpc_connection_properties" in value:
        import aws_sdk_quicksight.types.vpc_connection_properties

        out["VpcConnectionProperties"] = (
            aws_sdk_quicksight.types.vpc_connection_properties.serialize_json(
                value["vpc_connection_properties"]
            )
        )
    if "ssl_properties" in value:
        import aws_sdk_quicksight.types.ssl_properties

        out["SslProperties"] = aws_sdk_quicksight.types.ssl_properties.serialize_json(
            value["ssl_properties"]
        )
    if "credentials" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_data_source_credentials

        out["Credentials"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_data_source_credentials.serialize_json(
                value["credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSourceOverrideParameters:
    out: AssetBundleImportJobDataSourceOverrideParameters = {}  # type: ignore[typeddict-item]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSourceOverrideParameters.data_source_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "DataSourceParameters" in data:
        import aws_sdk_quicksight.types.data_source_parameters

        out["data_source_parameters"] = (
            aws_sdk_quicksight.types.data_source_parameters.deserialize_json(
                data["DataSourceParameters"]
            )
        )
    if "VpcConnectionProperties" in data:
        import aws_sdk_quicksight.types.vpc_connection_properties

        out["vpc_connection_properties"] = (
            aws_sdk_quicksight.types.vpc_connection_properties.deserialize_json(
                data["VpcConnectionProperties"]
            )
        )
    if "SslProperties" in data:
        import aws_sdk_quicksight.types.ssl_properties

        out["ssl_properties"] = (
            aws_sdk_quicksight.types.ssl_properties.deserialize_json(
                data["SslProperties"]
            )
        )
    if "Credentials" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_data_source_credentials

        out["credentials"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_data_source_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    return out
