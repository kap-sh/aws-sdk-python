"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceConfigurableAudioChannelPairProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Property of InputDeviceConfigurableAudioChannelPairConfig, which configures one audio channel that the device produces."""
InputDeviceConfigurableAudioChannelPairProfile: TypeAlias = Literal[
    "DISABLED",
    "VBR-AAC_HHE-16000",
    "VBR-AAC_HE-64000",
    "VBR-AAC_LC-128000",
    "CBR-AAC_HQ-192000",
    "CBR-AAC_HQ-256000",
    "CBR-AAC_HQ-384000",
    "CBR-AAC_HQ-512000",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "VBR-AAC_HHE-16000",
        "VBR-AAC_HE-64000",
        "VBR-AAC_LC-128000",
        "CBR-AAC_HQ-192000",
        "CBR-AAC_HQ-256000",
        "CBR-AAC_HQ-384000",
        "CBR-AAC_HQ-512000",
    )
)


def serialize_json(value: InputDeviceConfigurableAudioChannelPairProfile) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceConfigurableAudioChannelPairProfile:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InputDeviceConfigurableAudioChannelPairProfile value: {data!r}"
        )
    return cast(InputDeviceConfigurableAudioChannelPairProfile, data)
