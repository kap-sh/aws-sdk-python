"""Generated from Smithy shape ``com.amazonaws.efs#PutAccountPreferencesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.resource_id_preference


class PutAccountPreferencesResponse(TypedDict):
    resource_id_preference: NotRequired[
        "aws_sdk_efs.types.resource_id_preference.ResourceIdPreference"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountPreferencesResponse) -> dict:
    out: dict = {}
    if "resource_id_preference" in value:
        import aws_sdk_efs.types.resource_id_preference

        out["ResourceIdPreference"] = (
            aws_sdk_efs.types.resource_id_preference.serialize_json(
                value["resource_id_preference"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutAccountPreferencesResponse:
    out: PutAccountPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "ResourceIdPreference" in data:
        import aws_sdk_efs.types.resource_id_preference

        out["resource_id_preference"] = (
            aws_sdk_efs.types.resource_id_preference.deserialize_json(
                data["ResourceIdPreference"]
            )
        )
    return out
