"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListContinuousDeploymentPoliciesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.continuous_deployment_policy_list


class ListContinuousDeploymentPoliciesResult(TypedDict, closed=True):
    continuous_deployment_policy_list: NotRequired[
        "aws_sdk_cloudfront.types.continuous_deployment_policy_list.ContinuousDeploymentPolicyList"
    ]
    """<p>A list of continuous deployment policies.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListContinuousDeploymentPoliciesResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "continuous_deployment_policy_list" in value:
        import aws_sdk_cloudfront.types.continuous_deployment_policy_list

        aws_sdk_cloudfront.types.continuous_deployment_policy_list.serialize_xml(
            value["continuous_deployment_policy_list"],
            el,
            "ContinuousDeploymentPolicyList",
        )


def deserialize_xml(el: Element) -> ListContinuousDeploymentPoliciesResult:
    out: ListContinuousDeploymentPoliciesResult = {}  # type: ignore[typeddict-item]
    child_continuous_deployment_policy_list = el.find("ContinuousDeploymentPolicyList")
    if child_continuous_deployment_policy_list is not None:
        import aws_sdk_cloudfront.types.continuous_deployment_policy_list

        out["continuous_deployment_policy_list"] = (
            aws_sdk_cloudfront.types.continuous_deployment_policy_list.deserialize_xml(
                child_continuous_deployment_policy_list
            )
        )
    return out
