"""Generated from Smithy shape ``com.amazonaws.cloudformation#UpdateTerminationProtectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.enable_termination_protection
    import aws_sdk_cloudformation.types.stack_name_or_id


class UpdateTerminationProtectionInput(TypedDict, closed=True):
    enable_termination_protection: NotRequired[
        "aws_sdk_cloudformation.types.enable_termination_protection.EnableTerminationProtection"
    ]
    """<p>Whether to enable termination protection on the specified stack.</p>"""
    stack_name: NotRequired[
        "aws_sdk_cloudformation.types.stack_name_or_id.StackNameOrId"
    ]
    """<p>The name or unique ID of the stack for which you want to set termination protection.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateTerminationProtectionInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "enable_termination_protection" in value:
        pairs.append(
            (
                f"{prefix}.EnableTerminationProtection",
                "true" if value["enable_termination_protection"] else "false",
            )
        )
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))


def deserialize_query(el: Element) -> UpdateTerminationProtectionInput:
    out: UpdateTerminationProtectionInput = {}  # type: ignore[typeddict-item]
    child_enable_termination_protection = el.find("EnableTerminationProtection")
    if child_enable_termination_protection is not None:
        out["enable_termination_protection"] = (
            child_enable_termination_protection.text or ""
        ).lower() == "true"
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    return out
