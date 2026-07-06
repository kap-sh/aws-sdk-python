"""Generated from Smithy shape ``com.amazonaws.elementalinference#ClippingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.resource_description


class ClippingConfig(TypedDict, closed=True):
    callback_metadata: NotRequired[
        "aws_sdk_elementalinference.types.resource_description.ResourceDescription"
    ]
    """<p>A string that you want Elemental Inference to always include in the event clipping metadata for this output. The string might identify the sports event in the source media, for example. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClippingConfig) -> dict:
    out: dict = {}
    if "callback_metadata" in value:
        out["callbackMetadata"] = value["callback_metadata"]
    return out


def deserialize_json(data: dict) -> ClippingConfig:
    out: ClippingConfig = {}  # type: ignore[typeddict-item]
    if "callbackMetadata" in data:
        out["callback_metadata"] = data["callbackMetadata"]
    return out
