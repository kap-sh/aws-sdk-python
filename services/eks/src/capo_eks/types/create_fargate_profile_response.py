"""Generated from Smithy shape ``com.amazonaws.eks#CreateFargateProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.fargate_profile


class CreateFargateProfileResponse(TypedDict, closed=True):
    fargate_profile: NotRequired["capo_eks.types.fargate_profile.FargateProfile"]
    """<p>The full description of your new Fargate profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFargateProfileResponse) -> dict:
    out: dict = {}
    if "fargate_profile" in value:
        import capo_eks.types.fargate_profile

        out["fargateProfile"] = capo_eks.types.fargate_profile.serialize_json(
            value["fargate_profile"]
        )
    return out


def deserialize_json(data: dict) -> CreateFargateProfileResponse:
    out: CreateFargateProfileResponse = {}  # type: ignore[typeddict-item]
    if "fargateProfile" in data:
        import capo_eks.types.fargate_profile

        out["fargate_profile"] = capo_eks.types.fargate_profile.deserialize_json(
            data["fargateProfile"]
        )
    return out
