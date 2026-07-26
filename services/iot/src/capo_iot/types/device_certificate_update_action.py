"""Generated from Smithy shape ``com.amazonaws.iot#DeviceCertificateUpdateAction``."""

from typing import Literal, TypeAlias, cast

DeviceCertificateUpdateAction: TypeAlias = Literal["DEACTIVATE",]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceCertificateUpdateAction) -> str:
    return value


def deserialize_json(data: str) -> DeviceCertificateUpdateAction:
    return cast(DeviceCertificateUpdateAction, data)
