"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderErrorMasking``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rtbfabric.types.responder_error_masking_for_http_code

ResponderErrorMasking: TypeAlias = list[
    "capo_rtbfabric.types.responder_error_masking_for_http_code.ResponderErrorMaskingForHttpCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponderErrorMasking) -> list:
    import capo_rtbfabric.types.responder_error_masking_for_http_code

    out: list = []
    for item in value:
        out.append(
            capo_rtbfabric.types.responder_error_masking_for_http_code.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResponderErrorMasking:
    import capo_rtbfabric.types.responder_error_masking_for_http_code

    out: ResponderErrorMasking = []
    for item in data:
        out.append(
            capo_rtbfabric.types.responder_error_masking_for_http_code.deserialize_json(
                item
            )
        )
    return out
