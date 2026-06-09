"""Generated from Smithy shape ``com.amazonaws.eks#DeleteFargateProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.fargate_profile


class DeleteFargateProfileResponse(TypedDict):
    fargate_profile: NotRequired["aws_sdk_eks.types.fargate_profile.FargateProfile"]
    """<p>The deleted Fargate profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFargateProfileResponse) -> dict:
    out: dict = {}
    if "fargate_profile" in value:
        import aws_sdk_eks.types.fargate_profile

        out["fargateProfile"] = aws_sdk_eks.types.fargate_profile.serialize_json(
            value["fargate_profile"]
        )
    return out


def deserialize_json(data: dict) -> DeleteFargateProfileResponse:
    out: DeleteFargateProfileResponse = {}  # type: ignore[typeddict-item]
    if "fargateProfile" in data:
        import aws_sdk_eks.types.fargate_profile

        out["fargate_profile"] = aws_sdk_eks.types.fargate_profile.deserialize_json(
            data["fargateProfile"]
        )
    return out
