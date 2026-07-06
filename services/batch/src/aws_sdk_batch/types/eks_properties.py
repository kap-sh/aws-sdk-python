"""Generated from Smithy shape ``com.amazonaws.batch#EksProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.eks_pod_properties


class EksProperties(TypedDict, closed=True):
    pod_properties: NotRequired[
        "aws_sdk_batch.types.eks_pod_properties.EksPodProperties"
    ]
    """<p>The properties for the Kubernetes pod resources of a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksProperties) -> dict:
    out: dict = {}
    if "pod_properties" in value:
        import aws_sdk_batch.types.eks_pod_properties

        out["podProperties"] = aws_sdk_batch.types.eks_pod_properties.serialize_json(
            value["pod_properties"]
        )
    return out


def deserialize_json(data: dict) -> EksProperties:
    out: EksProperties = {}  # type: ignore[typeddict-item]
    if "podProperties" in data:
        import aws_sdk_batch.types.eks_pod_properties

        out["pod_properties"] = aws_sdk_batch.types.eks_pod_properties.deserialize_json(
            data["podProperties"]
        )
    return out
