"""Generated from Smithy shape ``com.amazonaws.appstream#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: NotRequired["capo_appstream.types.tag_key_list.TagKeyList"]
    """<p>The tag keys for the tags to disassociate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tag_keys" in value:
        import capo_appstream.types.tag_key_list

        out["TagKeys"] = capo_appstream.types.tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "TagKeys" in data:
        import capo_appstream.types.tag_key_list

        out["tag_keys"] = capo_appstream.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    return out
