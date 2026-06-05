"""Generated from Smithy shape ``com.amazonaws.ec2#CreditSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CreditSpecification(TypedDict):
    cpu_credits: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The credit option for CPU usage of a T instance.</p> <p>Valid values: <code>standard</code> | <code>unlimited</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreditSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cpu_credits" in value:
        pairs.append((f"{prefix}.CpuCredits", str(value["cpu_credits"])))


def deserialize_ec2_query(el: Element) -> CreditSpecification:
    out: CreditSpecification = {}  # type: ignore[typeddict-item]
    child_cpu_credits = el.find("CpuCredits")
    if child_cpu_credits is not None:
        out["cpu_credits"] = str(child_cpu_credits.text or "")
    return out
