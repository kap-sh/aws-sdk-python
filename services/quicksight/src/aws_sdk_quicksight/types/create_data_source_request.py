"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.data_source_credentials
    import aws_sdk_quicksight.types.data_source_parameters
    import aws_sdk_quicksight.types.data_source_type
    import aws_sdk_quicksight.types.folder_arn_list
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.resource_name
    import aws_sdk_quicksight.types.resource_permission_list
    import aws_sdk_quicksight.types.ssl_properties
    import aws_sdk_quicksight.types.tag_list
    import aws_sdk_quicksight.types.vpc_connection_properties


class CreateDataSourceRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_source_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>An ID for the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account. </p>"""
    name: "aws_sdk_quicksight.types.resource_name.ResourceName"
    """<p>A display name for the data source.</p>"""
    type: "aws_sdk_quicksight.types.data_source_type.DataSourceType"
    """<p>The type of the data source. To return a list of all data sources, use <code>ListDataSources</code>.</p> <p>Use <code>AMAZON_ELASTICSEARCH</code> for Amazon OpenSearch Service.</p>"""
    data_source_parameters: NotRequired[
        "aws_sdk_quicksight.types.data_source_parameters.DataSourceParameters"
    ]
    """<p>The parameters that Amazon Quick Sight uses to connect to your underlying source.</p>"""
    credentials: NotRequired[
        "aws_sdk_quicksight.types.data_source_credentials.DataSourceCredentials"
    ]
    """<p>The credentials Amazon Quick Sight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.</p>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A list of resource permissions on the data source.</p>"""
    vpc_connection_properties: NotRequired[
        "aws_sdk_quicksight.types.vpc_connection_properties.VpcConnectionProperties"
    ]
    """<p>Use this parameter only when you want Amazon Quick Sight to use a VPC connection when connecting to your underlying source.</p>"""
    ssl_properties: NotRequired["aws_sdk_quicksight.types.ssl_properties.SslProperties"]
    """<p>Secure Socket Layer (SSL) properties that apply when Amazon Quick Sight connects to your underlying source.</p>"""
    tags: NotRequired["aws_sdk_quicksight.types.tag_list.TagList"]
    """<p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>"""
    folder_arns: NotRequired["aws_sdk_quicksight.types.folder_arn_list.FolderArnList"]
    """<p>When you create the data source, Amazon Quick Sight adds the data source to these folders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceRequest) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.data_source_type

    out["Type"] = aws_sdk_quicksight.types.data_source_type.serialize_json(
        value["type"]
    )
    if "data_source_parameters" in value:
        import aws_sdk_quicksight.types.data_source_parameters

        out["DataSourceParameters"] = (
            aws_sdk_quicksight.types.data_source_parameters.serialize_json(
                value["data_source_parameters"]
            )
        )
    if "credentials" in value:
        import aws_sdk_quicksight.types.data_source_credentials

        out["Credentials"] = (
            aws_sdk_quicksight.types.data_source_credentials.serialize_json(
                value["credentials"]
            )
        )
    if "permissions" in value:
        import aws_sdk_quicksight.types.resource_permission_list

        out["Permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
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
    if "tags" in value:
        import aws_sdk_quicksight.types.tag_list

        out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    if "folder_arns" in value:
        import aws_sdk_quicksight.types.folder_arn_list

        out["FolderArns"] = aws_sdk_quicksight.types.folder_arn_list.serialize_json(
            value["folder_arns"]
        )
    return out


def deserialize_json(data: dict) -> CreateDataSourceRequest:
    out: CreateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    else:
        raise DeserializationError("CreateDataSourceRequest.data_source_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDataSourceRequest.name required")
    if "Type" in data:
        import aws_sdk_quicksight.types.data_source_type

        out["type"] = aws_sdk_quicksight.types.data_source_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateDataSourceRequest.type required")
    if "DataSourceParameters" in data:
        import aws_sdk_quicksight.types.data_source_parameters

        out["data_source_parameters"] = (
            aws_sdk_quicksight.types.data_source_parameters.deserialize_json(
                data["DataSourceParameters"]
            )
        )
    if "Credentials" in data:
        import aws_sdk_quicksight.types.data_source_credentials

        out["credentials"] = (
            aws_sdk_quicksight.types.data_source_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    if "Permissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
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
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    if "FolderArns" in data:
        import aws_sdk_quicksight.types.folder_arn_list

        out["folder_arns"] = aws_sdk_quicksight.types.folder_arn_list.deserialize_json(
            data["FolderArns"]
        )
    return out
