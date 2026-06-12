"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfBackendAPIAuthType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.backend_api_auth_type

ListOfBackendAPIAuthType: TypeAlias = list[
    "aws_sdk_amplifybackend.types.backend_api_auth_type.BackendAPIAuthType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfBackendAPIAuthType) -> list:
    import aws_sdk_amplifybackend.types.backend_api_auth_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_amplifybackend.types.backend_api_auth_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfBackendAPIAuthType:
    import aws_sdk_amplifybackend.types.backend_api_auth_type

    out: ListOfBackendAPIAuthType = []
    for item in data:
        out.append(
            aws_sdk_amplifybackend.types.backend_api_auth_type.deserialize_json(item)
        )
    return out
