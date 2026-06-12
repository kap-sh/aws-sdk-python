"""Generated from Smithy shape ``com.amazonaws.mediatailor#DefaultSegmentDeliveryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DefaultSegmentDeliveryConfiguration(TypedDict):
    base_url: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The hostname of the server that will be used to serve segments. This string must include the protocol, such as <b>https://</b>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultSegmentDeliveryConfiguration) -> dict:
    out: dict = {}
    if "base_url" in value:
        out["BaseUrl"] = value["base_url"]
    return out


def deserialize_json(data: dict) -> DefaultSegmentDeliveryConfiguration:
    out: DefaultSegmentDeliveryConfiguration = {}  # type: ignore[typeddict-item]
    if "BaseUrl" in data:
        out["base_url"] = data["BaseUrl"]
    return out
