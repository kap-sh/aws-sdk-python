"""Generated from Smithy shape ``com.amazonaws.ec2#GetDefaultCreditSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.unlimited_supported_instance_family


class GetDefaultCreditSpecificationRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_family: NotRequired[
        "capo_ec2.types.unlimited_supported_instance_family.UnlimitedSupportedInstanceFamily"
    ]
    """<p>The instance family.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetDefaultCreditSpecificationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_family" in value:
        import capo_ec2.types.unlimited_supported_instance_family

        capo_ec2.types.unlimited_supported_instance_family.serialize_ec2_query(
            value["instance_family"], pairs, f"{key_prefix}InstanceFamily"
        )


def deserialize_ec2_query(el: Element) -> GetDefaultCreditSpecificationRequest:
    out: GetDefaultCreditSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_family = el.find("InstanceFamily")
    if child_instance_family is not None:
        import capo_ec2.types.unlimited_supported_instance_family

        out["instance_family"] = (
            capo_ec2.types.unlimited_supported_instance_family.deserialize_ec2_query(
                child_instance_family
            )
        )
    return out
