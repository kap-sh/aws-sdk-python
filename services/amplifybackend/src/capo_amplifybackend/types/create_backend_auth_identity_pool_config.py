"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendAuthIdentityPoolConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__boolean
    import capo_amplifybackend.types.__string


class CreateBackendAuthIdentityPoolConfig(TypedDict, closed=True):
    identity_pool_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>Name of the Amazon Cognito identity pool used for authorization.</p>"""
    unauthenticated_login: NotRequired["capo_amplifybackend.types.__boolean.__boolean"]
    """<p>Set to true or false based on whether you want to enable guest authorization to your Amplify app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendAuthIdentityPoolConfig) -> dict:
    out: dict = {}
    if "identity_pool_name" in value:
        out["identityPoolName"] = value["identity_pool_name"]
    if "unauthenticated_login" in value:
        out["unauthenticatedLogin"] = value["unauthenticated_login"]
    return out


def deserialize_json(data: dict) -> CreateBackendAuthIdentityPoolConfig:
    out: CreateBackendAuthIdentityPoolConfig = {}  # type: ignore[typeddict-item]
    if "identityPoolName" in data:
        out["identity_pool_name"] = data["identityPoolName"]
    if "unauthenticatedLogin" in data:
        out["unauthenticated_login"] = data["unauthenticatedLogin"]
    return out
