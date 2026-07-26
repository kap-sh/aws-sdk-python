"""Generated from Smithy shape ``com.amazonaws.securityhub#ConfigurationPolicyAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.target


class ConfigurationPolicyAssociation(TypedDict, closed=True):
    target: NotRequired["capo_securityhub.types.target.Target"]
    """<p> The target account, organizational unit, or the root. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationPolicyAssociation) -> dict:
    out: dict = {}
    if "target" in value:
        import capo_securityhub.types.target

        out["Target"] = capo_securityhub.types.target.serialize_json(value["target"])
    return out


def deserialize_json(data: dict) -> ConfigurationPolicyAssociation:
    out: ConfigurationPolicyAssociation = {}  # type: ignore[typeddict-item]
    if "Target" in data:
        import capo_securityhub.types.target

        out["target"] = capo_securityhub.types.target.deserialize_json(data["Target"])
    return out
