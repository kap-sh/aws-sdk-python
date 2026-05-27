"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableCreationParameters``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_definitions
    import aws_sdk_dynamodb.types.billing_mode
    import aws_sdk_dynamodb.types.global_secondary_index_list
    import aws_sdk_dynamodb.types.key_schema
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.provisioned_throughput
    import aws_sdk_dynamodb.types.sse_specification
    import aws_sdk_dynamodb.types.table_name


class TableCreationParameters(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p> The name of the table created as part of the import operation. </p>"""
    attribute_definitions: (
        "aws_sdk_dynamodb.types.attribute_definitions.AttributeDefinitions"
    )
    """<p> The attributes of the table created as part of the import operation. </p>"""
    key_schema: "aws_sdk_dynamodb.types.key_schema.KeySchema"
    """<p> The primary key and option sort key of the table created as part of the import operation. </p>"""
    billing_mode: NotRequired["aws_sdk_dynamodb.types.billing_mode.BillingMode"]
    """<p> The billing mode for provisioning the table created as part of the import operation. </p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    on_demand_throughput: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    sse_specification: NotRequired[
        "aws_sdk_dynamodb.types.sse_specification.SSESpecification"
    ]
    global_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.global_secondary_index_list.GlobalSecondaryIndexList"
    ]
    """<p> The Global Secondary Indexes (GSI) of the table to be created as part of the import operation. </p>"""
