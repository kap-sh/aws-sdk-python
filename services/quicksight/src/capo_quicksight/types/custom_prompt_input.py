"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomPromptInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_quicksight.types.custom_prompt_input_parameters
    import capo_quicksight.types.custom_prompt_profile


class _CustomPromptInput_ExistingPrompt(TypedDict, closed=True):
    ExistingPrompt: "capo_quicksight.types.custom_prompt_profile.CustomPromptProfile"


class _CustomPromptInput_NewPrompt(TypedDict, closed=True):
    NewPrompt: "capo_quicksight.types.custom_prompt_input_parameters.CustomPromptInputParameters"


CustomPromptInput: TypeAlias = (
    _CustomPromptInput_ExistingPrompt | _CustomPromptInput_NewPrompt
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomPromptInput) -> dict:
    if "ExistingPrompt" in value:
        import capo_quicksight.types.custom_prompt_profile

        return {
            "ExistingPrompt": capo_quicksight.types.custom_prompt_profile.serialize_json(
                value["ExistingPrompt"]
            )
        }
    elif "NewPrompt" in value:
        import capo_quicksight.types.custom_prompt_input_parameters

        return {
            "NewPrompt": capo_quicksight.types.custom_prompt_input_parameters.serialize_json(
                value["NewPrompt"]
            )
        }
    else:
        raise SerializationError("CustomPromptInput: no variant present")


def deserialize_json(data: dict) -> CustomPromptInput:
    if "ExistingPrompt" in data:
        import capo_quicksight.types.custom_prompt_profile

        return {
            "ExistingPrompt": capo_quicksight.types.custom_prompt_profile.deserialize_json(
                data["ExistingPrompt"]
            )
        }
    elif "NewPrompt" in data:
        import capo_quicksight.types.custom_prompt_input_parameters

        return {
            "NewPrompt": capo_quicksight.types.custom_prompt_input_parameters.deserialize_json(
                data["NewPrompt"]
            )
        }
    else:
        raise DeserializationError("CustomPromptInput: no recognized variant key")
