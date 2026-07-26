"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateAssertionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.assertion_text
    import capo_resiliencehubv2.types.client_token


class CreateAssertionRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    text: "capo_resiliencehubv2.types.assertion_text.AssertionText"
    """<p>The text content of the assertion.</p>"""
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssertionRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["text"] = value["text"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAssertionRequest:
    out: CreateAssertionRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("CreateAssertionRequest.service_arn required")
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("CreateAssertionRequest.text required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
