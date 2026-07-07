"""Generated from Smithy shape ``com.amazonaws.appflow#SalesforceDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.error_handling_config
    import aws_sdk_appflow.types.id_field_name_list
    import aws_sdk_appflow.types.object
    import aws_sdk_appflow.types.salesforce_data_transfer_api
    import aws_sdk_appflow.types.write_operation_type


class SalesforceDestinationProperties(TypedDict, closed=True):
    object: "aws_sdk_appflow.types.object.Object"
    """<p> The object specified in the Salesforce flow destination. </p>"""
    id_field_names: NotRequired[
        "aws_sdk_appflow.types.id_field_name_list.IdFieldNameList"
    ]
    """<p> The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update or delete. </p>"""
    error_handling_config: NotRequired[
        "aws_sdk_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]
    """<p> The settings that determine how Amazon AppFlow handles an error when placing data in the Salesforce destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. <code>ErrorHandlingConfig</code> is a part of the destination connector details. </p>"""
    write_operation_type: NotRequired[
        "aws_sdk_appflow.types.write_operation_type.WriteOperationType"
    ]
    """<p> This specifies the type of write operation to be performed in Salesforce. When the value is <code>UPSERT</code>, then <code>idFieldNames</code> is required. </p>"""
    data_transfer_api: NotRequired[
        "aws_sdk_appflow.types.salesforce_data_transfer_api.SalesforceDataTransferApi"
    ]
    """<p>Specifies which Salesforce API is used by Amazon AppFlow when your flow transfers data to Salesforce.</p> <dl> <dt>AUTOMATIC</dt> <dd> <p>The default. Amazon AppFlow selects which API to use based on the number of records that your flow transfers to Salesforce. If your flow transfers fewer than 1,000 records, Amazon AppFlow uses Salesforce REST API. If your flow transfers 1,000 records or more, Amazon AppFlow uses Salesforce Bulk API 2.0.</p> <p>Each of these Salesforce APIs structures data differently. If Amazon AppFlow selects the API automatically, be aware that, for recurring flows, the data output might vary from one flow run to the next. For example, if a flow runs daily, it might use REST API on one day to transfer 900 records, and it might use Bulk API 2.0 on the next day to transfer 1,100 records. For each of these flow runs, the respective Salesforce API formats the data differently. Some of the differences include how dates are formatted and null values are represented. Also, Bulk API 2.0 doesn't transfer Salesforce compound fields.</p> <p>By choosing this option, you optimize flow performance for both small and large data transfers, but the tradeoff is inconsistent formatting in the output.</p> </dd> <dt>BULKV2</dt> <dd> <p>Amazon AppFlow uses only Salesforce Bulk API 2.0. This API runs asynchronous data transfers, and it's optimal for large sets of data. By choosing this option, you ensure that your flow writes consistent output, but you optimize performance only for large data transfers.</p> <p>Note that Bulk API 2.0 does not transfer Salesforce compound fields.</p> </dd> <dt>REST_SYNC</dt> <dd> <p>Amazon AppFlow uses only Salesforce REST API. By choosing this option, you ensure that your flow writes consistent output, but you decrease performance for large data transfers that are better suited for Bulk API 2.0. In some cases, if your flow attempts to transfer a vary large set of data, it might fail with a timed out error.</p> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceDestinationProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    if "id_field_names" in value:
        import aws_sdk_appflow.types.id_field_name_list

        out["idFieldNames"] = aws_sdk_appflow.types.id_field_name_list.serialize_json(
            value["id_field_names"]
        )
    if "error_handling_config" in value:
        import aws_sdk_appflow.types.error_handling_config

        out["errorHandlingConfig"] = (
            aws_sdk_appflow.types.error_handling_config.serialize_json(
                value["error_handling_config"]
            )
        )
    if "write_operation_type" in value:
        import aws_sdk_appflow.types.write_operation_type

        out["writeOperationType"] = (
            aws_sdk_appflow.types.write_operation_type.serialize_json(
                value["write_operation_type"]
            )
        )
    if "data_transfer_api" in value:
        import aws_sdk_appflow.types.salesforce_data_transfer_api

        out["dataTransferApi"] = (
            aws_sdk_appflow.types.salesforce_data_transfer_api.serialize_json(
                value["data_transfer_api"]
            )
        )
    return out


def deserialize_json(data: dict) -> SalesforceDestinationProperties:
    out: SalesforceDestinationProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("SalesforceDestinationProperties.object required")
    if "idFieldNames" in data:
        import aws_sdk_appflow.types.id_field_name_list

        out["id_field_names"] = (
            aws_sdk_appflow.types.id_field_name_list.deserialize_json(
                data["idFieldNames"]
            )
        )
    if "errorHandlingConfig" in data:
        import aws_sdk_appflow.types.error_handling_config

        out["error_handling_config"] = (
            aws_sdk_appflow.types.error_handling_config.deserialize_json(
                data["errorHandlingConfig"]
            )
        )
    if "writeOperationType" in data:
        import aws_sdk_appflow.types.write_operation_type

        out["write_operation_type"] = (
            aws_sdk_appflow.types.write_operation_type.deserialize_json(
                data["writeOperationType"]
            )
        )
    if "dataTransferApi" in data:
        import aws_sdk_appflow.types.salesforce_data_transfer_api

        out["data_transfer_api"] = (
            aws_sdk_appflow.types.salesforce_data_transfer_api.deserialize_json(
                data["dataTransferApi"]
            )
        )
    return out
