"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateContinuousDeploymentPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.continuous_deployment_policy_config
    import aws_sdk_cloudfront.types.string


class UpdateContinuousDeploymentPolicyRequest(TypedDict):
    continuous_deployment_policy_config: "aws_sdk_cloudfront.types.continuous_deployment_policy_config.ContinuousDeploymentPolicyConfig"
    """<p>The continuous deployment policy configuration.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the continuous deployment policy that you are updating.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version (<code>ETag</code> value) of the continuous deployment policy that you are updating.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateContinuousDeploymentPolicyRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.continuous_deployment_policy_config

    aws_sdk_cloudfront.types.continuous_deployment_policy_config.serialize_xml(
        value["continuous_deployment_policy_config"],
        el,
        "ContinuousDeploymentPolicyConfig",
    )


def deserialize_xml(el: Element) -> UpdateContinuousDeploymentPolicyRequest:
    out: UpdateContinuousDeploymentPolicyRequest = {}  # type: ignore[typeddict-item]
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
    else:
        raise DeserializationError(
            "UpdateContinuousDeploymentPolicyRequest.continuous_deployment_policy_config required"
        )
    return out
