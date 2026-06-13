"""Generated from Smithy shape ``com.amazonaws.qbusiness#ResponseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.instruction_collection


class ResponseConfiguration(TypedDict):
    instruction_collection: NotRequired[
        "aws_sdk_qbusiness.types.instruction_collection.InstructionCollection"
    ]
    """<p>A collection of instructions that guide how Amazon Q Business generates responses, including parameters for response length, target audience, perspective, output style, identity, tone, and custom instructions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseConfiguration) -> dict:
    out: dict = {}
    if "instruction_collection" in value:
        import aws_sdk_qbusiness.types.instruction_collection

        out["instructionCollection"] = (
            aws_sdk_qbusiness.types.instruction_collection.serialize_json(
                value["instruction_collection"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResponseConfiguration:
    out: ResponseConfiguration = {}  # type: ignore[typeddict-item]
    if "instructionCollection" in data:
        import aws_sdk_qbusiness.types.instruction_collection

        out["instruction_collection"] = (
            aws_sdk_qbusiness.types.instruction_collection.deserialize_json(
                data["instructionCollection"]
            )
        )
    return out
