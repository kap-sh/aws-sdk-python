"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceSizeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_size_bins
    import capo_cleanroomsml.types.audience_size_type


class AudienceSizeConfig(TypedDict, closed=True):
    audience_size_type: "capo_cleanroomsml.types.audience_size_type.AudienceSizeType"
    """<p>Whether the audience output sizes are defined as an absolute number or a percentage.</p>"""
    audience_size_bins: "capo_cleanroomsml.types.audience_size_bins.AudienceSizeBins"
    """<p>An array of the different audience output sizes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceSizeConfig) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.audience_size_type

    out["audienceSizeType"] = capo_cleanroomsml.types.audience_size_type.serialize_json(
        value["audience_size_type"]
    )
    import capo_cleanroomsml.types.audience_size_bins

    out["audienceSizeBins"] = capo_cleanroomsml.types.audience_size_bins.serialize_json(
        value["audience_size_bins"]
    )
    return out


def deserialize_json(data: dict) -> AudienceSizeConfig:
    out: AudienceSizeConfig = {}  # type: ignore[typeddict-item]
    if "audienceSizeType" in data:
        import capo_cleanroomsml.types.audience_size_type

        out["audience_size_type"] = (
            capo_cleanroomsml.types.audience_size_type.deserialize_json(
                data["audienceSizeType"]
            )
        )
    else:
        raise DeserializationError("AudienceSizeConfig.audience_size_type required")
    if "audienceSizeBins" in data:
        import capo_cleanroomsml.types.audience_size_bins

        out["audience_size_bins"] = (
            capo_cleanroomsml.types.audience_size_bins.deserialize_json(
                data["audienceSizeBins"]
            )
        )
    else:
        raise DeserializationError("AudienceSizeConfig.audience_size_bins required")
    return out
