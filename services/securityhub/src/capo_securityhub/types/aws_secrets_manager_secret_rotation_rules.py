"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSecretsManagerSecretRotationRules``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer


class AwsSecretsManagerSecretRotationRules(TypedDict, closed=True):
    automatically_after_days: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of days after the previous rotation to rotate the secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSecretsManagerSecretRotationRules) -> dict:
    out: dict = {}
    if "automatically_after_days" in value:
        out["AutomaticallyAfterDays"] = value["automatically_after_days"]
    return out


def deserialize_json(data: dict) -> AwsSecretsManagerSecretRotationRules:
    out: AwsSecretsManagerSecretRotationRules = {}  # type: ignore[typeddict-item]
    if "AutomaticallyAfterDays" in data:
        out["automatically_after_days"] = data["AutomaticallyAfterDays"]
    return out
