"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfCrossAccountAuthorization``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.cross_account_authorization

__listOfCrossAccountAuthorization: TypeAlias = list[
    "capo_route53_recovery_readiness.types.cross_account_authorization.CrossAccountAuthorization"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCrossAccountAuthorization) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOfCrossAccountAuthorization:
    return list(data)
