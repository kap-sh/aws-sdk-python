"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.lifecycle_policy_details
    import capo_imagebuilder.types.lifecycle_policy_resource_selection
    import capo_imagebuilder.types.lifecycle_policy_resource_type
    import capo_imagebuilder.types.lifecycle_policy_status
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.tag_map


class CreateLifecyclePolicyRequest(TypedDict, closed=True):
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the lifecycle policy to create.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Optional description for the lifecycle policy.</p>"""
    status: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_status.LifecyclePolicyStatus"
    ]
    """<p>Indicates whether the lifecycle policy resource is enabled.</p>"""
    execution_role: "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions.</p>"""
    resource_type: "capo_imagebuilder.types.lifecycle_policy_resource_type.LifecyclePolicyResourceType"
    """<p>The type of Image Builder resource that the lifecycle policy applies to.</p>"""
    policy_details: (
        "capo_imagebuilder.types.lifecycle_policy_details.LifecyclePolicyDetails"
    )
    """<p>Configuration details for the lifecycle policy rules.</p>"""
    resource_selection: "capo_imagebuilder.types.lifecycle_policy_resource_selection.LifecyclePolicyResourceSelection"
    """<p>Selection criteria for the resources that the lifecycle policy applies to. </p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags to apply to the lifecycle policy resource.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLifecyclePolicyRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_imagebuilder.types.lifecycle_policy_status

        out["status"] = capo_imagebuilder.types.lifecycle_policy_status.serialize_json(
            value["status"]
        )
    out["executionRole"] = value["execution_role"]
    import capo_imagebuilder.types.lifecycle_policy_resource_type

    out["resourceType"] = (
        capo_imagebuilder.types.lifecycle_policy_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import capo_imagebuilder.types.lifecycle_policy_details

    out["policyDetails"] = (
        capo_imagebuilder.types.lifecycle_policy_details.serialize_json(
            value["policy_details"]
        )
    )
    import capo_imagebuilder.types.lifecycle_policy_resource_selection

    out["resourceSelection"] = (
        capo_imagebuilder.types.lifecycle_policy_resource_selection.serialize_json(
            value["resource_selection"]
        )
    )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateLifecyclePolicyRequest:
    out: CreateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateLifecyclePolicyRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import capo_imagebuilder.types.lifecycle_policy_status

        out["status"] = (
            capo_imagebuilder.types.lifecycle_policy_status.deserialize_json(
                data["status"]
            )
        )
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError(
            "CreateLifecyclePolicyRequest.execution_role required"
        )
    if "resourceType" in data:
        import capo_imagebuilder.types.lifecycle_policy_resource_type

        out["resource_type"] = (
            capo_imagebuilder.types.lifecycle_policy_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLifecyclePolicyRequest.resource_type required"
        )
    if "policyDetails" in data:
        import capo_imagebuilder.types.lifecycle_policy_details

        out["policy_details"] = (
            capo_imagebuilder.types.lifecycle_policy_details.deserialize_json(
                data["policyDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLifecyclePolicyRequest.policy_details required"
        )
    if "resourceSelection" in data:
        import capo_imagebuilder.types.lifecycle_policy_resource_selection

        out["resource_selection"] = (
            capo_imagebuilder.types.lifecycle_policy_resource_selection.deserialize_json(
                data["resourceSelection"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLifecyclePolicyRequest.resource_selection required"
        )
    if "tags" in data:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateLifecyclePolicyRequest.client_token required")
    return out
