"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetTableAutoScalingSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.arn
    import aws_sdk_keyspaces.types.auto_scaling_specification
    import aws_sdk_keyspaces.types.keyspace_name
    import aws_sdk_keyspaces.types.replica_auto_scaling_specification_list
    import aws_sdk_keyspaces.types.table_name


class GetTableAutoScalingSettingsResponse(TypedDict, closed=True):
    keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace.</p>"""
    table_name: "aws_sdk_keyspaces.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    resource_arn: "aws_sdk_keyspaces.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    auto_scaling_specification: NotRequired[
        "aws_sdk_keyspaces.types.auto_scaling_specification.AutoScalingSpecification"
    ]
    """<p>The auto scaling settings of the table.</p>"""
    replica_specifications: NotRequired[
        "aws_sdk_keyspaces.types.replica_auto_scaling_specification_list.ReplicaAutoScalingSpecificationList"
    ]
    """<p>The Amazon Web Services Region specific settings of a multi-Region table. Returns the settings for all Regions the table is replicated in.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTableAutoScalingSettingsResponse) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    out["resourceArn"] = value["resource_arn"]
    if "auto_scaling_specification" in value:
        import aws_sdk_keyspaces.types.auto_scaling_specification

        out["autoScalingSpecification"] = (
            aws_sdk_keyspaces.types.auto_scaling_specification.serialize_aws_json_1_0(
                value["auto_scaling_specification"]
            )
        )
    if "replica_specifications" in value:
        import aws_sdk_keyspaces.types.replica_auto_scaling_specification_list

        out["replicaSpecifications"] = (
            aws_sdk_keyspaces.types.replica_auto_scaling_specification_list.serialize_aws_json_1_0(
                value["replica_specifications"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTableAutoScalingSettingsResponse:
    out: GetTableAutoScalingSettingsResponse = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError(
            "GetTableAutoScalingSettingsResponse.keyspace_name required"
        )
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError(
            "GetTableAutoScalingSettingsResponse.table_name required"
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "GetTableAutoScalingSettingsResponse.resource_arn required"
        )
    if "autoScalingSpecification" in data:
        import aws_sdk_keyspaces.types.auto_scaling_specification

        out["auto_scaling_specification"] = (
            aws_sdk_keyspaces.types.auto_scaling_specification.deserialize_aws_json_1_0(
                data["autoScalingSpecification"]
            )
        )
    if "replicaSpecifications" in data:
        import aws_sdk_keyspaces.types.replica_auto_scaling_specification_list

        out["replica_specifications"] = (
            aws_sdk_keyspaces.types.replica_auto_scaling_specification_list.deserialize_aws_json_1_0(
                data["replicaSpecifications"]
            )
        )
    return out
