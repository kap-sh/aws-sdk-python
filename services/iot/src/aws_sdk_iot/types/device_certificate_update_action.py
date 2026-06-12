"""Generated from Smithy shape ``com.amazonaws.iot#DeviceCertificateUpdateAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DeviceCertificateUpdateAction: TypeAlias = Literal["DEACTIVATE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEACTIVATE",))


def serialize_json(value: DeviceCertificateUpdateAction) -> str:
    return value


def deserialize_json(data: str) -> DeviceCertificateUpdateAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeviceCertificateUpdateAction value: {data!r}"
        )
    return cast(DeviceCertificateUpdateAction, data)
