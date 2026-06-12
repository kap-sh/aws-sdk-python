"""Generated from Smithy shape ``com.amazonaws.iot#HttpUrlDestinationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.url


class HttpUrlDestinationConfiguration(TypedDict):
    confirmation_url: "aws_sdk_iot.types.url.Url"
    """<p>The URL IoT uses to confirm ownership of or access to the topic rule destination URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpUrlDestinationConfiguration) -> dict:
    out: dict = {}
    out["confirmationUrl"] = value["confirmation_url"]
    return out


def deserialize_json(data: dict) -> HttpUrlDestinationConfiguration:
    out: HttpUrlDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "confirmationUrl" in data:
        out["confirmation_url"] = data["confirmationUrl"]
    else:
        raise DeserializationError(
            "HttpUrlDestinationConfiguration.confirmation_url required"
        )
    return out
