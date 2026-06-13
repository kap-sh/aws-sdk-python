"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderErrorMaskingLoggingTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.responder_error_masking_logging_type

ResponderErrorMaskingLoggingTypes: TypeAlias = list[
    "aws_sdk_rtbfabric.types.responder_error_masking_logging_type.ResponderErrorMaskingLoggingType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponderErrorMaskingLoggingTypes) -> list:
    import aws_sdk_rtbfabric.types.responder_error_masking_logging_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rtbfabric.types.responder_error_masking_logging_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResponderErrorMaskingLoggingTypes:
    import aws_sdk_rtbfabric.types.responder_error_masking_logging_type

    out: ResponderErrorMaskingLoggingTypes = []
    for item in data:
        out.append(
            aws_sdk_rtbfabric.types.responder_error_masking_logging_type.deserialize_json(
                item
            )
        )
    return out
