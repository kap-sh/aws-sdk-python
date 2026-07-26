"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContinuousDeploymentPolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.continuous_deployment_policy


class ContinuousDeploymentPolicySummary(TypedDict, closed=True):
    continuous_deployment_policy: (
        "capo_cloudfront.types.continuous_deployment_policy.ContinuousDeploymentPolicy"
    )
    """<p>The continuous deployment policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ContinuousDeploymentPolicySummary, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.continuous_deployment_policy

    capo_cloudfront.types.continuous_deployment_policy.serialize_xml(
        value["continuous_deployment_policy"], el, "ContinuousDeploymentPolicy"
    )


def deserialize_xml(el: Element) -> ContinuousDeploymentPolicySummary:
    out: ContinuousDeploymentPolicySummary = {}  # type: ignore[typeddict-item]
    child_continuous_deployment_policy = el.find("ContinuousDeploymentPolicy")
    if child_continuous_deployment_policy is not None:
        import capo_cloudfront.types.continuous_deployment_policy

        out["continuous_deployment_policy"] = (
            capo_cloudfront.types.continuous_deployment_policy.deserialize_xml(
                child_continuous_deployment_policy
            )
        )
    else:
        raise DeserializationError(
            "ContinuousDeploymentPolicySummary.continuous_deployment_policy required"
        )
    return out
