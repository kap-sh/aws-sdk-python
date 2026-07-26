"""Generated from Smithy shape ``com.amazonaws.xray#PutResourcePolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.resource_policy


class PutResourcePolicyResult(TypedDict, closed=True):
    resource_policy: NotRequired["capo_xray.types.resource_policy.ResourcePolicy"]
    """<p>The resource policy document, as provided in the <code>PutResourcePolicyRequest</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyResult) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        import capo_xray.types.resource_policy

        out["ResourcePolicy"] = capo_xray.types.resource_policy.serialize_json(
            value["resource_policy"]
        )
    return out


def deserialize_json(data: dict) -> PutResourcePolicyResult:
    out: PutResourcePolicyResult = {}  # type: ignore[typeddict-item]
    if "ResourcePolicy" in data:
        import capo_xray.types.resource_policy

        out["resource_policy"] = capo_xray.types.resource_policy.deserialize_json(
            data["ResourcePolicy"]
        )
    return out
