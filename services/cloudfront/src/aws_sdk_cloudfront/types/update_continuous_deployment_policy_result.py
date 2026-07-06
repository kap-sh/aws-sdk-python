"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateContinuousDeploymentPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.continuous_deployment_policy
    import aws_sdk_cloudfront.types.string


class UpdateContinuousDeploymentPolicyResult(TypedDict, closed=True):
    continuous_deployment_policy: NotRequired[
        "aws_sdk_cloudfront.types.continuous_deployment_policy.ContinuousDeploymentPolicy"
    ]
    """<p>A continuous deployment policy.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the continuous deployment policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateContinuousDeploymentPolicyResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "continuous_deployment_policy" in value:
        import aws_sdk_cloudfront.types.continuous_deployment_policy

        aws_sdk_cloudfront.types.continuous_deployment_policy.serialize_xml(
            value["continuous_deployment_policy"], el, "ContinuousDeploymentPolicy"
        )


def deserialize_xml(el: Element) -> UpdateContinuousDeploymentPolicyResult:
    out: UpdateContinuousDeploymentPolicyResult = {}  # type: ignore[typeddict-item]
    child_continuous_deployment_policy = el.find("ContinuousDeploymentPolicy")
    if child_continuous_deployment_policy is not None:
        import aws_sdk_cloudfront.types.continuous_deployment_policy

        out["continuous_deployment_policy"] = (
            aws_sdk_cloudfront.types.continuous_deployment_policy.deserialize_xml(
                child_continuous_deployment_policy
            )
        )
    return out
