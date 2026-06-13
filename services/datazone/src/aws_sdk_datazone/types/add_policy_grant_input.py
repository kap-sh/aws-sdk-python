"""Generated from Smithy shape ``com.amazonaws.datazone#AddPolicyGrantInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.managed_policy_type
    import aws_sdk_datazone.types.policy_grant_detail
    import aws_sdk_datazone.types.policy_grant_principal
    import aws_sdk_datazone.types.target_entity_type


class AddPolicyGrantInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to add a policy grant.</p>"""
    entity_type: "aws_sdk_datazone.types.target_entity_type.TargetEntityType"
    """<p>The type of entity (resource) to which the grant is added.</p>"""
    entity_identifier: "str"
    """<p>The ID of the entity (resource) to which you want to add a policy grant.</p>"""
    policy_type: "aws_sdk_datazone.types.managed_policy_type.ManagedPolicyType"
    """<p>The type of policy that you want to grant.</p>"""
    principal: "aws_sdk_datazone.types.policy_grant_principal.PolicyGrantPrincipal"
    """<p>The principal to whom the permissions are granted.</p>"""
    detail: "aws_sdk_datazone.types.policy_grant_detail.PolicyGrantDetail"
    """<p>The details of the policy grant.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddPolicyGrantInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.managed_policy_type

    out["policyType"] = aws_sdk_datazone.types.managed_policy_type.serialize_json(
        value["policy_type"]
    )
    import aws_sdk_datazone.types.policy_grant_principal

    out["principal"] = aws_sdk_datazone.types.policy_grant_principal.serialize_json(
        value["principal"]
    )
    import aws_sdk_datazone.types.policy_grant_detail

    out["detail"] = aws_sdk_datazone.types.policy_grant_detail.serialize_json(
        value["detail"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AddPolicyGrantInput:
    out: AddPolicyGrantInput = {}  # type: ignore[typeddict-item]
    if "policyType" in data:
        import aws_sdk_datazone.types.managed_policy_type

        out["policy_type"] = (
            aws_sdk_datazone.types.managed_policy_type.deserialize_json(
                data["policyType"]
            )
        )
    else:
        raise DeserializationError("AddPolicyGrantInput.policy_type required")
    if "principal" in data:
        import aws_sdk_datazone.types.policy_grant_principal

        out["principal"] = (
            aws_sdk_datazone.types.policy_grant_principal.deserialize_json(
                data["principal"]
            )
        )
    else:
        raise DeserializationError("AddPolicyGrantInput.principal required")
    if "detail" in data:
        import aws_sdk_datazone.types.policy_grant_detail

        out["detail"] = aws_sdk_datazone.types.policy_grant_detail.deserialize_json(
            data["detail"]
        )
    else:
        raise DeserializationError("AddPolicyGrantInput.detail required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
