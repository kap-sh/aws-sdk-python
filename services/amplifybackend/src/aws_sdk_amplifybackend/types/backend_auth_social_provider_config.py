"""Generated from Smithy shape ``com.amazonaws.amplifybackend#BackendAuthSocialProviderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class BackendAuthSocialProviderConfig(TypedDict, closed=True):
    client_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>Describes the client_id, which can be obtained from the third-party social federation provider.</p>"""
    client_secret: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>Describes the client_secret, which can be obtained from third-party social federation providers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendAuthSocialProviderConfig) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["client_id"] = value["client_id"]
    if "client_secret" in value:
        out["client_secret"] = value["client_secret"]
    return out


def deserialize_json(data: dict) -> BackendAuthSocialProviderConfig:
    out: BackendAuthSocialProviderConfig = {}  # type: ignore[typeddict-item]
    if "client_id" in data:
        out["client_id"] = data["client_id"]
    if "client_secret" in data:
        out["client_secret"] = data["client_secret"]
    return out
