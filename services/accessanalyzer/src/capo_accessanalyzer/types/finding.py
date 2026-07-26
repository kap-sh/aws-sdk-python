"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Finding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.action_list
    import capo_accessanalyzer.types.condition_key_map
    import capo_accessanalyzer.types.finding_id
    import capo_accessanalyzer.types.finding_source_list
    import capo_accessanalyzer.types.finding_status
    import capo_accessanalyzer.types.principal_map
    import capo_accessanalyzer.types.resource_control_policy_restriction
    import capo_accessanalyzer.types.resource_type
    import capo_accessanalyzer.types.timestamp


class Finding(TypedDict, closed=True):
    id: "capo_accessanalyzer.types.finding_id.FindingId"
    """<p>The ID of the finding.</p>"""
    principal: NotRequired["capo_accessanalyzer.types.principal_map.PrincipalMap"]
    """<p>The external principal that has access to a resource within the zone of trust.</p>"""
    action: NotRequired["capo_accessanalyzer.types.action_list.ActionList"]
    """<p>The action in the analyzed policy statement that an external principal has permission to use.</p>"""
    resource: NotRequired["str"]
    """<p>The resource that an external principal has access to.</p>"""
    is_public: NotRequired["bool"]
    """<p>Indicates whether the policy that generated the finding allows public access to the resource.</p>"""
    resource_type: "capo_accessanalyzer.types.resource_type.ResourceType"
    """<p>The type of the resource identified in the finding.</p>"""
    condition: "capo_accessanalyzer.types.condition_key_map.ConditionKeyMap"
    """<p>The condition in the analyzed policy statement that resulted in a finding.</p>"""
    created_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was generated.</p>"""
    analyzed_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the resource was analyzed.</p>"""
    updated_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was updated.</p>"""
    status: "capo_accessanalyzer.types.finding_status.FindingStatus"
    """<p>The current status of the finding.</p>"""
    resource_owner_account: "str"
    """<p>The Amazon Web Services account ID that owns the resource.</p>"""
    error: NotRequired["str"]
    """<p>An error.</p>"""
    sources: NotRequired[
        "capo_accessanalyzer.types.finding_source_list.FindingSourceList"
    ]
    """<p>The sources of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.</p>"""
    resource_control_policy_restriction: NotRequired[
        "capo_accessanalyzer.types.resource_control_policy_restriction.ResourceControlPolicyRestriction"
    ]
    """<p>The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "principal" in value:
        import capo_accessanalyzer.types.principal_map

        out["principal"] = capo_accessanalyzer.types.principal_map.serialize_json(
            value["principal"]
        )
    if "action" in value:
        import capo_accessanalyzer.types.action_list

        out["action"] = capo_accessanalyzer.types.action_list.serialize_json(
            value["action"]
        )
    if "resource" in value:
        out["resource"] = value["resource"]
    if "is_public" in value:
        out["isPublic"] = value["is_public"]
    out["resourceType"] = value["resource_type"]
    import capo_accessanalyzer.types.condition_key_map

    out["condition"] = capo_accessanalyzer.types.condition_key_map.serialize_json(
        value["condition"]
    )
    import capo_accessanalyzer.types.timestamp

    out["createdAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_accessanalyzer.types.timestamp

    out["analyzedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["analyzed_at"]
    )
    import capo_accessanalyzer.types.timestamp

    out["updatedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["updated_at"]
    )
    out["status"] = value["status"]
    out["resourceOwnerAccount"] = value["resource_owner_account"]
    if "error" in value:
        out["error"] = value["error"]
    if "sources" in value:
        import capo_accessanalyzer.types.finding_source_list

        out["sources"] = capo_accessanalyzer.types.finding_source_list.serialize_json(
            value["sources"]
        )
    if "resource_control_policy_restriction" in value:
        out["resourceControlPolicyRestriction"] = value[
            "resource_control_policy_restriction"
        ]
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Finding.id required")
    if "principal" in data:
        import capo_accessanalyzer.types.principal_map

        out["principal"] = capo_accessanalyzer.types.principal_map.deserialize_json(
            data["principal"]
        )
    if "action" in data:
        import capo_accessanalyzer.types.action_list

        out["action"] = capo_accessanalyzer.types.action_list.deserialize_json(
            data["action"]
        )
    if "resource" in data:
        out["resource"] = data["resource"]
    if "isPublic" in data:
        out["is_public"] = data["isPublic"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("Finding.resource_type required")
    if "condition" in data:
        import capo_accessanalyzer.types.condition_key_map

        out["condition"] = capo_accessanalyzer.types.condition_key_map.deserialize_json(
            data["condition"]
        )
    else:
        raise DeserializationError("Finding.condition required")
    if "createdAt" in data:
        import capo_accessanalyzer.types.timestamp

        out["created_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("Finding.created_at required")
    if "analyzedAt" in data:
        import capo_accessanalyzer.types.timestamp

        out["analyzed_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["analyzedAt"]
        )
    else:
        raise DeserializationError("Finding.analyzed_at required")
    if "updatedAt" in data:
        import capo_accessanalyzer.types.timestamp

        out["updated_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("Finding.updated_at required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("Finding.status required")
    if "resourceOwnerAccount" in data:
        out["resource_owner_account"] = data["resourceOwnerAccount"]
    else:
        raise DeserializationError("Finding.resource_owner_account required")
    if "error" in data:
        out["error"] = data["error"]
    if "sources" in data:
        import capo_accessanalyzer.types.finding_source_list

        out["sources"] = capo_accessanalyzer.types.finding_source_list.deserialize_json(
            data["sources"]
        )
    if "resourceControlPolicyRestriction" in data:
        out["resource_control_policy_restriction"] = data[
            "resourceControlPolicyRestriction"
        ]
    return out
