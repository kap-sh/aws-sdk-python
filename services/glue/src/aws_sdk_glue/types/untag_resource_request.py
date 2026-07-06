"""Generated from Smithy shape ``com.amazonaws.glue#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.tag_keys_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource from which to remove the tags.</p>"""
    tags_to_remove: "aws_sdk_glue.types.tag_keys_list.TagKeysList"
    """<p>Tags to remove from this resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_glue.types.tag_keys_list

    out["TagsToRemove"] = aws_sdk_glue.types.tag_keys_list.serialize_aws_json_1_1(
        value["tags_to_remove"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagsToRemove" in data:
        import aws_sdk_glue.types.tag_keys_list

        out["tags_to_remove"] = (
            aws_sdk_glue.types.tag_keys_list.deserialize_aws_json_1_1(
                data["TagsToRemove"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tags_to_remove required")
    return out
