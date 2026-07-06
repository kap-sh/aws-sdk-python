"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetContinuousDeploymentPolicyConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.continuous_deployment_policy_config
    import aws_sdk_cloudfront.types.string


class GetContinuousDeploymentPolicyConfigResult(TypedDict, closed=True):
    continuous_deployment_policy_config: NotRequired[
        "aws_sdk_cloudfront.types.continuous_deployment_policy_config.ContinuousDeploymentPolicyConfig"
    ]
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the continuous deployment policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetContinuousDeploymentPolicyConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "continuous_deployment_policy_config" in value:
        import aws_sdk_cloudfront.types.continuous_deployment_policy_config

        aws_sdk_cloudfront.types.continuous_deployment_policy_config.serialize_xml(
            value["continuous_deployment_policy_config"],
            el,
            "ContinuousDeploymentPolicyConfig",
        )


def deserialize_xml(el: Element) -> GetContinuousDeploymentPolicyConfigResult:
    out: GetContinuousDeploymentPolicyConfigResult = {}  # type: ignore[typeddict-item]
    child_continuous_deployment_policy_config = el.find(
        "ContinuousDeploymentPolicyConfig"
    )
    if child_continuous_deployment_policy_config is not None:
        import aws_sdk_cloudfront.types.continuous_deployment_policy_config

        out["continuous_deployment_policy_config"] = (
            aws_sdk_cloudfront.types.continuous_deployment_policy_config.deserialize_xml(
                child_continuous_deployment_policy_config
            )
        )
    return out
