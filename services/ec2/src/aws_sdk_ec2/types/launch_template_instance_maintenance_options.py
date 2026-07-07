"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceMaintenanceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_auto_recovery_state


class LaunchTemplateInstanceMaintenanceOptions(TypedDict, closed=True):
    auto_recovery: NotRequired[
        "aws_sdk_ec2.types.launch_template_auto_recovery_state.LaunchTemplateAutoRecoveryState"
    ]
    """<p>Disables the automatic recovery behavior of your instance or sets it to default.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateInstanceMaintenanceOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "auto_recovery" in value:
        import aws_sdk_ec2.types.launch_template_auto_recovery_state

        aws_sdk_ec2.types.launch_template_auto_recovery_state.serialize_ec2_query(
            value["auto_recovery"], pairs, f"{prefix}.AutoRecovery"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateInstanceMaintenanceOptions:
    out: LaunchTemplateInstanceMaintenanceOptions = {}  # type: ignore[typeddict-item]
    child_auto_recovery = el.find("AutoRecovery")
    if child_auto_recovery is not None:
        import aws_sdk_ec2.types.launch_template_auto_recovery_state

        out["auto_recovery"] = (
            aws_sdk_ec2.types.launch_template_auto_recovery_state.deserialize_ec2_query(
                child_auto_recovery
            )
        )
    return out
