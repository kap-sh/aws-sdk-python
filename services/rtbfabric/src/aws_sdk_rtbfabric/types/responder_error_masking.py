"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderErrorMasking``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.responder_error_masking_for_http_code

ResponderErrorMasking: TypeAlias = list[
    "aws_sdk_rtbfabric.types.responder_error_masking_for_http_code.ResponderErrorMaskingForHttpCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponderErrorMasking) -> list:
    import aws_sdk_rtbfabric.types.responder_error_masking_for_http_code

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rtbfabric.types.responder_error_masking_for_http_code.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResponderErrorMasking:
    import aws_sdk_rtbfabric.types.responder_error_masking_for_http_code

    out: ResponderErrorMasking = []
    for item in data:
        out.append(
            aws_sdk_rtbfabric.types.responder_error_masking_for_http_code.deserialize_json(
                item
            )
        )
    return out
