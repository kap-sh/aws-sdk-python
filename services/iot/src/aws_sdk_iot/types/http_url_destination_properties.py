"""Generated from Smithy shape ``com.amazonaws.iot#HttpUrlDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.url


class HttpUrlDestinationProperties(TypedDict, closed=True):
    confirmation_url: NotRequired["aws_sdk_iot.types.url.Url"]
    """<p>The URL used to confirm the HTTP topic rule destination URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpUrlDestinationProperties) -> dict:
    out: dict = {}
    if "confirmation_url" in value:
        out["confirmationUrl"] = value["confirmation_url"]
    return out


def deserialize_json(data: dict) -> HttpUrlDestinationProperties:
    out: HttpUrlDestinationProperties = {}  # type: ignore[typeddict-item]
    if "confirmationUrl" in data:
        out["confirmation_url"] = data["confirmationUrl"]
    return out
