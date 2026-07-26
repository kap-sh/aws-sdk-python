"""Generated from Smithy shape ``com.amazonaws.batch#EksPropertiesOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_pod_properties_override


class EksPropertiesOverride(TypedDict, closed=True):
    pod_properties: NotRequired[
        "capo_batch.types.eks_pod_properties_override.EksPodPropertiesOverride"
    ]
    """<p>The overrides for the Kubernetes pod resources of a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksPropertiesOverride) -> dict:
    out: dict = {}
    if "pod_properties" in value:
        import capo_batch.types.eks_pod_properties_override

        out["podProperties"] = (
            capo_batch.types.eks_pod_properties_override.serialize_json(
                value["pod_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksPropertiesOverride:
    out: EksPropertiesOverride = {}  # type: ignore[typeddict-item]
    if "podProperties" in data:
        import capo_batch.types.eks_pod_properties_override

        out["pod_properties"] = (
            capo_batch.types.eks_pod_properties_override.deserialize_json(
                data["podProperties"]
            )
        )
    return out
