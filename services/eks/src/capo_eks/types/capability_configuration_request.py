"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.argo_cd_config_request


class CapabilityConfigurationRequest(TypedDict, closed=True):
    argo_cd: NotRequired["capo_eks.types.argo_cd_config_request.ArgoCdConfigRequest"]
    """<p>Configuration settings specific to Argo CD capabilities. This field is only used when creating or updating an Argo CD capability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityConfigurationRequest) -> dict:
    out: dict = {}
    if "argo_cd" in value:
        import capo_eks.types.argo_cd_config_request

        out["argoCd"] = capo_eks.types.argo_cd_config_request.serialize_json(
            value["argo_cd"]
        )
    return out


def deserialize_json(data: dict) -> CapabilityConfigurationRequest:
    out: CapabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "argoCd" in data:
        import capo_eks.types.argo_cd_config_request

        out["argo_cd"] = capo_eks.types.argo_cd_config_request.deserialize_json(
            data["argoCd"]
        )
    return out
