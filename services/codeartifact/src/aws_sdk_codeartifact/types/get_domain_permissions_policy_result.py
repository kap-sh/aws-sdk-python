"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetDomainPermissionsPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.resource_policy


class GetDomainPermissionsPolicyResult(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_codeartifact.types.resource_policy.ResourcePolicy"]
    """<p> The returned resource policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainPermissionsPolicyResult) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_codeartifact.types.resource_policy

        out["policy"] = aws_sdk_codeartifact.types.resource_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> GetDomainPermissionsPolicyResult:
    out: GetDomainPermissionsPolicyResult = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_codeartifact.types.resource_policy

        out["policy"] = aws_sdk_codeartifact.types.resource_policy.deserialize_json(
            data["policy"]
        )
    return out
