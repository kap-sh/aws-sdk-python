"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateBrowserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_arn
    import capo_bedrock_agentcore_control.types.browser_id
    import capo_bedrock_agentcore_control.types.browser_status
    import capo_bedrock_agentcore_control.types.date_timestamp


class CreateBrowserResponse(TypedDict, closed=True):
    browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the created browser.</p>"""
    browser_arn: "capo_bedrock_agentcore_control.types.browser_arn.BrowserArn"
    """<p>The Amazon Resource Name (ARN) of the created browser.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser was created.</p>"""
    status: "capo_bedrock_agentcore_control.types.browser_status.BrowserStatus"
    """<p>The current status of the browser.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrowserResponse) -> dict:
    out: dict = {}
    out["browserId"] = value["browser_id"]
    out["browserArn"] = value["browser_arn"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.browser_status

    out["status"] = capo_bedrock_agentcore_control.types.browser_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateBrowserResponse:
    out: CreateBrowserResponse = {}  # type: ignore[typeddict-item]
    if data.get("browserId") is not None:
        out["browser_id"] = data["browserId"]
    else:
        raise DeserializationError("CreateBrowserResponse.browser_id required")
    if data.get("browserArn") is not None:
        out["browser_arn"] = data["browserArn"]
    else:
        raise DeserializationError("CreateBrowserResponse.browser_arn required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateBrowserResponse.created_at required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.browser_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.browser_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateBrowserResponse.status required")
    return out
