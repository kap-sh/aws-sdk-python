"""Generated from Smithy shape ``com.amazonaws.qbusiness#ResponseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.instruction_collection


class ResponseConfiguration(TypedDict, closed=True):
    instruction_collection: NotRequired[
        "capo_qbusiness.types.instruction_collection.InstructionCollection"
    ]
    """<p>A collection of instructions that guide how Amazon Q Business generates responses, including parameters for response length, target audience, perspective, output style, identity, tone, and custom instructions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseConfiguration) -> dict:
    out: dict = {}
    if "instruction_collection" in value:
        import capo_qbusiness.types.instruction_collection

        out["instructionCollection"] = (
            capo_qbusiness.types.instruction_collection.serialize_json(
                value["instruction_collection"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResponseConfiguration:
    out: ResponseConfiguration = {}  # type: ignore[typeddict-item]
    if "instructionCollection" in data:
        import capo_qbusiness.types.instruction_collection

        out["instruction_collection"] = (
            capo_qbusiness.types.instruction_collection.deserialize_json(
                data["instructionCollection"]
            )
        )
    return out
