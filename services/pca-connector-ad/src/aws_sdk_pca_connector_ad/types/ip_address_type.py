"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

IpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUALSTACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "DUALSTACK",
    )
)


def serialize_json(value: IpAddressType) -> str:
    return value


def deserialize_json(data: str) -> IpAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpAddressType value: {data!r}")
    return cast(IpAddressType, data)
