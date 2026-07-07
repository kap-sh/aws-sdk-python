"""Generated from Smithy shape ``com.amazonaws.backupgateway#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.resource_arn
    import aws_sdk_backup_gateway.types.tag_keys


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_backup_gateway.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>"""
    tag_keys: "aws_sdk_backup_gateway.types.tag_keys.TagKeys"
    """<p>The list of tag keys specifying which tags to remove.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_backup_gateway.types.tag_keys

    out["TagKeys"] = aws_sdk_backup_gateway.types.tag_keys.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_backup_gateway.types.tag_keys

        out["tag_keys"] = (
            aws_sdk_backup_gateway.types.tag_keys.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
