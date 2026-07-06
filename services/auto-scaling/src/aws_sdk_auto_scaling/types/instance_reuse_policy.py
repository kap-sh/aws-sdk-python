"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceReusePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.reuse_on_scale_in


class InstanceReusePolicy(TypedDict, closed=True):
    reuse_on_scale_in: NotRequired[
        "aws_sdk_auto_scaling.types.reuse_on_scale_in.ReuseOnScaleIn"
    ]
    """<p>Specifies whether instances in the Auto Scaling group can be returned to the warm pool on scale in. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceReusePolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reuse_on_scale_in" in value:
        pairs.append(
            (
                f"{prefix}.ReuseOnScaleIn",
                "true" if value["reuse_on_scale_in"] else "false",
            )
        )


def deserialize_query(el: Element) -> InstanceReusePolicy:
    out: InstanceReusePolicy = {}  # type: ignore[typeddict-item]
    child_reuse_on_scale_in = el.find("ReuseOnScaleIn")
    if child_reuse_on_scale_in is not None:
        out["reuse_on_scale_in"] = (
            child_reuse_on_scale_in.text or ""
        ).lower() == "true"
    return out
