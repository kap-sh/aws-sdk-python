"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#InferenceOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.inference_receiver_members


class InferenceOutputConfiguration(TypedDict, closed=True):
    accept: "str"
    """<p>The MIME type used to specify the output data.</p>"""
    members: (
        "aws_sdk_cleanroomsml.types.inference_receiver_members.InferenceReceiverMembers"
    )
    """<p>Defines the members that can receive inference output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceOutputConfiguration) -> dict:
    out: dict = {}
    out["accept"] = value.get("accept", "application/json")
    import aws_sdk_cleanroomsml.types.inference_receiver_members

    out["members"] = (
        aws_sdk_cleanroomsml.types.inference_receiver_members.serialize_json(
            value["members"]
        )
    )
    return out


def deserialize_json(data: dict) -> InferenceOutputConfiguration:
    out: InferenceOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "accept" in data:
        out["accept"] = data["accept"]
    else:
        out["accept"] = "application/json"
    if "members" in data:
        import aws_sdk_cleanroomsml.types.inference_receiver_members

        out["members"] = (
            aws_sdk_cleanroomsml.types.inference_receiver_members.deserialize_json(
                data["members"]
            )
        )
    else:
        raise DeserializationError("InferenceOutputConfiguration.members required")
    return out
