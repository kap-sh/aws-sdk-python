"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.action_list
    import aws_sdk_accessanalyzer.types.condition_key_map
    import aws_sdk_accessanalyzer.types.finding_id
    import aws_sdk_accessanalyzer.types.finding_source_list
    import aws_sdk_accessanalyzer.types.finding_status
    import aws_sdk_accessanalyzer.types.principal_map
    import aws_sdk_accessanalyzer.types.resource_control_policy_restriction
    import aws_sdk_accessanalyzer.types.resource_type
    import aws_sdk_accessanalyzer.types.timestamp


class FindingSummary(TypedDict, closed=True):
    id: "aws_sdk_accessanalyzer.types.finding_id.FindingId"
    """<p>The ID of the finding.</p>"""
    principal: NotRequired["aws_sdk_accessanalyzer.types.principal_map.PrincipalMap"]
    """<p>The external principal that has access to a resource within the zone of trust.</p>"""
    action: NotRequired["aws_sdk_accessanalyzer.types.action_list.ActionList"]
    """<p>The action in the analyzed policy statement that an external principal has permission to use.</p>"""
    resource: NotRequired["str"]
    """<p>The resource that the external principal has access to.</p>"""
    is_public: NotRequired["bool"]
    """<p>Indicates whether the finding reports a resource that has a policy that allows public access.</p>"""
    resource_type: "aws_sdk_accessanalyzer.types.resource_type.ResourceType"
    """<p>The type of the resource that the external principal has access to.</p>"""
    condition: "aws_sdk_accessanalyzer.types.condition_key_map.ConditionKeyMap"
    """<p>The condition in the analyzed policy statement that resulted in a finding.</p>"""
    created_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was created.</p>"""
    analyzed_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the resource-based policy that generated the finding was analyzed.</p>"""
    updated_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was most recently updated.</p>"""
    status: "aws_sdk_accessanalyzer.types.finding_status.FindingStatus"
    """<p>The status of the finding.</p>"""
    resource_owner_account: "str"
    """<p>The Amazon Web Services account ID that owns the resource.</p>"""
    error: NotRequired["str"]
    """<p>The error that resulted in an Error finding.</p>"""
    sources: NotRequired[
        "aws_sdk_accessanalyzer.types.finding_source_list.FindingSourceList"
    ]
    """<p>The sources of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.</p>"""
    resource_control_policy_restriction: NotRequired[
        "aws_sdk_accessanalyzer.types.resource_control_policy_restriction.ResourceControlPolicyRestriction"
    ]
    """<p>The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "principal" in value:
        import aws_sdk_accessanalyzer.types.principal_map

        out["principal"] = aws_sdk_accessanalyzer.types.principal_map.serialize_json(
            value["principal"]
        )
    if "action" in value:
        import aws_sdk_accessanalyzer.types.action_list

        out["action"] = aws_sdk_accessanalyzer.types.action_list.serialize_json(
            value["action"]
        )
    if "resource" in value:
        out["resource"] = value["resource"]
    if "is_public" in value:
        out["isPublic"] = value["is_public"]
    out["resourceType"] = value["resource_type"]
    import aws_sdk_accessanalyzer.types.condition_key_map

    out["condition"] = aws_sdk_accessanalyzer.types.condition_key_map.serialize_json(
        value["condition"]
    )
    import aws_sdk_accessanalyzer.types.timestamp

    out["createdAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_accessanalyzer.types.timestamp

    out["analyzedAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["analyzed_at"]
    )
    import aws_sdk_accessanalyzer.types.timestamp

    out["updatedAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["updated_at"]
    )
    out["status"] = value["status"]
    out["resourceOwnerAccount"] = value["resource_owner_account"]
    if "error" in value:
        out["error"] = value["error"]
    if "sources" in value:
        import aws_sdk_accessanalyzer.types.finding_source_list

        out["sources"] = (
            aws_sdk_accessanalyzer.types.finding_source_list.serialize_json(
                value["sources"]
            )
        )
    if "resource_control_policy_restriction" in value:
        out["resourceControlPolicyRestriction"] = value[
            "resource_control_policy_restriction"
        ]
    return out


def deserialize_json(data: dict) -> FindingSummary:
    out: FindingSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FindingSummary.id required")
    if "principal" in data:
        import aws_sdk_accessanalyzer.types.principal_map

        out["principal"] = aws_sdk_accessanalyzer.types.principal_map.deserialize_json(
            data["principal"]
        )
    if "action" in data:
        import aws_sdk_accessanalyzer.types.action_list

        out["action"] = aws_sdk_accessanalyzer.types.action_list.deserialize_json(
            data["action"]
        )
    if "resource" in data:
        out["resource"] = data["resource"]
    if "isPublic" in data:
        out["is_public"] = data["isPublic"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("FindingSummary.resource_type required")
    if "condition" in data:
        import aws_sdk_accessanalyzer.types.condition_key_map

        out["condition"] = (
            aws_sdk_accessanalyzer.types.condition_key_map.deserialize_json(
                data["condition"]
            )
        )
    else:
        raise DeserializationError("FindingSummary.condition required")
    if "createdAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["created_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("FindingSummary.created_at required")
    if "analyzedAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["analyzed_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["analyzedAt"]
        )
    else:
        raise DeserializationError("FindingSummary.analyzed_at required")
    if "updatedAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["updated_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("FindingSummary.updated_at required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("FindingSummary.status required")
    if "resourceOwnerAccount" in data:
        out["resource_owner_account"] = data["resourceOwnerAccount"]
    else:
        raise DeserializationError("FindingSummary.resource_owner_account required")
    if "error" in data:
        out["error"] = data["error"]
    if "sources" in data:
        import aws_sdk_accessanalyzer.types.finding_source_list

        out["sources"] = (
            aws_sdk_accessanalyzer.types.finding_source_list.deserialize_json(
                data["sources"]
            )
        )
    if "resourceControlPolicyRestriction" in data:
        out["resource_control_policy_restriction"] = data[
            "resourceControlPolicyRestriction"
        ]
    return out
