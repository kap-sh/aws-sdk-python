"""Generated from Smithy shape ``com.amazonaws.connect#FailedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.failure_reason_code
    import capo_connect.types.request_identifier
    import capo_connect.types.string


class FailedRequest(TypedDict, closed=True):
    request_identifier: NotRequired[
        "capo_connect.types.request_identifier.RequestIdentifier"
    ]
    """<p>Request identifier provided in the API call in the ContactDataRequest to create a contact.</p>"""
    failure_reason_code: NotRequired[
        "capo_connect.types.failure_reason_code.FailureReasonCode"
    ]
    """<p>Reason code for the failure.</p>"""
    failure_reason_message: NotRequired["capo_connect.types.string.String"]
    """<p>Why the request to create a contact failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedRequest) -> dict:
    out: dict = {}
    if "request_identifier" in value:
        out["RequestIdentifier"] = value["request_identifier"]
    if "failure_reason_code" in value:
        import capo_connect.types.failure_reason_code

        out["FailureReasonCode"] = (
            capo_connect.types.failure_reason_code.serialize_json(
                value["failure_reason_code"]
            )
        )
    if "failure_reason_message" in value:
        out["FailureReasonMessage"] = value["failure_reason_message"]
    return out


def deserialize_json(data: dict) -> FailedRequest:
    out: FailedRequest = {}  # type: ignore[typeddict-item]
    if "RequestIdentifier" in data:
        out["request_identifier"] = data["RequestIdentifier"]
    if "FailureReasonCode" in data:
        import capo_connect.types.failure_reason_code

        out["failure_reason_code"] = (
            capo_connect.types.failure_reason_code.deserialize_json(
                data["FailureReasonCode"]
            )
        )
    if "FailureReasonMessage" in data:
        out["failure_reason_message"] = data["FailureReasonMessage"]
    return out
