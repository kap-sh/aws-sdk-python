"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AccessPreviewFinding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.access_preview_finding_id
    import aws_sdk_accessanalyzer.types.action_list
    import aws_sdk_accessanalyzer.types.condition_key_map
    import aws_sdk_accessanalyzer.types.finding_change_type
    import aws_sdk_accessanalyzer.types.finding_id
    import aws_sdk_accessanalyzer.types.finding_source_list
    import aws_sdk_accessanalyzer.types.finding_status
    import aws_sdk_accessanalyzer.types.principal_map
    import aws_sdk_accessanalyzer.types.resource_control_policy_restriction
    import aws_sdk_accessanalyzer.types.resource_type
    import aws_sdk_accessanalyzer.types.timestamp


class AccessPreviewFinding(TypedDict):
    id: "aws_sdk_accessanalyzer.types.access_preview_finding_id.AccessPreviewFindingId"
    """<p>The ID of the access preview finding. This ID uniquely identifies the element in the list of access preview findings and is not related to the finding ID in Access Analyzer.</p>"""
    existing_finding_id: NotRequired[
        "aws_sdk_accessanalyzer.types.finding_id.FindingId"
    ]
    """<p>The existing ID of the finding in IAM Access Analyzer, provided only for existing findings.</p>"""
    existing_finding_status: NotRequired[
        "aws_sdk_accessanalyzer.types.finding_status.FindingStatus"
    ]
    """<p>The existing status of the finding, provided only for existing findings.</p>"""
    principal: NotRequired["aws_sdk_accessanalyzer.types.principal_map.PrincipalMap"]
    """<p>The external principal that has access to a resource within the zone of trust.</p>"""
    action: NotRequired["aws_sdk_accessanalyzer.types.action_list.ActionList"]
    """<p>The action in the analyzed policy statement that an external principal has permission to perform.</p>"""
    condition: NotRequired[
        "aws_sdk_accessanalyzer.types.condition_key_map.ConditionKeyMap"
    ]
    """<p>The condition in the analyzed policy statement that resulted in a finding.</p>"""
    resource: NotRequired["str"]
    """<p>The resource that an external principal has access to. This is the resource associated with the access preview.</p>"""
    is_public: NotRequired["bool"]
    """<p>Indicates whether the policy that generated the finding allows public access to the resource.</p>"""
    resource_type: "aws_sdk_accessanalyzer.types.resource_type.ResourceType"
    """<p>The type of the resource that can be accessed in the finding.</p>"""
    created_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the access preview finding was created.</p>"""
    change_type: "aws_sdk_accessanalyzer.types.finding_change_type.FindingChangeType"
    """<p>Provides context on how the access preview finding compares to existing access identified in IAM Access Analyzer.</p> <ul> <li> <p> <code>New</code> - The finding is for newly-introduced access.</p> </li> <li> <p> <code>Unchanged</code> - The preview finding is an existing finding that would remain unchanged.</p> </li> <li> <p> <code>Changed</code> - The preview finding is an existing finding with a change in status.</p> </li> </ul> <p>For example, a <code>Changed</code> finding with preview status <code>Resolved</code> and existing status <code>Active</code> indicates the existing <code>Active</code> finding would become <code>Resolved</code> as a result of the proposed permissions change.</p>"""
    status: "aws_sdk_accessanalyzer.types.finding_status.FindingStatus"
    """<p>The preview status of the finding. This is what the status of the finding would be after permissions deployment. For example, a <code>Changed</code> finding with preview status <code>Resolved</code> and existing status <code>Active</code> indicates the existing <code>Active</code> finding would become <code>Resolved</code> as a result of the proposed permissions change.</p>"""
    resource_owner_account: "str"
    """<p>The Amazon Web Services account ID that owns the resource. For most Amazon Web Services resources, the owning account is the account in which the resource was created.</p>"""
    error: NotRequired["str"]
    """<p>An error.</p>"""
    sources: NotRequired[
        "aws_sdk_accessanalyzer.types.finding_source_list.FindingSourceList"
    ]
    """<p>The sources of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.</p>"""
    resource_control_policy_restriction: NotRequired[
        "aws_sdk_accessanalyzer.types.resource_control_policy_restriction.ResourceControlPolicyRestriction"
    ]
    """<p>The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessPreviewFinding) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "existing_finding_id" in value:
        out["existingFindingId"] = value["existing_finding_id"]
    if "existing_finding_status" in value:
        out["existingFindingStatus"] = value["existing_finding_status"]
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
    if "condition" in value:
        import aws_sdk_accessanalyzer.types.condition_key_map

        out["condition"] = (
            aws_sdk_accessanalyzer.types.condition_key_map.serialize_json(
                value["condition"]
            )
        )
    if "resource" in value:
        out["resource"] = value["resource"]
    if "is_public" in value:
        out["isPublic"] = value["is_public"]
    out["resourceType"] = value["resource_type"]
    import aws_sdk_accessanalyzer.types.timestamp

    out["createdAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["created_at"]
    )
    out["changeType"] = value["change_type"]
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


def deserialize_json(data: dict) -> AccessPreviewFinding:
    out: AccessPreviewFinding = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AccessPreviewFinding.id required")
    if "existingFindingId" in data:
        out["existing_finding_id"] = data["existingFindingId"]
    if "existingFindingStatus" in data:
        out["existing_finding_status"] = data["existingFindingStatus"]
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
    if "condition" in data:
        import aws_sdk_accessanalyzer.types.condition_key_map

        out["condition"] = (
            aws_sdk_accessanalyzer.types.condition_key_map.deserialize_json(
                data["condition"]
            )
        )
    if "resource" in data:
        out["resource"] = data["resource"]
    if "isPublic" in data:
        out["is_public"] = data["isPublic"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("AccessPreviewFinding.resource_type required")
    if "createdAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["created_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AccessPreviewFinding.created_at required")
    if "changeType" in data:
        out["change_type"] = data["changeType"]
    else:
        raise DeserializationError("AccessPreviewFinding.change_type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("AccessPreviewFinding.status required")
    if "resourceOwnerAccount" in data:
        out["resource_owner_account"] = data["resourceOwnerAccount"]
    else:
        raise DeserializationError(
            "AccessPreviewFinding.resource_owner_account required"
        )
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
