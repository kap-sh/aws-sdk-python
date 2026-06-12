"""Generated from Smithy shape ``com.amazonaws.xray#ResourceARNDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.string


class ResourceARNDetail(TypedDict):
    arn: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The ARN of a corresponding resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceARNDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ResourceARNDetail:
    out: ResourceARNDetail = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    return out
