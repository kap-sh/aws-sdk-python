"""Generated from Smithy shape ``com.amazonaws.codeartifact#PutRepositoryPermissionsPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.resource_policy


class PutRepositoryPermissionsPolicyResult(TypedDict, closed=True):
    policy: NotRequired["capo_codeartifact.types.resource_policy.ResourcePolicy"]
    """<p> The resource policy that was set after processing the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRepositoryPermissionsPolicyResult) -> dict:
    out: dict = {}
    if "policy" in value:
        import capo_codeartifact.types.resource_policy

        out["policy"] = capo_codeartifact.types.resource_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> PutRepositoryPermissionsPolicyResult:
    out: PutRepositoryPermissionsPolicyResult = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import capo_codeartifact.types.resource_policy

        out["policy"] = capo_codeartifact.types.resource_policy.deserialize_json(
            data["policy"]
        )
    return out
