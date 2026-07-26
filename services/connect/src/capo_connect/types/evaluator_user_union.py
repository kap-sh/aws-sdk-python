"""Generated from Smithy shape ``com.amazonaws.connect#EvaluatorUserUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.arn


class _EvaluatorUserUnion_ConnectUserArn(TypedDict, closed=True):
    ConnectUserArn: "capo_connect.types.arn.ARN"


EvaluatorUserUnion: TypeAlias = _EvaluatorUserUnion_ConnectUserArn


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorUserUnion) -> dict:
    if "ConnectUserArn" in value:
        return {"ConnectUserArn": value["ConnectUserArn"]}
    else:
        raise SerializationError("EvaluatorUserUnion: no variant present")


def deserialize_json(data: dict) -> EvaluatorUserUnion:
    if "ConnectUserArn" in data:
        return {"ConnectUserArn": data["ConnectUserArn"]}
    else:
        raise DeserializationError("EvaluatorUserUnion: no recognized variant key")
