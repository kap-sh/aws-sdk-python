"""Generated from Smithy shape ``com.amazonaws.securityhub#GetConfigurationPolicyAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.target


class GetConfigurationPolicyAssociationRequest(TypedDict, closed=True):
    target: NotRequired["aws_sdk_securityhub.types.target.Target"]
    """<p> The target account ID, organizational unit ID, or the root ID to retrieve the association for. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationPolicyAssociationRequest) -> dict:
    out: dict = {}
    if "target" in value:
        import aws_sdk_securityhub.types.target

        out["Target"] = aws_sdk_securityhub.types.target.serialize_json(value["target"])
    return out


def deserialize_json(data: dict) -> GetConfigurationPolicyAssociationRequest:
    out: GetConfigurationPolicyAssociationRequest = {}  # type: ignore[typeddict-item]
    if "Target" in data:
        import aws_sdk_securityhub.types.target

        out["target"] = aws_sdk_securityhub.types.target.deserialize_json(
            data["Target"]
        )
    return out
