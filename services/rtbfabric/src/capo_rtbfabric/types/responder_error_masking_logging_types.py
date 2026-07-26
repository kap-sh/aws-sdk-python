"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderErrorMaskingLoggingTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rtbfabric.types.responder_error_masking_logging_type

ResponderErrorMaskingLoggingTypes: TypeAlias = list[
    "capo_rtbfabric.types.responder_error_masking_logging_type.ResponderErrorMaskingLoggingType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponderErrorMaskingLoggingTypes) -> list:
    import capo_rtbfabric.types.responder_error_masking_logging_type

    out: list = []
    for item in value:
        out.append(
            capo_rtbfabric.types.responder_error_masking_logging_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResponderErrorMaskingLoggingTypes:
    import capo_rtbfabric.types.responder_error_masking_logging_type

    out: ResponderErrorMaskingLoggingTypes = []
    for item in data:
        out.append(
            capo_rtbfabric.types.responder_error_masking_logging_type.deserialize_json(
                item
            )
        )
    return out
