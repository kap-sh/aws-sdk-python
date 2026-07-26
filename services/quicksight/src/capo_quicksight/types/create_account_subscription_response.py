"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAccountSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.signup_response
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class CreateAccountSubscriptionResponse(TypedDict, closed=True):
    signup_response: NotRequired["capo_quicksight.types.signup_response.SignupResponse"]
    """<p>A <code>SignupResponse</code> object that returns information about a newly created Quick Sight account.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountSubscriptionResponse) -> dict:
    out: dict = {}
    if "signup_response" in value:
        import capo_quicksight.types.signup_response

        out["SignupResponse"] = capo_quicksight.types.signup_response.serialize_json(
            value["signup_response"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateAccountSubscriptionResponse:
    out: CreateAccountSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "SignupResponse" in data:
        import capo_quicksight.types.signup_response

        out["signup_response"] = capo_quicksight.types.signup_response.deserialize_json(
            data["SignupResponse"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
