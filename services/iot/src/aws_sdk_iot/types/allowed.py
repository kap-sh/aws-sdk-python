"""Generated from Smithy shape ``com.amazonaws.iot#Allowed``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.policies


class Allowed(TypedDict):
    policies: NotRequired["aws_sdk_iot.types.policies.Policies"]
    """<p>A list of policies that allowed the authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Allowed) -> dict:
    out: dict = {}
    if "policies" in value:
        import aws_sdk_iot.types.policies

        out["policies"] = aws_sdk_iot.types.policies.serialize_json(value["policies"])
    return out


def deserialize_json(data: dict) -> Allowed:
    out: Allowed = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import aws_sdk_iot.types.policies

        out["policies"] = aws_sdk_iot.types.policies.deserialize_json(data["policies"])
    return out
