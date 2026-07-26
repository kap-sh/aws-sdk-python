"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_arn
    import capo_bedrock_agentcore_control.types.browser_id
    import capo_bedrock_agentcore_control.types.browser_status
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.sandbox_name


class BrowserSummary(TypedDict, closed=True):
    browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the browser.</p>"""
    browser_arn: "capo_bedrock_agentcore_control.types.browser_arn.BrowserArn"
    """<p>The Amazon Resource Name (ARN) of the browser.</p>"""
    name: NotRequired["capo_bedrock_agentcore_control.types.sandbox_name.SandboxName"]
    """<p>The name of the browser.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the browser.</p>"""
    status: "capo_bedrock_agentcore_control.types.browser_status.BrowserStatus"
    """<p>The current status of the browser.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser was created.</p>"""
    last_updated_at: NotRequired[
        "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the browser was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSummary) -> dict:
    out: dict = {}
    out["browserId"] = value["browser_id"]
    out["browserArn"] = value["browser_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.browser_status

    out["status"] = capo_bedrock_agentcore_control.types.browser_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    if "last_updated_at" in value:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["lastUpdatedAt"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrowserSummary:
    out: BrowserSummary = {}  # type: ignore[typeddict-item]
    if "browserId" in data:
        out["browser_id"] = data["browserId"]
    else:
        raise DeserializationError("BrowserSummary.browser_id required")
    if "browserArn" in data:
        out["browser_arn"] = data["browserArn"]
    else:
        raise DeserializationError("BrowserSummary.browser_arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import capo_bedrock_agentcore_control.types.browser_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.browser_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("BrowserSummary.status required")
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("BrowserSummary.created_at required")
    if "lastUpdatedAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
