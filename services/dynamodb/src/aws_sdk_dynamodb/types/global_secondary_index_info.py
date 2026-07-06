"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.key_schema
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.projection
    import aws_sdk_dynamodb.types.provisioned_throughput


class GlobalSecondaryIndexInfo(TypedDict, closed=True):
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index.</p>"""
    key_schema: NotRequired["aws_sdk_dynamodb.types.key_schema.KeySchema"]
    r"""<p>The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term \"hash attribute\" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term \"range attribute\" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note>"""
    projection: NotRequired["aws_sdk_dynamodb.types.projection.Projection"]
    """<p>Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. </p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>Represents the provisioned throughput settings for the specified global secondary index. </p>"""
    on_demand_throughput: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalSecondaryIndexInfo) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "key_schema" in value:
        import aws_sdk_dynamodb.types.key_schema

        out["KeySchema"] = aws_sdk_dynamodb.types.key_schema.serialize_aws_json_1_0(
            value["key_schema"]
        )
    if "projection" in value:
        import aws_sdk_dynamodb.types.projection

        out["Projection"] = aws_sdk_dynamodb.types.projection.serialize_aws_json_1_0(
            value["projection"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalSecondaryIndexInfo:
    out: GlobalSecondaryIndexInfo = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "KeySchema" in data:
        import aws_sdk_dynamodb.types.key_schema

        out["key_schema"] = aws_sdk_dynamodb.types.key_schema.deserialize_aws_json_1_0(
            data["KeySchema"]
        )
    if "Projection" in data:
        import aws_sdk_dynamodb.types.projection

        out["projection"] = aws_sdk_dynamodb.types.projection.deserialize_aws_json_1_0(
            data["Projection"]
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
    return out
