"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeSdiSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeSdiSourceRequest(TypedDict):
    sdi_source_id: "aws_sdk_medialive.types.__string.__string"
    """Get details about an SdiSource."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSdiSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSdiSourceRequest:
    out: DescribeSdiSourceRequest = {}  # type: ignore[typeddict-item]
    return out
