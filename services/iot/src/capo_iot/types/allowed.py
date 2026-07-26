"""Generated from Smithy shape ``com.amazonaws.iot#Allowed``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policies


class Allowed(TypedDict, closed=True):
    policies: NotRequired["capo_iot.types.policies.Policies"]
    """<p>A list of policies that allowed the authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Allowed) -> dict:
    out: dict = {}
    if "policies" in value:
        import capo_iot.types.policies

        out["policies"] = capo_iot.types.policies.serialize_json(value["policies"])
    return out


def deserialize_json(data: dict) -> Allowed:
    out: Allowed = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import capo_iot.types.policies

        out["policies"] = capo_iot.types.policies.deserialize_json(data["policies"])
    return out
