"""Generated from Smithy shape ``com.amazonaws.mpa#GetSessionResponseApproverResponses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.get_session_response_approver_response

GetSessionResponseApproverResponses: TypeAlias = list[
    "capo_mpa.types.get_session_response_approver_response.GetSessionResponseApproverResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponseApproverResponses) -> list:
    import capo_mpa.types.get_session_response_approver_response

    out: list = []
    for item in value:
        out.append(
            capo_mpa.types.get_session_response_approver_response.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GetSessionResponseApproverResponses:
    import capo_mpa.types.get_session_response_approver_response

    out: GetSessionResponseApproverResponses = []
    for item in data:
        out.append(
            capo_mpa.types.get_session_response_approver_response.deserialize_json(item)
        )
    return out
