"""Generated from Smithy shape ``com.amazonaws.dynamodb#SourceTableDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.billing_mode
    import aws_sdk_dynamodb.types.item_count
    import aws_sdk_dynamodb.types.key_schema
    import aws_sdk_dynamodb.types.long_object
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.provisioned_throughput
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.table_creation_date_time
    import aws_sdk_dynamodb.types.table_id
    import aws_sdk_dynamodb.types.table_name


class SourceTableDetails(TypedDict, closed=True):
    table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The name of the table for which the backup was created. </p>"""
    table_id: "aws_sdk_dynamodb.types.table_id.TableId"
    """<p>Unique identifier for the table for which the backup was created. </p>"""
    table_arn: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p>ARN of the table for which backup was created. </p>"""
    table_size_bytes: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>Size of the table in bytes. Note that this is an approximate value.</p>"""
    key_schema: "aws_sdk_dynamodb.types.key_schema.KeySchema"
    """<p>Schema of the table. </p>"""
    table_creation_date_time: (
        "aws_sdk_dynamodb.types.table_creation_date_time.TableCreationDateTime"
    )
    """<p>Time when the source table was created. </p>"""
    provisioned_throughput: (
        "aws_sdk_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    )
    """<p>Read IOPs and Write IOPS on the table when the backup was created.</p>"""
    on_demand_throughput: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    item_count: NotRequired["aws_sdk_dynamodb.types.item_count.ItemCount"]
    """<p>Number of items in the table. Note that this is an approximate value. </p>"""
    billing_mode: NotRequired["aws_sdk_dynamodb.types.billing_mode.BillingMode"]
    """<p>Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.</p> <ul> <li> <p> <code>PROVISIONED</code> - Sets the read/write capacity mode to <code>PROVISIONED</code>. We recommend using <code>PROVISIONED</code> for predictable workloads.</p> </li> <li> <p> <code>PAY_PER_REQUEST</code> - Sets the read/write capacity mode to <code>PAY_PER_REQUEST</code>. We recommend using <code>PAY_PER_REQUEST</code> for unpredictable workloads. </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceTableDetails) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    out["TableId"] = value["table_id"]
    if "table_arn" in value:
        out["TableArn"] = value["table_arn"]
    if "table_size_bytes" in value:
        out["TableSizeBytes"] = value["table_size_bytes"]
    import aws_sdk_dynamodb.types.key_schema

    out["KeySchema"] = aws_sdk_dynamodb.types.key_schema.serialize_aws_json_1_0(
        value["key_schema"]
    )
    import aws_sdk_dynamodb.types.table_creation_date_time

    out["TableCreationDateTime"] = (
        aws_sdk_dynamodb.types.table_creation_date_time.serialize_aws_json_1_0(
            value["table_creation_date_time"]
        )
    )
    import aws_sdk_dynamodb.types.provisioned_throughput

    out["ProvisionedThroughput"] = (
        aws_sdk_dynamodb.types.provisioned_throughput.serialize_aws_json_1_0(
            value["provisioned_throughput"]
        )
    )
    if "on_demand_throughput" in value:
        import aws_sdk_dynamodb.types.on_demand_throughput

        out["OnDemandThroughput"] = (
            aws_sdk_dynamodb.types.on_demand_throughput.serialize_aws_json_1_0(
                value["on_demand_throughput"]
            )
        )
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "billing_mode" in value:
        import aws_sdk_dynamodb.types.billing_mode

        out["BillingMode"] = aws_sdk_dynamodb.types.billing_mode.serialize_aws_json_1_0(
            value["billing_mode"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SourceTableDetails:
    out: SourceTableDetails = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("SourceTableDetails.table_name required")
    if "TableId" in data:
        out["table_id"] = data["TableId"]
    else:
        raise DeserializationError("SourceTableDetails.table_id required")
    if "TableArn" in data:
        out["table_arn"] = data["TableArn"]
    if "TableSizeBytes" in data:
        out["table_size_bytes"] = data["TableSizeBytes"]
    if "KeySchema" in data:
        import aws_sdk_dynamodb.types.key_schema

        out["key_schema"] = aws_sdk_dynamodb.types.key_schema.deserialize_aws_json_1_0(
            data["KeySchema"]
        )
    else:
        raise DeserializationError("SourceTableDetails.key_schema required")
    if "TableCreationDateTime" in data:
        import aws_sdk_dynamodb.types.table_creation_date_time

        out["table_creation_date_time"] = (
            aws_sdk_dynamodb.types.table_creation_date_time.deserialize_aws_json_1_0(
                data["TableCreationDateTime"]
            )
        )
    else:
        raise DeserializationError(
            "SourceTableDetails.table_creation_date_time required"
        )
    if "ProvisionedThroughput" in data:
        import aws_sdk_dynamodb.types.provisioned_throughput

        out["provisioned_throughput"] = (
            aws_sdk_dynamodb.types.provisioned_throughput.deserialize_aws_json_1_0(
                data["ProvisionedThroughput"]
            )
        )
    else:
        raise DeserializationError("SourceTableDetails.provisioned_throughput required")
    if "OnDemandThroughput" in data:
        import aws_sdk_dynamodb.types.on_demand_throughput

        out["on_demand_throughput"] = (
            aws_sdk_dynamodb.types.on_demand_throughput.deserialize_aws_json_1_0(
                data["OnDemandThroughput"]
            )
        )
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    if "BillingMode" in data:
        import aws_sdk_dynamodb.types.billing_mode

        out["billing_mode"] = (
            aws_sdk_dynamodb.types.billing_mode.deserialize_aws_json_1_0(
                data["BillingMode"]
            )
        )
    return out
