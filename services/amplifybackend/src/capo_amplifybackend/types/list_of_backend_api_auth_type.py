"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfBackendAPIAuthType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifybackend.types.backend_api_auth_type

ListOfBackendAPIAuthType: TypeAlias = list[
    "capo_amplifybackend.types.backend_api_auth_type.BackendAPIAuthType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfBackendAPIAuthType) -> list:
    import capo_amplifybackend.types.backend_api_auth_type

    out: list = []
    for item in value:
        out.append(capo_amplifybackend.types.backend_api_auth_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfBackendAPIAuthType:
    import capo_amplifybackend.types.backend_api_auth_type

    out: ListOfBackendAPIAuthType = []
    for item in data:
        out.append(
            capo_amplifybackend.types.backend_api_auth_type.deserialize_json(item)
        )
    return out
