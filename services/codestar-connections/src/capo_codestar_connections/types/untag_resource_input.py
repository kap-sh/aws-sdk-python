"""Generated from Smithy shape ``com.amazonaws.codestarconnections#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_connections.types.amazon_resource_name
    import capo_codestar_connections.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: (
        "capo_codestar_connections.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>"""
    tag_keys: "capo_codestar_connections.types.tag_key_list.TagKeyList"
    """<p>The list of keys for the tags to be removed from the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_codestar_connections.types.tag_key_list

    out["TagKeys"] = (
        capo_codestar_connections.types.tag_key_list.serialize_aws_json_1_0(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "TagKeys" in data:
        import capo_codestar_connections.types.tag_key_list

        out["tag_keys"] = (
            capo_codestar_connections.types.tag_key_list.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
