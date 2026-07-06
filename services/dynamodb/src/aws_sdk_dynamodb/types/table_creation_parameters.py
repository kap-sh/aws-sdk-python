"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableCreationParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_definitions
    import aws_sdk_dynamodb.types.billing_mode
    import aws_sdk_dynamodb.types.global_secondary_index_list
    import aws_sdk_dynamodb.types.key_schema
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.provisioned_throughput
    import aws_sdk_dynamodb.types.sse_specification
    import aws_sdk_dynamodb.types.table_name


class TableCreationParameters(TypedDict, closed=True):
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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableCreationParameters) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    import aws_sdk_dynamodb.types.attribute_definitions

    out["AttributeDefinitions"] = (
        aws_sdk_dynamodb.types.attribute_definitions.serialize_aws_json_1_0(
            value["attribute_definitions"]
        )
    )
    import aws_sdk_dynamodb.types.key_schema

    out["KeySchema"] = aws_sdk_dynamodb.types.key_schema.serialize_aws_json_1_0(
        value["key_schema"]
    )
    if "billing_mode" in value:
        import aws_sdk_dynamodb.types.billing_mode

        out["BillingMode"] = aws_sdk_dynamodb.types.billing_mode.serialize_aws_json_1_0(
            value["billing_mode"]
        )
    if "provisioned_throughput" in value:
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
    if "sse_specification" in value:
        import aws_sdk_dynamodb.types.sse_specification

        out["SSESpecification"] = (
            aws_sdk_dynamodb.types.sse_specification.serialize_aws_json_1_0(
                value["sse_specification"]
            )
        )
    if "global_secondary_indexes" in value:
        import aws_sdk_dynamodb.types.global_secondary_index_list

        out["GlobalSecondaryIndexes"] = (
            aws_sdk_dynamodb.types.global_secondary_index_list.serialize_aws_json_1_0(
                value["global_secondary_indexes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TableCreationParameters:
    out: TableCreationParameters = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("TableCreationParameters.table_name required")
    if "AttributeDefinitions" in data:
        import aws_sdk_dynamodb.types.attribute_definitions

        out["attribute_definitions"] = (
            aws_sdk_dynamodb.types.attribute_definitions.deserialize_aws_json_1_0(
                data["AttributeDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "TableCreationParameters.attribute_definitions required"
        )
    if "KeySchema" in data:
        import aws_sdk_dynamodb.types.key_schema

        out["key_schema"] = aws_sdk_dynamodb.types.key_schema.deserialize_aws_json_1_0(
            data["KeySchema"]
        )
    else:
        raise DeserializationError("TableCreationParameters.key_schema required")
    if "BillingMode" in data:
        import aws_sdk_dynamodb.types.billing_mode

        out["billing_mode"] = (
            aws_sdk_dynamodb.types.billing_mode.deserialize_aws_json_1_0(
                data["BillingMode"]
            )
        )
    if "ProvisionedThroughput" in data:
        import aws_sdk_dynamodb.types.provisioned_throughput

        out["provisioned_throughput"] = (
            aws_sdk_dynamodb.types.provisioned_throughput.deserialize_aws_json_1_0(
                data["ProvisionedThroughput"]
            )
        )
    if "OnDemandThroughput" in data:
        import aws_sdk_dynamodb.types.on_demand_throughput

        out["on_demand_throughput"] = (
            aws_sdk_dynamodb.types.on_demand_throughput.deserialize_aws_json_1_0(
                data["OnDemandThroughput"]
            )
        )
    if "SSESpecification" in data:
        import aws_sdk_dynamodb.types.sse_specification

        out["sse_specification"] = (
            aws_sdk_dynamodb.types.sse_specification.deserialize_aws_json_1_0(
                data["SSESpecification"]
            )
        )
    if "GlobalSecondaryIndexes" in data:
        import aws_sdk_dynamodb.types.global_secondary_index_list

        out["global_secondary_indexes"] = (
            aws_sdk_dynamodb.types.global_secondary_index_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexes"]
            )
        )
    return out
