"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__string
    import capo_medialive.types.sdi_source_mode
    import capo_medialive.types.sdi_source_state
    import capo_medialive.types.sdi_source_type


class SdiSource(TypedDict, closed=True):
    arn: NotRequired["capo_medialive.types.__string.__string"]
    """The ARN of this SdiSource. It is automatically assigned when the SdiSource is created."""
    id: NotRequired["capo_medialive.types.__string.__string"]
    """The ID of the SdiSource. Unique in the AWS account.The ID is the resource-id portion of the ARN."""
    inputs: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """The list of inputs that are currently using this SDI source. This list will be empty if the SdiSource has just been deleted."""
    mode: NotRequired["capo_medialive.types.sdi_source_mode.SdiSourceMode"]
    """Applies only if the type is QUAD. The mode for handling the quad-link signal QUADRANT or INTERLEAVE."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """The name of the SdiSource."""
    state: NotRequired["capo_medialive.types.sdi_source_state.SdiSourceState"]
    """Specifies whether the SDI source is attached to an SDI input (IN_USE) or not (IDLE)."""
    type: NotRequired["capo_medialive.types.sdi_source_type.SdiSourceType"]


# --- restJson1 ser/de ---
def serialize_json(value: SdiSource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "inputs" in value:
        import capo_medialive.types.__list_of__string

        out["inputs"] = capo_medialive.types.__list_of__string.serialize_json(
            value["inputs"]
        )
    if "mode" in value:
        import capo_medialive.types.sdi_source_mode

        out["mode"] = capo_medialive.types.sdi_source_mode.serialize_json(value["mode"])
    if "name" in value:
        out["name"] = value["name"]
    if "state" in value:
        import capo_medialive.types.sdi_source_state

        out["state"] = capo_medialive.types.sdi_source_state.serialize_json(
            value["state"]
        )
    if "type" in value:
        import capo_medialive.types.sdi_source_type

        out["type"] = capo_medialive.types.sdi_source_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SdiSource:
    out: SdiSource = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "inputs" in data:
        import capo_medialive.types.__list_of__string

        out["inputs"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["inputs"]
        )
    if "mode" in data:
        import capo_medialive.types.sdi_source_mode

        out["mode"] = capo_medialive.types.sdi_source_mode.deserialize_json(
            data["mode"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "state" in data:
        import capo_medialive.types.sdi_source_state

        out["state"] = capo_medialive.types.sdi_source_state.deserialize_json(
            data["state"]
        )
    if "type" in data:
        import capo_medialive.types.sdi_source_type

        out["type"] = capo_medialive.types.sdi_source_type.deserialize_json(
            data["type"]
        )
    return out
