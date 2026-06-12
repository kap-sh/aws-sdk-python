"""Generated from Smithy shape ``com.amazonaws.medicalimaging#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.arn
    import aws_sdk_medical_imaging.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_medical_imaging.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to.</p>"""
    tags: "aws_sdk_medical_imaging.types.tag_map.TagMap"
    """<p>The user-specified key and value tag pairs added to a medical imaging resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_medical_imaging.types.tag_map

    out["tags"] = aws_sdk_medical_imaging.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_medical_imaging.types.tag_map

        out["tags"] = aws_sdk_medical_imaging.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
