"""Generated from Smithy shape ``com.amazonaws.efs#PutAccountPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.resource_id_preference


class PutAccountPreferencesResponse(TypedDict, closed=True):
    resource_id_preference: NotRequired[
        "capo_efs.types.resource_id_preference.ResourceIdPreference"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountPreferencesResponse) -> dict:
    out: dict = {}
    if "resource_id_preference" in value:
        import capo_efs.types.resource_id_preference

        out["ResourceIdPreference"] = (
            capo_efs.types.resource_id_preference.serialize_json(
                value["resource_id_preference"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutAccountPreferencesResponse:
    out: PutAccountPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "ResourceIdPreference" in data:
        import capo_efs.types.resource_id_preference

        out["resource_id_preference"] = (
            capo_efs.types.resource_id_preference.deserialize_json(
                data["ResourceIdPreference"]
            )
        )
    return out
