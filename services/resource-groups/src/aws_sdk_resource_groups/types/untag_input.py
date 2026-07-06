"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UntagInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_arn_v2
    import aws_sdk_resource_groups.types.tag_key_list


class UntagInput(TypedDict, closed=True):
    arn: "aws_sdk_resource_groups.types.group_arn_v2.GroupArnV2"
    """<p>The Amazon resource name (ARN) of the resource group from which to remove tags. The command removed both the specified keys and any values associated with those keys.</p>"""
    keys: "aws_sdk_resource_groups.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagInput) -> dict:
    out: dict = {}
    import aws_sdk_resource_groups.types.tag_key_list

    out["Keys"] = aws_sdk_resource_groups.types.tag_key_list.serialize_json(
        value["keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagInput:
    out: UntagInput = {}  # type: ignore[typeddict-item]
    if "Keys" in data:
        import aws_sdk_resource_groups.types.tag_key_list

        out["keys"] = aws_sdk_resource_groups.types.tag_key_list.deserialize_json(
            data["Keys"]
        )
    else:
        raise DeserializationError("UntagInput.keys required")
    return out
