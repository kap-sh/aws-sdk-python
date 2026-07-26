"""Generated from Smithy shape ``com.amazonaws.backupgateway#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup_gateway.types.resource_arn
    import capo_backup_gateway.types.tags


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_backup_gateway.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "capo_backup_gateway.types.tags.Tags"
    """<p>A list of tags to assign to the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_backup_gateway.types.tags

    out["Tags"] = capo_backup_gateway.types.tags.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "Tags" in data:
        import capo_backup_gateway.types.tags

        out["tags"] = capo_backup_gateway.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
