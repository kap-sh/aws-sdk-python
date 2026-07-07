"""Generated from Smithy shape ``com.amazonaws.datazone#RemovePolicyGrantInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.grant_identifier
    import aws_sdk_datazone.types.managed_policy_type
    import aws_sdk_datazone.types.policy_grant_principal
    import aws_sdk_datazone.types.target_entity_type


class RemovePolicyGrantInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to remove a policy grant.</p>"""
    entity_type: "aws_sdk_datazone.types.target_entity_type.TargetEntityType"
    """<p>The type of the entity from which you want to remove a policy grant.</p>"""
    entity_identifier: "str"
    """<p>The ID of the entity from which you want to remove a policy grant.</p>"""
    policy_type: "aws_sdk_datazone.types.managed_policy_type.ManagedPolicyType"
    """<p>The type of the policy that you want to remove.</p>"""
    principal: "aws_sdk_datazone.types.policy_grant_principal.PolicyGrantPrincipal"
    """<p>The principal from which you want to remove a policy grant.</p>"""
    grant_identifier: NotRequired[
        "aws_sdk_datazone.types.grant_identifier.GrantIdentifier"
    ]
    """<p>The ID of the policy grant that is to be removed from a specified entity.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemovePolicyGrantInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.managed_policy_type

    out["policyType"] = aws_sdk_datazone.types.managed_policy_type.serialize_json(
        value["policy_type"]
    )
    import aws_sdk_datazone.types.policy_grant_principal

    out["principal"] = aws_sdk_datazone.types.policy_grant_principal.serialize_json(
        value["principal"]
    )
    if "grant_identifier" in value:
        out["grantIdentifier"] = value["grant_identifier"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RemovePolicyGrantInput:
    out: RemovePolicyGrantInput = {}  # type: ignore[typeddict-item]
    if "policyType" in data:
        import aws_sdk_datazone.types.managed_policy_type

        out["policy_type"] = (
            aws_sdk_datazone.types.managed_policy_type.deserialize_json(
                data["policyType"]
            )
        )
    else:
        raise DeserializationError("RemovePolicyGrantInput.policy_type required")
    if "principal" in data:
        import aws_sdk_datazone.types.policy_grant_principal

        out["principal"] = (
            aws_sdk_datazone.types.policy_grant_principal.deserialize_json(
                data["principal"]
            )
        )
    else:
        raise DeserializationError("RemovePolicyGrantInput.principal required")
    if "grantIdentifier" in data:
        out["grant_identifier"] = data["grantIdentifier"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
