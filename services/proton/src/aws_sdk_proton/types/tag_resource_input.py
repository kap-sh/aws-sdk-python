"""Generated from Smithy shape ``com.amazonaws.proton#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.tag_list


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_proton.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Proton resource to apply customer tags to.</p>"""
    tags: "aws_sdk_proton.types.tag_list.TagList"
    """<p>A list of customer tags to apply to the Proton resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.tag_list

    out["tags"] = aws_sdk_proton.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_proton.types.tag_list

        out["tags"] = aws_sdk_proton.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
