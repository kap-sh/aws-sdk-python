"""Generated from Smithy shape ``com.amazonaws.medicalimaging#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.arn
    import aws_sdk_medical_imaging.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_medical_imaging.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from.</p>"""
    tag_keys: "aws_sdk_medical_imaging.types.tag_key_list.TagKeyList"
    """<p>The keys for the tags to be removed from the medical imaging resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
