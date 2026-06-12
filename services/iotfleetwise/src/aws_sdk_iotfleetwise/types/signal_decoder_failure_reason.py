"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalDecoderFailureReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

SignalDecoderFailureReason: TypeAlias = Literal[
    "DUPLICATE_SIGNAL",
    "CONFLICTING_SIGNAL",
    "SIGNAL_TO_ADD_ALREADY_EXISTS",
    "SIGNAL_NOT_ASSOCIATED_WITH_NETWORK_INTERFACE",
    "NETWORK_INTERFACE_TYPE_INCOMPATIBLE_WITH_SIGNAL_DECODER_TYPE",
    "SIGNAL_NOT_IN_MODEL",
    "CAN_SIGNAL_INFO_IS_NULL",
    "OBD_SIGNAL_INFO_IS_NULL",
    "NO_DECODER_INFO_FOR_SIGNAL_IN_MODEL",
    "MESSAGE_SIGNAL_INFO_IS_NULL",
    "SIGNAL_DECODER_TYPE_INCOMPATIBLE_WITH_MESSAGE_SIGNAL_TYPE",
    "STRUCT_SIZE_MISMATCH",
    "NO_SIGNAL_IN_CATALOG_FOR_DECODER_SIGNAL",
    "SIGNAL_DECODER_INCOMPATIBLE_WITH_SIGNAL_CATALOG",
    "EMPTY_MESSAGE_SIGNAL",
    "CUSTOM_DECODING_SIGNAL_INFO_IS_NULL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DUPLICATE_SIGNAL",
        "CONFLICTING_SIGNAL",
        "SIGNAL_TO_ADD_ALREADY_EXISTS",
        "SIGNAL_NOT_ASSOCIATED_WITH_NETWORK_INTERFACE",
        "NETWORK_INTERFACE_TYPE_INCOMPATIBLE_WITH_SIGNAL_DECODER_TYPE",
        "SIGNAL_NOT_IN_MODEL",
        "CAN_SIGNAL_INFO_IS_NULL",
        "OBD_SIGNAL_INFO_IS_NULL",
        "NO_DECODER_INFO_FOR_SIGNAL_IN_MODEL",
        "MESSAGE_SIGNAL_INFO_IS_NULL",
        "SIGNAL_DECODER_TYPE_INCOMPATIBLE_WITH_MESSAGE_SIGNAL_TYPE",
        "STRUCT_SIZE_MISMATCH",
        "NO_SIGNAL_IN_CATALOG_FOR_DECODER_SIGNAL",
        "SIGNAL_DECODER_INCOMPATIBLE_WITH_SIGNAL_CATALOG",
        "EMPTY_MESSAGE_SIGNAL",
        "CUSTOM_DECODING_SIGNAL_INFO_IS_NULL",
    )
)


def serialize_aws_json_1_0(value: SignalDecoderFailureReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SignalDecoderFailureReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SignalDecoderFailureReason value: {data!r}"
        )
    return cast(SignalDecoderFailureReason, data)
