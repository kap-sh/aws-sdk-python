"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetScopeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.arn
    import capo_networkflowmonitor.types.scope_id
    import capo_networkflowmonitor.types.scope_status
    import capo_networkflowmonitor.types.tag_map
    import capo_networkflowmonitor.types.target_resource_list


class GetScopeOutput(TypedDict, closed=True):
    scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId"
    """<p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account. A scope ID is returned from a <code>CreateScope</code> API call.</p>"""
    status: "capo_networkflowmonitor.types.scope_status.ScopeStatus"
    """<p>The status for a scope. The status can be one of the following: <code>SUCCEEDED</code>, <code>IN_PROGRESS</code>, <code>FAILED</code>, <code>DEACTIVATING</code>, or <code>DEACTIVATED</code>.</p> <p>A status of <code>DEACTIVATING</code> means that you've requested a scope to be deactivated and Network Flow Monitor is in the process of deactivating the scope. A status of <code>DEACTIVATED</code> means that the deactivating process is complete.</p>"""
    scope_arn: "capo_networkflowmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the scope.</p>"""
    targets: "capo_networkflowmonitor.types.target_resource_list.TargetResourceList"
    """<p>The targets to define the scope to be monitored. A target is an array of targetResources, which are currently Region-account pairs, defined by targetResource constructs.</p>"""
    tags: NotRequired["capo_networkflowmonitor.types.tag_map.TagMap"]
    """<p>The tags for a scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetScopeOutput) -> dict:
    out: dict = {}
    out["scopeId"] = value["scope_id"]
    import capo_networkflowmonitor.types.scope_status

    out["status"] = capo_networkflowmonitor.types.scope_status.serialize_json(
        value["status"]
    )
    out["scopeArn"] = value["scope_arn"]
    import capo_networkflowmonitor.types.target_resource_list

    out["targets"] = capo_networkflowmonitor.types.target_resource_list.serialize_json(
        value["targets"]
    )
    if "tags" in value:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetScopeOutput:
    out: GetScopeOutput = {}  # type: ignore[typeddict-item]
    if "scopeId" in data:
        out["scope_id"] = data["scopeId"]
    else:
        raise DeserializationError("GetScopeOutput.scope_id required")
    if "status" in data:
        import capo_networkflowmonitor.types.scope_status

        out["status"] = capo_networkflowmonitor.types.scope_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetScopeOutput.status required")
    if "scopeArn" in data:
        out["scope_arn"] = data["scopeArn"]
    else:
        raise DeserializationError("GetScopeOutput.scope_arn required")
    if "targets" in data:
        import capo_networkflowmonitor.types.target_resource_list

        out["targets"] = (
            capo_networkflowmonitor.types.target_resource_list.deserialize_json(
                data["targets"]
            )
        )
    else:
        raise DeserializationError("GetScopeOutput.targets required")
    if "tags" in data:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
