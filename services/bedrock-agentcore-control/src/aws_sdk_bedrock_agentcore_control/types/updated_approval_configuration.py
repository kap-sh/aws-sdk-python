"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedApprovalConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.approval_configuration


class UpdatedApprovalConfiguration(TypedDict):
    optional_value: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.approval_configuration.ApprovalConfiguration"
    ]
    """<p>The updated approval configuration value. Set to <code>null</code> to unset the approval configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedApprovalConfiguration) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import aws_sdk_bedrock_agentcore_control.types.approval_configuration

        out["optionalValue"] = (
            aws_sdk_bedrock_agentcore_control.types.approval_configuration.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedApprovalConfiguration:
    out: UpdatedApprovalConfiguration = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import aws_sdk_bedrock_agentcore_control.types.approval_configuration

        out["optional_value"] = (
            aws_sdk_bedrock_agentcore_control.types.approval_configuration.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
