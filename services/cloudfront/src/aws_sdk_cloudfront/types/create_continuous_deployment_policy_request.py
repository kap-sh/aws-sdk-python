"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateContinuousDeploymentPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.continuous_deployment_policy_config


class CreateContinuousDeploymentPolicyRequest(TypedDict):
    continuous_deployment_policy_config: "aws_sdk_cloudfront.types.continuous_deployment_policy_config.ContinuousDeploymentPolicyConfig"
    """<p>Contains the configuration for a continuous deployment policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateContinuousDeploymentPolicyRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.continuous_deployment_policy_config

    aws_sdk_cloudfront.types.continuous_deployment_policy_config.serialize_xml(
        value["continuous_deployment_policy_config"],
        el,
        "ContinuousDeploymentPolicyConfig",
    )


def deserialize_xml(el: Element) -> CreateContinuousDeploymentPolicyRequest:
    out: CreateContinuousDeploymentPolicyRequest = {}  # type: ignore[typeddict-item]
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
            "CreateContinuousDeploymentPolicyRequest.continuous_deployment_policy_config required"
        )
    return out
