"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeleteDomainPermissionsPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.resource_policy


class DeleteDomainPermissionsPolicyResult(TypedDict, closed=True):
    policy: NotRequired["capo_codeartifact.types.resource_policy.ResourcePolicy"]
    """<p> Information about the deleted resource policy after processing the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainPermissionsPolicyResult) -> dict:
    out: dict = {}
    if "policy" in value:
        import capo_codeartifact.types.resource_policy

        out["policy"] = capo_codeartifact.types.resource_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> DeleteDomainPermissionsPolicyResult:
    out: DeleteDomainPermissionsPolicyResult = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import capo_codeartifact.types.resource_policy

        out["policy"] = capo_codeartifact.types.resource_policy.deserialize_json(
            data["policy"]
        )
    return out
