"""Generated from Smithy shape ``com.amazonaws.athena#DataCatalogSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.catalog_name_string
    import aws_sdk_athena.types.connection_type
    import aws_sdk_athena.types.data_catalog_status
    import aws_sdk_athena.types.data_catalog_type
    import aws_sdk_athena.types.error_message


class DataCatalogSummary(TypedDict, closed=True):
    catalog_name: NotRequired[
        "aws_sdk_athena.types.catalog_name_string.CatalogNameString"
    ]
    """<p>The name of the data catalog. The catalog name is unique for the Amazon Web Services account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.</p>"""
    type: NotRequired["aws_sdk_athena.types.data_catalog_type.DataCatalogType"]
    """<p>The data catalog type.</p>"""
    status: NotRequired["aws_sdk_athena.types.data_catalog_status.DataCatalogStatus"]
    """<p>The status of the creation or deletion of the data catalog.</p> <ul> <li> <p>The <code>LAMBDA</code>, <code>GLUE</code>, and <code>HIVE</code> data catalog types are created synchronously. Their status is either <code>CREATE_COMPLETE</code> or <code>CREATE_FAILED</code>.</p> </li> <li> <p>The <code>FEDERATED</code> data catalog type is created asynchronously.</p> </li> </ul> <p>Data catalog creation status:</p> <ul> <li> <p> <code>CREATE_IN_PROGRESS</code>: Federated data catalog creation in progress.</p> </li> <li> <p> <code>CREATE_COMPLETE</code>: Data catalog creation complete.</p> </li> <li> <p> <code>CREATE_FAILED</code>: Data catalog could not be created.</p> </li> <li> <p> <code>CREATE_FAILED_CLEANUP_IN_PROGRESS</code>: Federated data catalog creation failed and is being removed.</p> </li> <li> <p> <code>CREATE_FAILED_CLEANUP_COMPLETE</code>: Federated data catalog creation failed and was removed.</p> </li> <li> <p> <code>CREATE_FAILED_CLEANUP_FAILED</code>: Federated data catalog creation failed but could not be removed.</p> </li> </ul> <p>Data catalog deletion status:</p> <ul> <li> <p> <code>DELETE_IN_PROGRESS</code>: Federated data catalog deletion in progress.</p> </li> <li> <p> <code>DELETE_COMPLETE</code>: Federated data catalog deleted.</p> </li> <li> <p> <code>DELETE_FAILED</code>: Federated data catalog could not be deleted.</p> </li> </ul>"""
    connection_type: NotRequired["aws_sdk_athena.types.connection_type.ConnectionType"]
    r"""<p>The type of connection for a <code>FEDERATED</code> data catalog (for example, <code>REDSHIFT</code>, <code>MYSQL</code>, or <code>SQLSERVER</code>). For information about individual connectors, see <a href=\"https://docs.aws.amazon.com/athena/latest/ug/connectors-available.html\">Available data source connectors</a>.</p>"""
    error: NotRequired["aws_sdk_athena.types.error_message.ErrorMessage"]
    """<p>Text of the error that occurred during data catalog creation or deletion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataCatalogSummary) -> dict:
    out: dict = {}
    if "catalog_name" in value:
        out["CatalogName"] = value["catalog_name"]
    if "type" in value:
        import aws_sdk_athena.types.data_catalog_type

        out["Type"] = aws_sdk_athena.types.data_catalog_type.serialize_aws_json_1_1(
            value["type"]
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


def deserialize_aws_json_1_1(data: dict) -> DataCatalogSummary:
    out: DataCatalogSummary = {}  # type: ignore[typeddict-item]
    if "CatalogName" in data:
        out["catalog_name"] = data["CatalogName"]
    if "Type" in data:
        import aws_sdk_athena.types.data_catalog_type

        out["type"] = aws_sdk_athena.types.data_catalog_type.deserialize_aws_json_1_1(
            data["Type"]
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
