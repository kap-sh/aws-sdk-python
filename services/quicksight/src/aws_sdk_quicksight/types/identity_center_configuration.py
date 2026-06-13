"""Generated from Smithy shape ``com.amazonaws.quicksight#IdentityCenterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean


class IdentityCenterConfiguration(TypedDict):
    enable_identity_propagation: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>A Boolean option that controls whether Trusted Identity Propagation should be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenterConfiguration) -> dict:
    out: dict = {}
    if "enable_identity_propagation" in value:
        out["EnableIdentityPropagation"] = value["enable_identity_propagation"]
    return out


def deserialize_json(data: dict) -> IdentityCenterConfiguration:
    out: IdentityCenterConfiguration = {}  # type: ignore[typeddict-item]
    if "EnableIdentityPropagation" in data:
        out["enable_identity_propagation"] = data["EnableIdentityPropagation"]
    return out
