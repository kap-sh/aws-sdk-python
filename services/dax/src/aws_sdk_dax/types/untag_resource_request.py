"""Generated from Smithy shape ``com.amazonaws.dax#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dax.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dax.types.key_list
    import aws_sdk_dax.types.string


class UntagResourceRequest(TypedDict):
    resource_name: "aws_sdk_dax.types.string.String"
    """<p>The name of the DAX resource from which the tags should be removed.</p>"""
    tag_keys: "aws_sdk_dax.types.key_list.KeyList"
    """<p>A list of tag keys. If the DAX cluster has any tags with these keys, then the tags are removed from the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceName"] = value["resource_name"]
    import aws_sdk_dax.types.key_list

    out["TagKeys"] = aws_sdk_dax.types.key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_name required")
    if "TagKeys" in data:
        import aws_sdk_dax.types.key_list

        out["tag_keys"] = aws_sdk_dax.types.key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
