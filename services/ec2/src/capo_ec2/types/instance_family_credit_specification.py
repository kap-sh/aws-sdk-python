"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceFamilyCreditSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.unlimited_supported_instance_family


class InstanceFamilyCreditSpecification(TypedDict, closed=True):
    instance_family: NotRequired[
        "capo_ec2.types.unlimited_supported_instance_family.UnlimitedSupportedInstanceFamily"
    ]
    """<p>The instance family.</p>"""
    cpu_credits: NotRequired["capo_ec2.types.string.String"]
    """<p>The default credit option for CPU usage of the instance family. Valid values are <code>standard</code> and <code>unlimited</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceFamilyCreditSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_family" in value:
        import capo_ec2.types.unlimited_supported_instance_family

        capo_ec2.types.unlimited_supported_instance_family.serialize_ec2_query(
            value["instance_family"], pairs, f"{key_prefix}InstanceFamily"
        )
    if "cpu_credits" in value:
        pairs.append((f"{key_prefix}CpuCredits", str(value["cpu_credits"])))


def deserialize_ec2_query(el: Element) -> InstanceFamilyCreditSpecification:
    out: InstanceFamilyCreditSpecification = {}  # type: ignore[typeddict-item]
    child_instance_family = el.find("instanceFamily")
    if child_instance_family is not None:
        import capo_ec2.types.unlimited_supported_instance_family

        out["instance_family"] = (
            capo_ec2.types.unlimited_supported_instance_family.deserialize_ec2_query(
                child_instance_family
            )
        )
    child_cpu_credits = el.find("cpuCredits")
    if child_cpu_credits is not None:
        out["cpu_credits"] = str(child_cpu_credits.text or "")
    return out
