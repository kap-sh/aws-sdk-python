"""Generated from Smithy shape ``com.amazonaws.cloudformation#AutoDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.auto_deployment_nullable
    import aws_sdk_cloudformation.types.retain_stacks_on_account_removal_nullable
    import aws_sdk_cloudformation.types.stack_set_arn_list


class AutoDeployment(TypedDict, closed=True):
    enabled: NotRequired[
        "aws_sdk_cloudformation.types.auto_deployment_nullable.AutoDeploymentNullable"
    ]
    """<p>If set to <code>true</code>, StackSets automatically deploys additional stack instances to Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.</p>"""
    retain_stacks_on_account_removal: NotRequired[
        "aws_sdk_cloudformation.types.retain_stacks_on_account_removal_nullable.RetainStacksOnAccountRemovalNullable"
    ]
    """<p>If set to <code>true</code>, stack resources are retained when an account is removed from a target organization or OU. If set to <code>false</code>, stack resources are deleted. Specify only if <code>Enabled</code> is set to <code>True</code>.</p>"""
    depends_on: NotRequired[
        "aws_sdk_cloudformation.types.stack_set_arn_list.StackSetARNList"
    ]
    """<p>A list of StackSet ARNs that this StackSet depends on for auto-deployment operations. When auto-deployment is triggered, operations will be sequenced to ensure all dependencies complete successfully before this StackSet's operation begins.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AutoDeployment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))
    if "retain_stacks_on_account_removal" in value:
        pairs.append(
            (
                f"{prefix}.RetainStacksOnAccountRemoval",
                "true" if value["retain_stacks_on_account_removal"] else "false",
            )
        )
    if "depends_on" in value:
        import aws_sdk_cloudformation.types.stack_set_arn_list

        aws_sdk_cloudformation.types.stack_set_arn_list.serialize_query(
            value["depends_on"], pairs, f"{prefix}.DependsOn"
        )


def deserialize_query(el: Element) -> AutoDeployment:
    out: AutoDeployment = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_retain_stacks_on_account_removal = el.find("RetainStacksOnAccountRemoval")
    if child_retain_stacks_on_account_removal is not None:
        out["retain_stacks_on_account_removal"] = (
            child_retain_stacks_on_account_removal.text or ""
        ).lower() == "true"
    child_depends_on = el.find("DependsOn")
    if child_depends_on is not None:
        import aws_sdk_cloudformation.types.stack_set_arn_list

        out["depends_on"] = (
            aws_sdk_cloudformation.types.stack_set_arn_list.deserialize_query(
                child_depends_on
            )
        )
    return out
