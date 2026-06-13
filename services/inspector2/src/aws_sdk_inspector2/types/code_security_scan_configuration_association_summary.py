"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSecurityScanConfigurationAssociationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_resource


class CodeSecurityScanConfigurationAssociationSummary(TypedDict):
    resource: NotRequired[
        "aws_sdk_inspector2.types.code_security_resource.CodeSecurityResource"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CodeSecurityScanConfigurationAssociationSummary) -> dict:
    out: dict = {}
    if "resource" in value:
        import aws_sdk_inspector2.types.code_security_resource

        out["resource"] = (
            aws_sdk_inspector2.types.code_security_resource.serialize_json(
                value["resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodeSecurityScanConfigurationAssociationSummary:
    out: CodeSecurityScanConfigurationAssociationSummary = {}  # type: ignore[typeddict-item]
    if "resource" in data:
        import aws_sdk_inspector2.types.code_security_resource

        out["resource"] = (
            aws_sdk_inspector2.types.code_security_resource.deserialize_json(
                data["resource"]
            )
        )
    return out
