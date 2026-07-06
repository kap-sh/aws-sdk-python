"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string


class GetSubscriptionRequest(TypedDict, closed=True):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSubscriptionRequest:
    out: GetSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
