"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_quicksetup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.tags_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to tag.</p>"""
    tags: "aws_sdk_ssm_quicksetup.types.tags_map.TagsMap"
    """<p>Key-value pairs of metadata to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_ssm_quicksetup.types.tags_map

    out["Tags"] = aws_sdk_ssm_quicksetup.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_ssm_quicksetup.types.tags_map

        out["tags"] = aws_sdk_ssm_quicksetup.types.tags_map.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
