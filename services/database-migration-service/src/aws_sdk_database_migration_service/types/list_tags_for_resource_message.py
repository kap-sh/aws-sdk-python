"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ListTagsForResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.arn_list
    import aws_sdk_database_migration_service.types.string


class ListTagsForResourceMessage(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) string that uniquely identifies the DMS resource to list tags for. This returns a list of keys (names of tags) created for the resource and their associated tag values.</p>"""
    resource_arn_list: NotRequired[
        "aws_sdk_database_migration_service.types.arn_list.ArnList"
    ]
    """<p>List of ARNs that identify multiple DMS resources that you want to list tags for. This returns a list of keys (tag names) and their associated tag values. It also returns each tag's associated <code>ResourceArn</code> value, which is the ARN of the resource for which each listed tag is created. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceMessage) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_arn_list" in value:
        import aws_sdk_database_migration_service.types.arn_list

        out["ResourceArnList"] = (
            aws_sdk_database_migration_service.types.arn_list.serialize_aws_json_1_1(
                value["resource_arn_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceMessage:
    out: ListTagsForResourceMessage = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceArnList" in data:
        import aws_sdk_database_migration_service.types.arn_list

        out["resource_arn_list"] = (
            aws_sdk_database_migration_service.types.arn_list.deserialize_aws_json_1_1(
                data["ResourceArnList"]
            )
        )
    return out
