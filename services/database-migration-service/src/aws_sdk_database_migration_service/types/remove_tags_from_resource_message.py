"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RemoveTagsFromResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.key_list
    import aws_sdk_database_migration_service.types.string


class RemoveTagsFromResourceMessage(TypedDict, closed=True):
    resource_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>An DMS resource from which you want to remove tag(s). The value for this parameter is an Amazon Resource Name (ARN).</p>"""
    tag_keys: "aws_sdk_database_migration_service.types.key_list.KeyList"
    """<p>The tag key (name) of the tag to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceMessage) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_database_migration_service.types.key_list

    out["TagKeys"] = (
        aws_sdk_database_migration_service.types.key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceMessage:
    out: RemoveTagsFromResourceMessage = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "RemoveTagsFromResourceMessage.resource_arn required"
        )
    if "TagKeys" in data:
        import aws_sdk_database_migration_service.types.key_list

        out["tag_keys"] = (
            aws_sdk_database_migration_service.types.key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("RemoveTagsFromResourceMessage.tag_keys required")
    return out
