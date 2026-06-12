"""Generated from Smithy shape ``com.amazonaws.codeartifact#PutDomainPermissionsPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.resource_policy


class PutDomainPermissionsPolicyResult(TypedDict):
    policy: NotRequired["aws_sdk_codeartifact.types.resource_policy.ResourcePolicy"]
    """<p> The resource policy that was set after processing the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDomainPermissionsPolicyResult) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_codeartifact.types.resource_policy

        out["policy"] = aws_sdk_codeartifact.types.resource_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> PutDomainPermissionsPolicyResult:
    out: PutDomainPermissionsPolicyResult = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_codeartifact.types.resource_policy

        out["policy"] = aws_sdk_codeartifact.types.resource_policy.deserialize_json(
            data["policy"]
        )
    return out
