"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AddTagsToResourceMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.tag_list


class AddTagsToResourceMessage(TypedDict):
    resource_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>Identifies the DMS resource to which tags should be added. The value for this parameter is an Amazon Resource Name (ARN).</p> <p>For DMS, you can tag a replication instance, an endpoint, or a replication task.</p>"""
    tags: "aws_sdk_database_migration_service.types.tag_list.TagList"
    """<p>One or more tags to be assigned to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToResourceMessage) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_database_migration_service.types.tag_list

    out["Tags"] = (
        aws_sdk_database_migration_service.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToResourceMessage:
    out: AddTagsToResourceMessage = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("AddTagsToResourceMessage.resource_arn required")
    if "Tags" in data:
        import aws_sdk_database_migration_service.types.tag_list

        out["tags"] = (
            aws_sdk_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("AddTagsToResourceMessage.tags required")
    return out
