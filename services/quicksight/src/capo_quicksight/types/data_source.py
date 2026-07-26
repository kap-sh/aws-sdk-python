"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.data_source_error_info
    import capo_quicksight.types.data_source_parameters
    import capo_quicksight.types.data_source_parameters_list
    import capo_quicksight.types.data_source_type
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.secret_arn
    import capo_quicksight.types.ssl_properties
    import capo_quicksight.types.timestamp
    import capo_quicksight.types.vpc_connection_properties


class DataSource(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the data source.</p>"""
    data_source_id: NotRequired["capo_quicksight.types.resource_id.ResourceId"]
    """<p>The ID of the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A display name for the data source.</p>"""
    type: NotRequired["capo_quicksight.types.data_source_type.DataSourceType"]
    """<p>The type of the data source. This type indicates which database engine the data source connects to.</p>"""
    status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>The HTTP status of the request.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this data source was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this data source was updated.</p>"""
    data_source_parameters: NotRequired[
        "capo_quicksight.types.data_source_parameters.DataSourceParameters"
    ]
    """<p>The parameters that Quick Sight uses to connect to your underlying source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.</p>"""
    alternate_data_source_parameters: NotRequired[
        "capo_quicksight.types.data_source_parameters_list.DataSourceParametersList"
    ]
    """<p>A set of alternate data source parameters that you want to share for the credentials stored with this data source. The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the <code>DataSourceParameters</code> structure that's in the request with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the structures are an exact match, the request is allowed to use the credentials from this existing data source. If the <code>AlternateDataSourceParameters</code> list is null, the <code>Credentials</code> originally used with this <code>DataSourceParameters</code> are automatically allowed.</p>"""
    vpc_connection_properties: NotRequired[
        "capo_quicksight.types.vpc_connection_properties.VpcConnectionProperties"
    ]
    """<p>The VPC connection information. You need to use this parameter only when you want Quick Sight to use a VPC connection when connecting to your underlying source.</p>"""
    ssl_properties: NotRequired["capo_quicksight.types.ssl_properties.SslProperties"]
    """<p>Secure Socket Layer (SSL) properties that apply when Quick Sight connects to your underlying source.</p>"""
    error_info: NotRequired[
        "capo_quicksight.types.data_source_error_info.DataSourceErrorInfo"
    ]
    """<p>Error information from the last update or the creation of the data source.</p>"""
    secret_arn: NotRequired["capo_quicksight.types.secret_arn.SecretArn"]
    """<p>The Amazon Resource Name (ARN) of the secret associated with the data source in Amazon Secrets Manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_quicksight.types.data_source_type

        out["Type"] = capo_quicksight.types.data_source_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import capo_quicksight.types.resource_status

        out["Status"] = capo_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "data_source_parameters" in value:
        import capo_quicksight.types.data_source_parameters

        out["DataSourceParameters"] = (
            capo_quicksight.types.data_source_parameters.serialize_json(
                value["data_source_parameters"]
            )
        )
    if "alternate_data_source_parameters" in value:
        import capo_quicksight.types.data_source_parameters_list

        out["AlternateDataSourceParameters"] = (
            capo_quicksight.types.data_source_parameters_list.serialize_json(
                value["alternate_data_source_parameters"]
            )
        )
    if "vpc_connection_properties" in value:
        import capo_quicksight.types.vpc_connection_properties

        out["VpcConnectionProperties"] = (
            capo_quicksight.types.vpc_connection_properties.serialize_json(
                value["vpc_connection_properties"]
            )
        )
    if "ssl_properties" in value:
        import capo_quicksight.types.ssl_properties

        out["SslProperties"] = capo_quicksight.types.ssl_properties.serialize_json(
            value["ssl_properties"]
        )
    if "error_info" in value:
        import capo_quicksight.types.data_source_error_info

        out["ErrorInfo"] = capo_quicksight.types.data_source_error_info.serialize_json(
            value["error_info"]
        )
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import capo_quicksight.types.data_source_type

        out["type"] = capo_quicksight.types.data_source_type.deserialize_json(
            data["Type"]
        )
    if "Status" in data:
        import capo_quicksight.types.resource_status

        out["status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "DataSourceParameters" in data:
        import capo_quicksight.types.data_source_parameters

        out["data_source_parameters"] = (
            capo_quicksight.types.data_source_parameters.deserialize_json(
                data["DataSourceParameters"]
            )
        )
    if "AlternateDataSourceParameters" in data:
        import capo_quicksight.types.data_source_parameters_list

        out["alternate_data_source_parameters"] = (
            capo_quicksight.types.data_source_parameters_list.deserialize_json(
                data["AlternateDataSourceParameters"]
            )
        )
    if "VpcConnectionProperties" in data:
        import capo_quicksight.types.vpc_connection_properties

        out["vpc_connection_properties"] = (
            capo_quicksight.types.vpc_connection_properties.deserialize_json(
                data["VpcConnectionProperties"]
            )
        )
    if "SslProperties" in data:
        import capo_quicksight.types.ssl_properties

        out["ssl_properties"] = capo_quicksight.types.ssl_properties.deserialize_json(
            data["SslProperties"]
        )
    if "ErrorInfo" in data:
        import capo_quicksight.types.data_source_error_info

        out["error_info"] = (
            capo_quicksight.types.data_source_error_info.deserialize_json(
                data["ErrorInfo"]
            )
        )
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    return out
