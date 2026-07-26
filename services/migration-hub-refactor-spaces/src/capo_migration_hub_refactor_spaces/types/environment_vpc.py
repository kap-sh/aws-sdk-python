"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#EnvironmentVpc``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.account_id
    import capo_migration_hub_refactor_spaces.types.cidr_blocks
    import capo_migration_hub_refactor_spaces.types.ec2_tag_value
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.timestamp
    import capo_migration_hub_refactor_spaces.types.vpc_id


class EnvironmentVpc(TypedDict, closed=True):
    environment_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    ]
    """<p>The unique identifier of the environment. </p>"""
    vpc_id: NotRequired["capo_migration_hub_refactor_spaces.types.vpc_id.VpcId"]
    """<p>The ID of the VPC. </p>"""
    account_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the virtual private cloud (VPC) owner. </p>"""
    cidr_blocks: NotRequired[
        "capo_migration_hub_refactor_spaces.types.cidr_blocks.CidrBlocks"
    ]
    """<p>The list of Amazon Virtual Private Cloud (Amazon VPC) CIDR blocks. </p>"""
    vpc_name: NotRequired[
        "capo_migration_hub_refactor_spaces.types.ec2_tag_value.Ec2TagValue"
    ]
    """<p>The name of the VPC at the time it is added to the environment. </p>"""
    last_updated_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the VPC was last updated by the environment. </p>"""
    created_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the VPC is first added to the environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentVpc) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "cidr_blocks" in value:
        import capo_migration_hub_refactor_spaces.types.cidr_blocks

        out["CidrBlocks"] = (
            capo_migration_hub_refactor_spaces.types.cidr_blocks.serialize_json(
                value["cidr_blocks"]
            )
        )
    if "vpc_name" in value:
        out["VpcName"] = value["vpc_name"]
    if "last_updated_time" in value:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["LastUpdatedTime"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    if "created_time" in value:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["CreatedTime"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["created_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentVpc:
    out: EnvironmentVpc = {}  # type: ignore[typeddict-item]
    if "EnvironmentId" in data:
        out["environment_id"] = data["EnvironmentId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "CidrBlocks" in data:
        import capo_migration_hub_refactor_spaces.types.cidr_blocks

        out["cidr_blocks"] = (
            capo_migration_hub_refactor_spaces.types.cidr_blocks.deserialize_json(
                data["CidrBlocks"]
            )
        )
    if "VpcName" in data:
        out["vpc_name"] = data["VpcName"]
    if "LastUpdatedTime" in data:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["last_updated_time"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    if "CreatedTime" in data:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["created_time"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["CreatedTime"]
            )
        )
    return out
