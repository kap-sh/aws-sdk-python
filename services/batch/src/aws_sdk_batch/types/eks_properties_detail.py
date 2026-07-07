"""Generated from Smithy shape ``com.amazonaws.batch#EksPropertiesDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.eks_pod_properties_detail


class EksPropertiesDetail(TypedDict, closed=True):
    pod_properties: NotRequired[
        "aws_sdk_batch.types.eks_pod_properties_detail.EksPodPropertiesDetail"
    ]
    """<p>The properties for the Kubernetes pod resources of a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksPropertiesDetail) -> dict:
    out: dict = {}
    if "pod_properties" in value:
        import aws_sdk_batch.types.eks_pod_properties_detail

        out["podProperties"] = (
            aws_sdk_batch.types.eks_pod_properties_detail.serialize_json(
                value["pod_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksPropertiesDetail:
    out: EksPropertiesDetail = {}  # type: ignore[typeddict-item]
    if "podProperties" in data:
        import aws_sdk_batch.types.eks_pod_properties_detail

        out["pod_properties"] = (
            aws_sdk_batch.types.eks_pod_properties_detail.deserialize_json(
                data["podProperties"]
            )
        )
    return out
