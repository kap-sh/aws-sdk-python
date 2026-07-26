"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreatorModeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.creator_mode_control


class CreatorModeConfiguration(TypedDict, closed=True):
    creator_mode_control: "capo_qbusiness.types.creator_mode_control.CreatorModeControl"
    """<p>Status information about whether <code>CREATOR_MODE</code> has been enabled or disabled. The default status is <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatorModeConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.creator_mode_control

    out["creatorModeControl"] = (
        capo_qbusiness.types.creator_mode_control.serialize_json(
            value["creator_mode_control"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatorModeConfiguration:
    out: CreatorModeConfiguration = {}  # type: ignore[typeddict-item]
    if "creatorModeControl" in data:
        import capo_qbusiness.types.creator_mode_control

        out["creator_mode_control"] = (
            capo_qbusiness.types.creator_mode_control.deserialize_json(
                data["creatorModeControl"]
            )
        )
    else:
        raise DeserializationError(
            "CreatorModeConfiguration.creator_mode_control required"
        )
    return out
