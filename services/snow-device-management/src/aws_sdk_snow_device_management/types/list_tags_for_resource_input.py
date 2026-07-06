"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ListTagsForResourceInput``."""

from typing_extensions import TypedDict


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the device or task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
