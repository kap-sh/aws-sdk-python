"""Generated from Smithy shape ``com.amazonaws.ssoadmin#RedirectUris``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.uri

RedirectUris: TypeAlias = list["capo_sso_admin.types.uri.URI"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedirectUris) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RedirectUris:
    return list(data)
