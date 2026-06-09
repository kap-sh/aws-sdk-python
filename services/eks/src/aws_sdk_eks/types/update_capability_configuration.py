"""Generated from Smithy shape ``com.amazonaws.eks#UpdateCapabilityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.update_argo_cd_config


class UpdateCapabilityConfiguration(TypedDict):
    argo_cd: NotRequired["aws_sdk_eks.types.update_argo_cd_config.UpdateArgoCdConfig"]
    """<p>Configuration updates specific to Argo CD capabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCapabilityConfiguration) -> dict:
    out: dict = {}
    if "argo_cd" in value:
        import aws_sdk_eks.types.update_argo_cd_config

        out["argoCd"] = aws_sdk_eks.types.update_argo_cd_config.serialize_json(
            value["argo_cd"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCapabilityConfiguration:
    out: UpdateCapabilityConfiguration = {}  # type: ignore[typeddict-item]
    if "argoCd" in data:
        import aws_sdk_eks.types.update_argo_cd_config

        out["argo_cd"] = aws_sdk_eks.types.update_argo_cd_config.deserialize_json(
            data["argoCd"]
        )
    return out
