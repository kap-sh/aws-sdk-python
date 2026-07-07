"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecuteActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.action_payload
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.resolve_to
    import aws_sdk_iotsitewise.types.target_resource


class ExecuteActionRequest(TypedDict, closed=True):
    target_resource: "aws_sdk_iotsitewise.types.target_resource.TargetResource"
    """<p>The resource the action will be taken on.</p>"""
    action_definition_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the action definition.</p>"""
    action_payload: "aws_sdk_iotsitewise.types.action_payload.ActionPayload"
    """<p>The JSON payload of the action.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    resolve_to: NotRequired["aws_sdk_iotsitewise.types.resolve_to.ResolveTo"]
    """<p>The detailed resource this action resolves to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteActionRequest) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.target_resource

    out["targetResource"] = aws_sdk_iotsitewise.types.target_resource.serialize_json(
        value["target_resource"]
    )
    out["actionDefinitionId"] = value["action_definition_id"]
    import aws_sdk_iotsitewise.types.action_payload

    out["actionPayload"] = aws_sdk_iotsitewise.types.action_payload.serialize_json(
        value["action_payload"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "resolve_to" in value:
        import aws_sdk_iotsitewise.types.resolve_to

        out["resolveTo"] = aws_sdk_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    return out


def deserialize_json(data: dict) -> ExecuteActionRequest:
    out: ExecuteActionRequest = {}  # type: ignore[typeddict-item]
    if "targetResource" in data:
        import aws_sdk_iotsitewise.types.target_resource

        out["target_resource"] = (
            aws_sdk_iotsitewise.types.target_resource.deserialize_json(
                data["targetResource"]
            )
        )
    else:
        raise DeserializationError("ExecuteActionRequest.target_resource required")
    if "actionDefinitionId" in data:
        out["action_definition_id"] = data["actionDefinitionId"]
    else:
        raise DeserializationError("ExecuteActionRequest.action_definition_id required")
    if "actionPayload" in data:
        import aws_sdk_iotsitewise.types.action_payload

        out["action_payload"] = (
            aws_sdk_iotsitewise.types.action_payload.deserialize_json(
                data["actionPayload"]
            )
        )
    else:
        raise DeserializationError("ExecuteActionRequest.action_payload required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "resolveTo" in data:
        import aws_sdk_iotsitewise.types.resolve_to

        out["resolve_to"] = aws_sdk_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    return out
