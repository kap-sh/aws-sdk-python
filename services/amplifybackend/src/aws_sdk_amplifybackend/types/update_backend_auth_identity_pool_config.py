"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthIdentityPoolConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__boolean


class UpdateBackendAuthIdentityPoolConfig(TypedDict):
    unauthenticated_login: NotRequired[
        "aws_sdk_amplifybackend.types.__boolean.__boolean"
    ]
    """<p>A boolean value that can be set to allow or disallow guest-level authorization into your Amplify app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthIdentityPoolConfig) -> dict:
    out: dict = {}
    if "unauthenticated_login" in value:
        out["unauthenticatedLogin"] = value["unauthenticated_login"]
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthIdentityPoolConfig:
    out: UpdateBackendAuthIdentityPoolConfig = {}  # type: ignore[typeddict-item]
    if "unauthenticatedLogin" in data:
        out["unauthenticated_login"] = data["unauthenticatedLogin"]
    return out
