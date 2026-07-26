"""Generated from Smithy shape ``com.amazonaws.guardduty#AnomalyObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.observations
    import capo_guardduty.types.profile_subtype
    import capo_guardduty.types.profile_type


class AnomalyObject(TypedDict, closed=True):
    profile_type: NotRequired["capo_guardduty.types.profile_type.ProfileType"]
    """<p>The type of behavior of the profile.</p>"""
    profile_subtype: NotRequired["capo_guardduty.types.profile_subtype.ProfileSubtype"]
    """<p>The frequency of the anomaly.</p>"""
    observations: NotRequired["capo_guardduty.types.observations.Observations"]
    """<p>The recorded value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyObject) -> dict:
    out: dict = {}
    if "profile_type" in value:
        import capo_guardduty.types.profile_type

        out["profileType"] = capo_guardduty.types.profile_type.serialize_json(
            value["profile_type"]
        )
    if "profile_subtype" in value:
        import capo_guardduty.types.profile_subtype

        out["profileSubtype"] = capo_guardduty.types.profile_subtype.serialize_json(
            value["profile_subtype"]
        )
    if "observations" in value:
        import capo_guardduty.types.observations

        out["observations"] = capo_guardduty.types.observations.serialize_json(
            value["observations"]
        )
    return out


def deserialize_json(data: dict) -> AnomalyObject:
    out: AnomalyObject = {}  # type: ignore[typeddict-item]
    if "profileType" in data:
        import capo_guardduty.types.profile_type

        out["profile_type"] = capo_guardduty.types.profile_type.deserialize_json(
            data["profileType"]
        )
    if "profileSubtype" in data:
        import capo_guardduty.types.profile_subtype

        out["profile_subtype"] = capo_guardduty.types.profile_subtype.deserialize_json(
            data["profileSubtype"]
        )
    if "observations" in data:
        import capo_guardduty.types.observations

        out["observations"] = capo_guardduty.types.observations.deserialize_json(
            data["observations"]
        )
    return out
