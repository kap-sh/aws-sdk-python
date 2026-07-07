"""Generated from Smithy shape ``com.amazonaws.athena#DataCatalog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.catalog_name_string
    import aws_sdk_athena.types.connection_type
    import aws_sdk_athena.types.data_catalog_status
    import aws_sdk_athena.types.data_catalog_type
    import aws_sdk_athena.types.description_string
    import aws_sdk_athena.types.error_message
    import aws_sdk_athena.types.parameters_map


class DataCatalog(TypedDict, closed=True):
    name: "aws_sdk_athena.types.catalog_name_string.CatalogNameString"
    """<p>The name of the data catalog. The catalog name must be unique for the Amazon Web Services account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.description_string.DescriptionString"
    ]
    """<p>An optional description of the data catalog.</p>"""
    type: "aws_sdk_athena.types.data_catalog_type.DataCatalogType"
    """<p>The type of data catalog to create: <code>LAMBDA</code> for a federated catalog, <code>GLUE</code> for an Glue Data Catalog, and <code>HIVE</code> for an external Apache Hive metastore. <code>FEDERATED</code> is a federated catalog for which Athena creates the connection and the Lambda function for you based on the parameters that you pass.</p>"""
    parameters: NotRequired["aws_sdk_athena.types.parameters_map.ParametersMap"]
    r"""<p>Specifies the Lambda function or functions to use for the data catalog. This is a mapping whose values depend on the catalog type. </p> <ul> <li> <p>For the <code>HIVE</code> data catalog type, use the following syntax. The <code>metadata-function</code> parameter is required. <code>The sdk-version</code> parameter is optional and defaults to the currently supported version.</p> <p> <code>metadata-function=<i>lambda_arn</i>, sdk-version=<i>version_number</i> </code> </p> </li> <li> <p>For the <code>LAMBDA</code> data catalog type, use one of the following sets of required parameters, but not both.</p> <ul> <li> <p>If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.</p> <p> <code>metadata-function=<i>lambda_arn</i>, record-function=<i>lambda_arn</i> </code> </p> </li> <li> <p> If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.</p> <p> <code>function=<i>lambda_arn</i> </code> </p> </li> </ul> </li> <li> <p>The <code>GLUE</code> type takes a catalog ID parameter and is required. The <code> <i>catalog_id</i> </code> is the account ID of the Amazon Web Services account to which the Glue catalog belongs.</p> <p> <code>catalog-id=<i>catalog_id</i> </code> </p> <ul> <li> <p>The <code>GLUE</code> data catalog type also applies to the default <code>AwsDataCatalog</code> that already exists in your account, of which you can have only one and cannot modify.</p> </li> </ul> </li> <li> <p>The <code>FEDERATED</code> data catalog type uses one of the following parameters, but not both. Use <code>connection-arn</code> for an existing Glue connection. Use <code>connection-type</code> and <code>connection-properties</code> to specify the configuration setting for a new connection.</p> <ul> <li> <p> <code>connection-arn:<i><glue_connection_arn_to_reuse></i> </code> </p> </li> <li> <p> <code>connection-type:MYSQL|REDSHIFT|...., connection-properties:\"<i><json_string></i>\"</code> </p> <p>For <i> <code><json_string></code> </i>, use escaped JSON text, as in the following example.</p> <p> <code>\"{\\"spill_bucket\\":\\"my_spill\\",\\"spill_prefix\\":\\"athena-spill\\",\\"host\\":\\"abc12345.snowflakecomputing.com\\",\\"port\\":\\"1234\\",\\"warehouse\\":\\"DEV_WH\\",\\"database\\":\\"TEST\\",\\"schema\\":\\"PUBLIC\\",\\"SecretArn\\":\\"arn:aws:secretsmanager:ap-south-1:111122223333:secret:snowflake-XHb67j\\"}\"</code> </p> </li> </ul> </li> </ul>"""
    status: NotRequired["aws_sdk_athena.types.data_catalog_status.DataCatalogStatus"]
    """<p>The status of the creation or deletion of the data catalog.</p> <ul> <li> <p>The <code>LAMBDA</code>, <code>GLUE</code>, and <code>HIVE</code> data catalog types are created synchronously. Their status is either <code>CREATE_COMPLETE</code> or <code>CREATE_FAILED</code>.</p> </li> <li> <p>The <code>FEDERATED</code> data catalog type is created asynchronously.</p> </li> </ul> <p>Data catalog creation status:</p> <ul> <li> <p> <code>CREATE_IN_PROGRESS</code>: Federated data catalog creation in progress.</p> </li> <li> <p> <code>CREATE_COMPLETE</code>: Data catalog creation complete.</p> </li> <li> <p> <code>CREATE_FAILED</code>: Data catalog could not be created.</p> </li> <li> <p> <code>CREATE_FAILED_CLEANUP_IN_PROGRESS</code>: Federated data catalog creation failed and is being removed.</p> </li> <li> <p> <code>CREATE_FAILED_CLEANUP_COMPLETE</code>: Federated data catalog creation failed and was removed.</p> </li> <li> <p> <code>CREATE_FAILED_CLEANUP_FAILED</code>: Federated data catalog creation failed but could not be removed.</p> </li> </ul> <p>Data catalog deletion status:</p> <ul> <li> <p> <code>DELETE_IN_PROGRESS</code>: Federated data catalog deletion in progress.</p> </li> <li> <p> <code>DELETE_COMPLETE</code>: Federated data catalog deleted.</p> </li> <li> <p> <code>DELETE_FAILED</code>: Federated data catalog could not be deleted.</p> </li> </ul>"""
    connection_type: NotRequired["aws_sdk_athena.types.connection_type.ConnectionType"]
    r"""<p>The type of connection for a <code>FEDERATED</code> data catalog (for example, <code>REDSHIFT</code>, <code>MYSQL</code>, or <code>SQLSERVER</code>). For information about individual connectors, see <a href=\"https://docs.aws.amazon.com/athena/latest/ug/connectors-available.html\">Available data source connectors</a>.</p>"""
    error: NotRequired["aws_sdk_athena.types.error_message.ErrorMessage"]
    """<p>Text of the error that occurred during data catalog creation or deletion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataCatalog) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_athena.types.data_catalog_type

    out["Type"] = aws_sdk_athena.types.data_catalog_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "parameters" in value:
        import aws_sdk_athena.types.parameters_map

        out["Parameters"] = aws_sdk_athena.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "status" in value:
        import aws_sdk_athena.types.data_catalog_status

        out["Status"] = aws_sdk_athena.types.data_catalog_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "connection_type" in value:
        import aws_sdk_athena.types.connection_type

        out["ConnectionType"] = (
            aws_sdk_athena.types.connection_type.serialize_aws_json_1_1(
                value["connection_type"]
            )
        )
    if "error" in value:
        out["Error"] = value["error"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataCatalog:
    out: DataCatalog = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DataCatalog.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        import aws_sdk_athena.types.data_catalog_type

        out["type"] = aws_sdk_athena.types.data_catalog_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("DataCatalog.type required")
    if "Parameters" in data:
        import aws_sdk_athena.types.parameters_map

        out["parameters"] = (
            aws_sdk_athena.types.parameters_map.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if "Status" in data:
        import aws_sdk_athena.types.data_catalog_status

        out["status"] = (
            aws_sdk_athena.types.data_catalog_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ConnectionType" in data:
        import aws_sdk_athena.types.connection_type

        out["connection_type"] = (
            aws_sdk_athena.types.connection_type.deserialize_aws_json_1_1(
                data["ConnectionType"]
            )
        )
    if "Error" in data:
        out["error"] = data["Error"]
    return out
