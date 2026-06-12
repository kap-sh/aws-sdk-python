"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeleteDomainPermissionsPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.resource_policy


class DeleteDomainPermissionsPolicyResult(TypedDict):
    policy: NotRequired["aws_sdk_codeartifact.types.resource_policy.ResourcePolicy"]
    """<p> Information about the deleted resource policy after processing the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainPermissionsPolicyResult) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_codeartifact.types.resource_policy

        out["policy"] = aws_sdk_codeartifact.types.resource_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> DeleteDomainPermissionsPolicyResult:
    out: DeleteDomainPermissionsPolicyResult = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_codeartifact.types.resource_policy

        out["policy"] = aws_sdk_codeartifact.types.resource_policy.deserialize_json(
            data["policy"]
        )
    return out
