"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.description


class UpdatedDescription(TypedDict, closed=True):
    optional_value: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>Represents an optional value that is used to update the human-readable description of the resource. If not specified, it will clear the current description of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedDescription) -> dict:
    out: dict = {}
    if "optional_value" in value:
        out["optionalValue"] = value["optional_value"]
    return out


def deserialize_json(data: dict) -> UpdatedDescription:
    out: UpdatedDescription = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        out["optional_value"] = data["optionalValue"]
    return out
