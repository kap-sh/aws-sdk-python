"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationStatusString``."""

from typing import Literal, TypeAlias, cast

ResaleAuthorizationStatusString: TypeAlias = Literal[
    "Draft",
    "Active",
    "Restricted",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationStatusString) -> str:
    return value


def deserialize_json(data: str) -> ResaleAuthorizationStatusString:
    return cast(ResaleAuthorizationStatusString, data)
