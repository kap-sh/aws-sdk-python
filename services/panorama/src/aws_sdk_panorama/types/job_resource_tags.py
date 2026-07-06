"""Generated from Smithy shape ``com.amazonaws.panorama#JobResourceTags``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.job_resource_type
    import aws_sdk_panorama.types.tag_map


class JobResourceTags(TypedDict, closed=True):
    resource_type: "aws_sdk_panorama.types.job_resource_type.JobResourceType"
    """<p>The job's type.</p>"""
    tags: "aws_sdk_panorama.types.tag_map.TagMap"
    """<p>The job's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobResourceTags) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    import aws_sdk_panorama.types.tag_map

    out["Tags"] = aws_sdk_panorama.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> JobResourceTags:
    out: JobResourceTags = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("JobResourceTags.resource_type required")
    if "Tags" in data:
        import aws_sdk_panorama.types.tag_map

        out["tags"] = aws_sdk_panorama.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("JobResourceTags.tags required")
    return out
