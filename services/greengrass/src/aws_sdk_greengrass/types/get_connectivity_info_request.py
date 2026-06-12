"""Generated from Smithy shape ``com.amazonaws.greengrass#GetConnectivityInfoRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetConnectivityInfoRequest(TypedDict):
    thing_name: "aws_sdk_greengrass.types.__string.__string"
    """The thing name."""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectivityInfoRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectivityInfoRequest:
    out: GetConnectivityInfoRequest = {}  # type: ignore[typeddict-item]
    return out
