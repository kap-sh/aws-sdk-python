"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DescribeNetworkRequest(TypedDict, closed=True):
    network_id: "capo_medialive.types.__string.__string"
    """The ID of the network."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeNetworkRequest:
    out: DescribeNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
