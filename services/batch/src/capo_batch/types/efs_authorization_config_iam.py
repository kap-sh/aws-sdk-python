"""Generated from Smithy shape ``com.amazonaws.batch#EFSAuthorizationConfigIAM``."""

from typing import Literal, TypeAlias, cast

EFSAuthorizationConfigIAM: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EFSAuthorizationConfigIAM) -> str:
    return value


def deserialize_json(data: str) -> EFSAuthorizationConfigIAM:
    return cast(EFSAuthorizationConfigIAM, data)
