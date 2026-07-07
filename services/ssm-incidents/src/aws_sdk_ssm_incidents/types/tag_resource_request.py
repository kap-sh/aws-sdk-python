"""Generated from Smithy shape ``com.amazonaws.ssmincidents#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the response plan you're adding the tags to.</p>"""
    tags: "aws_sdk_ssm_incidents.types.tag_map.TagMap"
    """<p>A list of tags to add to the response plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.tag_map

    out["tags"] = aws_sdk_ssm_incidents.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_ssm_incidents.types.tag_map

        out["tags"] = aws_sdk_ssm_incidents.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
