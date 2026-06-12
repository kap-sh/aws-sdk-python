"""Generated from Smithy shape ``com.amazonaws.backupgateway#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.resource_arn
    import aws_sdk_backup_gateway.types.tags


class ListTagsForResourceOutput(TypedDict):
    resource_arn: NotRequired["aws_sdk_backup_gateway.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource's tags that you listed.</p>"""
    tags: NotRequired["aws_sdk_backup_gateway.types.tags.Tags"]
    """<p>A list of the resource's tags.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import aws_sdk_backup_gateway.types.tags

        out["Tags"] = aws_sdk_backup_gateway.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Tags" in data:
        import aws_sdk_backup_gateway.types.tags

        out["tags"] = aws_sdk_backup_gateway.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
