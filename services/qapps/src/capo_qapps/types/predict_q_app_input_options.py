"""Generated from Smithy shape ``com.amazonaws.qapps#PredictQAppInputOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qapps.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qapps.types.message_list


class _PredictQAppInputOptions_conversation(TypedDict, closed=True):
    conversation: "capo_qapps.types.message_list.MessageList"


class _PredictQAppInputOptions_problemStatement(TypedDict, closed=True):
    problemStatement: "str"


PredictQAppInputOptions: TypeAlias = (
    _PredictQAppInputOptions_conversation | _PredictQAppInputOptions_problemStatement
)


# --- restJson1 ser/de ---
def serialize_json(value: PredictQAppInputOptions) -> dict:
    if "conversation" in value:
        import capo_qapps.types.message_list

        return {
            "conversation": capo_qapps.types.message_list.serialize_json(
                value["conversation"]
            )
        }
    elif "problemStatement" in value:
        return {"problemStatement": value["problemStatement"]}
    else:
        raise SerializationError("PredictQAppInputOptions: no variant present")


def deserialize_json(data: dict) -> PredictQAppInputOptions:
    if "conversation" in data:
        import capo_qapps.types.message_list

        return {
            "conversation": capo_qapps.types.message_list.deserialize_json(
                data["conversation"]
            )
        }
    elif "problemStatement" in data:
        return {"problemStatement": data["problemStatement"]}
    else:
        raise DeserializationError("PredictQAppInputOptions: no recognized variant key")
