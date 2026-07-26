"""Generated from Smithy shape ``com.amazonaws.cognitosync#IdentityPoolUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_sync.types.identity_pool_usage

IdentityPoolUsageList: TypeAlias = list[
    "capo_cognito_sync.types.identity_pool_usage.IdentityPoolUsage"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityPoolUsageList) -> list:
    import capo_cognito_sync.types.identity_pool_usage

    out: list = []
    for item in value:
        out.append(capo_cognito_sync.types.identity_pool_usage.serialize_json(item))
    return out


def deserialize_json(data: list) -> IdentityPoolUsageList:
    import capo_cognito_sync.types.identity_pool_usage

    out: IdentityPoolUsageList = []
    for item in data:
        out.append(capo_cognito_sync.types.identity_pool_usage.deserialize_json(item))
    return out
