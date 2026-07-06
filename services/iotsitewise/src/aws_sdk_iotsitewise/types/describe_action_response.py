"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.action_payload
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.resolve_to
    import aws_sdk_iotsitewise.types.target_resource
    import aws_sdk_iotsitewise.types.timestamp


class DescribeActionResponse(TypedDict, closed=True):
    action_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the action.</p>"""
    target_resource: "aws_sdk_iotsitewise.types.target_resource.TargetResource"
    """<p>The resource the action will be taken on.</p>"""
    action_definition_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the action definition.</p>"""
    action_payload: "aws_sdk_iotsitewise.types.action_payload.ActionPayload"
    """<p>The JSON payload of the action.</p>"""
    execution_time: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the action was executed.</p>"""
    resolve_to: NotRequired["aws_sdk_iotsitewise.types.resolve_to.ResolveTo"]
    """<p>The detailed resource this action resolves to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeActionResponse) -> dict:
    out: dict = {}
    out["actionId"] = value["action_id"]
    import aws_sdk_iotsitewise.types.target_resource

    out["targetResource"] = aws_sdk_iotsitewise.types.target_resource.serialize_json(
        value["target_resource"]
    )
    out["actionDefinitionId"] = value["action_definition_id"]
    import aws_sdk_iotsitewise.types.action_payload

    out["actionPayload"] = aws_sdk_iotsitewise.types.action_payload.serialize_json(
        value["action_payload"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["executionTime"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["execution_time"]
    )
    if "resolve_to" in value:
        import aws_sdk_iotsitewise.types.resolve_to

        out["resolveTo"] = aws_sdk_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    return out


def deserialize_json(data: dict) -> DescribeActionResponse:
    out: DescribeActionResponse = {}  # type: ignore[typeddict-item]
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    else:
        raise DeserializationError("DescribeActionResponse.action_id required")
    if "targetResource" in data:
        import aws_sdk_iotsitewise.types.target_resource

        out["target_resource"] = (
            aws_sdk_iotsitewise.types.target_resource.deserialize_json(
                data["targetResource"]
            )
        )
    else:
        raise DeserializationError("DescribeActionResponse.target_resource required")
    if "actionDefinitionId" in data:
        out["action_definition_id"] = data["actionDefinitionId"]
    else:
        raise DeserializationError(
            "DescribeActionResponse.action_definition_id required"
        )
    if "actionPayload" in data:
        import aws_sdk_iotsitewise.types.action_payload

        out["action_payload"] = (
            aws_sdk_iotsitewise.types.action_payload.deserialize_json(
                data["actionPayload"]
            )
        )
    else:
        raise DeserializationError("DescribeActionResponse.action_payload required")
    if "executionTime" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["execution_time"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["executionTime"]
        )
    else:
        raise DeserializationError("DescribeActionResponse.execution_time required")
    if "resolveTo" in data:
        import aws_sdk_iotsitewise.types.resolve_to

        out["resolve_to"] = aws_sdk_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    return out
