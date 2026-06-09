"""Generated from Smithy shape ``com.amazonaws.iam#DelegationPermission``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.policy_parameter_list_type


class DelegationPermission(TypedDict):
    policy_template_arn: NotRequired["aws_sdk_iam.types.arn_type.arnType"]
    """<p>This ARN maps to a pre-registered policy content for this partner. See the <a href=\"\">partner onboarding documentation</a> to understand how to create a delegation template.</p>"""
    parameters: NotRequired[
        "aws_sdk_iam.types.policy_parameter_list_type.policyParameterListType"
    ]
    """<p>A list of policy parameters that define the scope and constraints of the delegated permissions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DelegationPermission, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy_template_arn" in value:
        pairs.append((f"{prefix}.PolicyTemplateArn", str(value["policy_template_arn"])))
    if "parameters" in value:
        import aws_sdk_iam.types.policy_parameter_list_type

        aws_sdk_iam.types.policy_parameter_list_type.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )


def deserialize_query(el: Element) -> DelegationPermission:
    out: DelegationPermission = {}  # type: ignore[typeddict-item]
    child_policy_template_arn = el.find("PolicyTemplateArn")
    if child_policy_template_arn is not None:
        out["policy_template_arn"] = str(child_policy_template_arn.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import aws_sdk_iam.types.policy_parameter_list_type

        out["parameters"] = (
            aws_sdk_iam.types.policy_parameter_list_type.deserialize_query(
                child_parameters
            )
        )
    return out
