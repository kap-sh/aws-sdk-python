"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableWitnessGroupUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.create_global_table_witness_group_member_action
    import aws_sdk_dynamodb.types.delete_global_table_witness_group_member_action


class GlobalTableWitnessGroupUpdate(TypedDict):
    create: NotRequired[
        "aws_sdk_dynamodb.types.create_global_table_witness_group_member_action.CreateGlobalTableWitnessGroupMemberAction"
    ]
    """<p>Specifies a witness Region to be added to a new MRSC global table. The witness must be added when creating the MRSC global table.</p>"""
    delete: NotRequired[
        "aws_sdk_dynamodb.types.delete_global_table_witness_group_member_action.DeleteGlobalTableWitnessGroupMemberAction"
    ]
    """<p>Specifies a witness Region to be removed from an existing global table. Must be done in conjunction with removing a replica. The deletion of both a witness and replica converts the remaining replica to a single-Region DynamoDB table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableWitnessGroupUpdate) -> dict:
    out: dict = {}
    if "create" in value:
        import aws_sdk_dynamodb.types.create_global_table_witness_group_member_action

        out["Create"] = (
            aws_sdk_dynamodb.types.create_global_table_witness_group_member_action.serialize_aws_json_1_0(
                value["create"]
            )
        )
    if "delete" in value:
        import aws_sdk_dynamodb.types.delete_global_table_witness_group_member_action

        out["Delete"] = (
            aws_sdk_dynamodb.types.delete_global_table_witness_group_member_action.serialize_aws_json_1_0(
                value["delete"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalTableWitnessGroupUpdate:
    out: GlobalTableWitnessGroupUpdate = {}  # type: ignore[typeddict-item]
    if "Create" in data:
        import aws_sdk_dynamodb.types.create_global_table_witness_group_member_action

        out["create"] = (
            aws_sdk_dynamodb.types.create_global_table_witness_group_member_action.deserialize_aws_json_1_0(
                data["Create"]
            )
        )
    if "Delete" in data:
        import aws_sdk_dynamodb.types.delete_global_table_witness_group_member_action

        out["delete"] = (
            aws_sdk_dynamodb.types.delete_global_table_witness_group_member_action.deserialize_aws_json_1_0(
                data["Delete"]
            )
        )
    return out
