"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateDelegationRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.create_delegation_request

CreateDelegationRequests: TypeAlias = list[
    "capo_auditmanager.types.create_delegation_request.CreateDelegationRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateDelegationRequests) -> list:
    import capo_auditmanager.types.create_delegation_request

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.create_delegation_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateDelegationRequests:
    import capo_auditmanager.types.create_delegation_request

    out: CreateDelegationRequests = []
    for item in data:
        out.append(
            capo_auditmanager.types.create_delegation_request.deserialize_json(item)
        )
    return out
