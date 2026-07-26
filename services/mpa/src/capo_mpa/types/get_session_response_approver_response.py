"""Generated from Smithy shape ``com.amazonaws.mpa#GetSessionResponseApproverResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.identity_id
    import capo_mpa.types.iso_timestamp
    import capo_mpa.types.participant_id
    import capo_mpa.types.session_response
    import capo_mpa.types.string


class GetSessionResponseApproverResponse(TypedDict, closed=True):
    approver_id: NotRequired["capo_mpa.types.participant_id.ParticipantId"]
    """<p>ID for the approver.</p>"""
    identity_source_arn: NotRequired["capo_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the identity source. The identity source manages the user authentication for approvers.</p>"""
    identity_id: NotRequired["capo_mpa.types.identity_id.IdentityId"]
    """<p>ID for the identity source. The identity source manages the user authentication for approvers.</p>"""
    response: NotRequired["capo_mpa.types.session_response.SessionResponse"]
    """<p>Response to the operation request.</p>"""
    response_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when a approver responded to the operation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponseApproverResponse) -> dict:
    out: dict = {}
    if "approver_id" in value:
        out["ApproverId"] = value["approver_id"]
    if "identity_source_arn" in value:
        out["IdentitySourceArn"] = value["identity_source_arn"]
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "response" in value:
        import capo_mpa.types.session_response

        out["Response"] = capo_mpa.types.session_response.serialize_json(
            value["response"]
        )
    if "response_time" in value:
        import capo_mpa.types.iso_timestamp

        out["ResponseTime"] = capo_mpa.types.iso_timestamp.serialize_json(
            value["response_time"]
        )
    return out


def deserialize_json(data: dict) -> GetSessionResponseApproverResponse:
    out: GetSessionResponseApproverResponse = {}  # type: ignore[typeddict-item]
    if "ApproverId" in data:
        out["approver_id"] = data["ApproverId"]
    if "IdentitySourceArn" in data:
        out["identity_source_arn"] = data["IdentitySourceArn"]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    if "Response" in data:
        import capo_mpa.types.session_response

        out["response"] = capo_mpa.types.session_response.deserialize_json(
            data["Response"]
        )
    if "ResponseTime" in data:
        import capo_mpa.types.iso_timestamp

        out["response_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["ResponseTime"]
        )
    return out
