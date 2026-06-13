"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#SecretsManagerCredentialsProvider``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SecretsManagerCredentialsProvider(TypedDict):
    secret_id: NotRequired["str"]
    """<p>The ID of the Secrets Manager secret that contains credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManagerCredentialsProvider) -> dict:
    out: dict = {}
    if "secret_id" in value:
        out["SecretId"] = value["secret_id"]
    return out


def deserialize_json(data: dict) -> SecretsManagerCredentialsProvider:
    out: SecretsManagerCredentialsProvider = {}  # type: ignore[typeddict-item]
    if "SecretId" in data:
        out["secret_id"] = data["SecretId"]
    return out
