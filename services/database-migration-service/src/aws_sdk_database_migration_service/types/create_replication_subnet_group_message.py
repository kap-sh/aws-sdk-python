"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateReplicationSubnetGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.subnet_identifier_list
    import aws_sdk_database_migration_service.types.tag_list


class CreateReplicationSubnetGroupMessage(TypedDict):
    replication_subnet_group_identifier: (
        "aws_sdk_database_migration_service.types.string.String"
    )
    r"""<p>The name for the replication subnet group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, or hyphens. Must not be \"default\".</p> <p>Example: <code>mySubnetgroup</code> </p>"""
    replication_subnet_group_description: (
        "aws_sdk_database_migration_service.types.string.String"
    )
    """<p>The description for the subnet group. </p> <p>Constraints: This parameter Must not contain non-printable control characters.</p>"""
    subnet_ids: "aws_sdk_database_migration_service.types.subnet_identifier_list.SubnetIdentifierList"
    """<p>Two or more subnet IDs to be assigned to the subnet group.</p>"""
    tags: NotRequired["aws_sdk_database_migration_service.types.tag_list.TagList"]
    """<p>One or more tags to be assigned to the subnet group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReplicationSubnetGroupMessage) -> dict:
    out: dict = {}
    out["ReplicationSubnetGroupIdentifier"] = value[
        "replication_subnet_group_identifier"
    ]
    out["ReplicationSubnetGroupDescription"] = value[
        "replication_subnet_group_description"
    ]
    import aws_sdk_database_migration_service.types.subnet_identifier_list

    out["SubnetIds"] = (
        aws_sdk_database_migration_service.types.subnet_identifier_list.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    )
    if "tags" in value:
        import aws_sdk_database_migration_service.types.tag_list

        out["Tags"] = (
            aws_sdk_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReplicationSubnetGroupMessage:
    out: CreateReplicationSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationSubnetGroupIdentifier" in data:
        out["replication_subnet_group_identifier"] = data[
            "ReplicationSubnetGroupIdentifier"
        ]
    else:
        raise DeserializationError(
            "CreateReplicationSubnetGroupMessage.replication_subnet_group_identifier required"
        )
    if "ReplicationSubnetGroupDescription" in data:
        out["replication_subnet_group_description"] = data[
            "ReplicationSubnetGroupDescription"
        ]
    else:
        raise DeserializationError(
            "CreateReplicationSubnetGroupMessage.replication_subnet_group_description required"
        )
    if "SubnetIds" in data:
        import aws_sdk_database_migration_service.types.subnet_identifier_list

        out["subnet_ids"] = (
            aws_sdk_database_migration_service.types.subnet_identifier_list.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateReplicationSubnetGroupMessage.subnet_ids required"
        )
    if "Tags" in data:
        import aws_sdk_database_migration_service.types.tag_list

        out["tags"] = (
            aws_sdk_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    return out
