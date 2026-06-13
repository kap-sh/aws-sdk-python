"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceSizeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_size_bins
    import aws_sdk_cleanroomsml.types.audience_size_type


class AudienceSizeConfig(TypedDict):
    audience_size_type: "aws_sdk_cleanroomsml.types.audience_size_type.AudienceSizeType"
    """<p>Whether the audience output sizes are defined as an absolute number or a percentage.</p>"""
    audience_size_bins: "aws_sdk_cleanroomsml.types.audience_size_bins.AudienceSizeBins"
    """<p>An array of the different audience output sizes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceSizeConfig) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.audience_size_type

    out["audienceSizeType"] = (
        aws_sdk_cleanroomsml.types.audience_size_type.serialize_json(
            value["audience_size_type"]
        )
    )
    import aws_sdk_cleanroomsml.types.audience_size_bins

    out["audienceSizeBins"] = (
        aws_sdk_cleanroomsml.types.audience_size_bins.serialize_json(
            value["audience_size_bins"]
        )
    )
    return out


def deserialize_json(data: dict) -> AudienceSizeConfig:
    out: AudienceSizeConfig = {}  # type: ignore[typeddict-item]
    if "audienceSizeType" in data:
        import aws_sdk_cleanroomsml.types.audience_size_type

        out["audience_size_type"] = (
            aws_sdk_cleanroomsml.types.audience_size_type.deserialize_json(
                data["audienceSizeType"]
            )
        )
    else:
        raise DeserializationError("AudienceSizeConfig.audience_size_type required")
    if "audienceSizeBins" in data:
        import aws_sdk_cleanroomsml.types.audience_size_bins

        out["audience_size_bins"] = (
            aws_sdk_cleanroomsml.types.audience_size_bins.deserialize_json(
                data["audienceSizeBins"]
            )
        )
    else:
        raise DeserializationError("AudienceSizeConfig.audience_size_bins required")
    return out
