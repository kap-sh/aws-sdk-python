"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeGlobalTableSettingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_settings_description_list
    import capo_dynamodb.types.table_name


class DescribeGlobalTableSettingsOutput(TypedDict, closed=True):
    global_table_name: NotRequired["capo_dynamodb.types.table_name.TableName"]
    """<p>The name of the global table.</p>"""
    replica_settings: NotRequired[
        "capo_dynamodb.types.replica_settings_description_list.ReplicaSettingsDescriptionList"
    ]
    """<p>The Region-specific settings for the global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeGlobalTableSettingsOutput) -> dict:
    out: dict = {}
    if "global_table_name" in value:
        out["GlobalTableName"] = value["global_table_name"]
    if "replica_settings" in value:
        import capo_dynamodb.types.replica_settings_description_list

        out["ReplicaSettings"] = (
            capo_dynamodb.types.replica_settings_description_list.serialize_aws_json_1_0(
                value["replica_settings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeGlobalTableSettingsOutput:
    out: DescribeGlobalTableSettingsOutput = {}  # type: ignore[typeddict-item]
    if "GlobalTableName" in data:
        out["global_table_name"] = data["GlobalTableName"]
    if "ReplicaSettings" in data:
        import capo_dynamodb.types.replica_settings_description_list

        out["replica_settings"] = (
            capo_dynamodb.types.replica_settings_description_list.deserialize_aws_json_1_0(
                data["ReplicaSettings"]
            )
        )
    return out
