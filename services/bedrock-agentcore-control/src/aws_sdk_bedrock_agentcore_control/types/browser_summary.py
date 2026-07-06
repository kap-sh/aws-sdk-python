"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_arn
    import aws_sdk_bedrock_agentcore_control.types.browser_id
    import aws_sdk_bedrock_agentcore_control.types.browser_status
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.sandbox_name


class BrowserSummary(TypedDict, closed=True):
    browser_id: "aws_sdk_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the browser.</p>"""
    browser_arn: "aws_sdk_bedrock_agentcore_control.types.browser_arn.BrowserArn"
    """<p>The Amazon Resource Name (ARN) of the browser.</p>"""
    name: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.sandbox_name.SandboxName"
    ]
    """<p>The name of the browser.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the browser.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.browser_status.BrowserStatus"
    """<p>The current status of the browser.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser was created.</p>"""
    last_updated_at: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
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
    import aws_sdk_bedrock_agentcore_control.types.browser_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.browser_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    if "last_updated_at" in value:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
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
        import aws_sdk_bedrock_agentcore_control.types.browser_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.browser_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("BrowserSummary.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("BrowserSummary.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
