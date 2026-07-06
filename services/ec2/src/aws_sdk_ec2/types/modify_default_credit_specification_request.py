"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyDefaultCreditSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.unlimited_supported_instance_family


class ModifyDefaultCreditSpecificationRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_family: NotRequired[
        "aws_sdk_ec2.types.unlimited_supported_instance_family.UnlimitedSupportedInstanceFamily"
    ]
    """<p>The instance family.</p>"""
    cpu_credits: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The credit option for CPU usage of the instance family.</p> <p>Valid Values: <code>standard</code> | <code>unlimited</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyDefaultCreditSpecificationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "instance_family" in value:
        import aws_sdk_ec2.types.unlimited_supported_instance_family

        aws_sdk_ec2.types.unlimited_supported_instance_family.serialize_ec2_query(
            value["instance_family"], pairs, f"{prefix}.InstanceFamily"
        )
    if "cpu_credits" in value:
        pairs.append((f"{prefix}.CpuCredits", str(value["cpu_credits"])))


def deserialize_ec2_query(el: Element) -> ModifyDefaultCreditSpecificationRequest:
    out: ModifyDefaultCreditSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_family = el.find("InstanceFamily")
    if child_instance_family is not None:
        import aws_sdk_ec2.types.unlimited_supported_instance_family

        out["instance_family"] = (
            aws_sdk_ec2.types.unlimited_supported_instance_family.deserialize_ec2_query(
                child_instance_family
            )
        )
    child_cpu_credits = el.find("CpuCredits")
    if child_cpu_credits is not None:
        out["cpu_credits"] = str(child_cpu_credits.text or "")
    return out
