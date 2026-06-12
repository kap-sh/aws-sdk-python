"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#CreateScopeOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_networkflowmonitor.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.arn
    import aws_sdk_networkflowmonitor.types.scope_id
    import aws_sdk_networkflowmonitor.types.scope_status
    import aws_sdk_networkflowmonitor.types.tag_map

class CreateScopeOutput(TypedDict):
    scope_id: "aws_sdk_networkflowmonitor.types.scope_id.ScopeId"
    """<p>The identifier for the scope that includes the resources you want to get metrics for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>"""
    status: "aws_sdk_networkflowmonitor.types.scope_status.ScopeStatus"
    """<p>The status for a scope. The status can be one of the following: <code>SUCCEEDED</code>, <code>IN_PROGRESS</code>, <code>FAILED</code>, <code>DEACTIVATING</code>, or <code>DEACTIVATED</code>.</p> <p>A status of <code>DEACTIVATING</code> means that you've requested a scope to be deactivated and Network Flow Monitor is in the process of deactivating the scope. A status of <code>DEACTIVATED</code> means that the deactivating process is complete.</p>"""
    scope_arn: "aws_sdk_networkflowmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the scope.</p>"""
    tags: NotRequired["aws_sdk_networkflowmonitor.types.tag_map.TagMap"]
    """<p>The tags for a scope.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateScopeOutput) -> dict:
    out: dict = {}
    out["scopeId"] = value["scope_id"]
    import aws_sdk_networkflowmonitor.types.scope_status
    out["status"] = aws_sdk_networkflowmonitor.types.scope_status.serialize_json(value["status"])
    out["scopeArn"] = value["scope_arn"]
    if "tags" in value:
        import aws_sdk_networkflowmonitor.types.tag_map
        out["tags"] = aws_sdk_networkflowmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateScopeOutput:
    out: CreateScopeOutput = {}  # type: ignore[typeddict-item]
    if "scopeId" in data:
        out["scope_id"] = data["scopeId"]
    else:
        raise DeserializationError("CreateScopeOutput.scope_id required")
    if "status" in data:
        import aws_sdk_networkflowmonitor.types.scope_status
        out["status"] = aws_sdk_networkflowmonitor.types.scope_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("CreateScopeOutput.status required")
    if "scopeArn" in data:
        out["scope_arn"] = data["scopeArn"]
    else:
        raise DeserializationError("CreateScopeOutput.scope_arn required")
    if "tags" in data:
        import aws_sdk_networkflowmonitor.types.tag_map
        out["tags"] = aws_sdk_networkflowmonitor.types.tag_map.deserialize_json(data["tags"])
    return out