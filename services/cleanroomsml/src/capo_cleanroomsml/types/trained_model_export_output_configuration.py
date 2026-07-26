"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_export_receiver_members


class TrainedModelExportOutputConfiguration(TypedDict, closed=True):
    members: "capo_cleanroomsml.types.trained_model_export_receiver_members.TrainedModelExportReceiverMembers"
    """<p>The members that will received the exported trained model output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportOutputConfiguration) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.trained_model_export_receiver_members

    out["members"] = (
        capo_cleanroomsml.types.trained_model_export_receiver_members.serialize_json(
            value["members"]
        )
    )
    return out


def deserialize_json(data: dict) -> TrainedModelExportOutputConfiguration:
    out: TrainedModelExportOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "members" in data:
        import capo_cleanroomsml.types.trained_model_export_receiver_members

        out["members"] = (
            capo_cleanroomsml.types.trained_model_export_receiver_members.deserialize_json(
                data["members"]
            )
        )
    else:
        raise DeserializationError(
            "TrainedModelExportOutputConfiguration.members required"
        )
    return out
