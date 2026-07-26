"""Generated from Smithy shape ``com.amazonaws.datazone#ManagedPolicyType``."""

from typing import Literal, TypeAlias, cast

ManagedPolicyType: TypeAlias = Literal[
    "CREATE_DOMAIN_UNIT",
    "OVERRIDE_DOMAIN_UNIT_OWNERS",
    "ADD_TO_PROJECT_MEMBER_POOL",
    "OVERRIDE_PROJECT_OWNERS",
    "CREATE_GLOSSARY",
    "CREATE_FORM_TYPE",
    "CREATE_ASSET_TYPE",
    "CREATE_PROJECT",
    "CREATE_ENVIRONMENT_PROFILE",
    "DELEGATE_CREATE_ENVIRONMENT_PROFILE",
    "CREATE_ENVIRONMENT",
    "CREATE_ENVIRONMENT_FROM_BLUEPRINT",
    "CREATE_PROJECT_FROM_PROJECT_PROFILE",
    "USE_ASSET_TYPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedPolicyType) -> str:
    return value


def deserialize_json(data: str) -> ManagedPolicyType:
    return cast(ManagedPolicyType, data)
