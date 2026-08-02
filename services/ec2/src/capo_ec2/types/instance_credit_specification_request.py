"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCreditSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_id
    import capo_ec2.types.string


class InstanceCreditSpecificationRequest(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    cpu_credits: NotRequired["capo_ec2.types.string.String"]
    """<p>The credit option for CPU usage of the instance.</p> <p>Valid values: <code>standard</code> | <code>unlimited</code> </p> <p>T3 instances with <code>host</code> tenancy do not support the <code>unlimited</code> CPU credit option.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceCreditSpecificationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "cpu_credits" in value:
        pairs.append((f"{key_prefix}CpuCredits", str(value["cpu_credits"])))


def deserialize_ec2_query(el: Element) -> InstanceCreditSpecificationRequest:
    out: InstanceCreditSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_cpu_credits = el.find("CpuCredits")
    if child_cpu_credits is not None:
        out["cpu_credits"] = str(child_cpu_credits.text or "")
    return out
