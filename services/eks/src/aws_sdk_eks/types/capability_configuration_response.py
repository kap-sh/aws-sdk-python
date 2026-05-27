"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.argo_cd_config_response


class CapabilityConfigurationResponse(TypedDict):
    argo_cd: NotRequired[
        "aws_sdk_eks.types.argo_cd_config_response.ArgoCdConfigResponse"
    ]
    """<p>Configuration settings for an Argo CD capability, including the server URL and other Argo CD-specific settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityConfigurationResponse) -> dict:
    out: dict = {}
    if "argo_cd" in value:
        import aws_sdk_eks.types.argo_cd_config_response

        out["argoCd"] = aws_sdk_eks.types.argo_cd_config_response.serialize_json(
            value["argo_cd"]
        )
    return out


def deserialize_json(data: dict) -> CapabilityConfigurationResponse:
    out: CapabilityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "argoCd" in data:
        import aws_sdk_eks.types.argo_cd_config_response

        out["argo_cd"] = aws_sdk_eks.types.argo_cd_config_response.deserialize_json(
            data["argoCd"]
        )
    return out
