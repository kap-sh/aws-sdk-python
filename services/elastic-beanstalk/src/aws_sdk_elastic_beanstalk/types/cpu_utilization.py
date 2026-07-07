"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CPUUtilization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.nullable_double


class CPUUtilization(TypedDict, closed=True):
    user: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>Percentage of time that the CPU has spent in the <code>User</code> state over the last 10 seconds.</p>"""
    nice: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>Available on Linux environments only.</p> <p>Percentage of time that the CPU has spent in the <code>Nice</code> state over the last 10 seconds.</p>"""
    system: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"
    ]
    """<p>Available on Linux environments only.</p> <p>Percentage of time that the CPU has spent in the <code>System</code> state over the last 10 seconds.</p>"""
    idle: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>Percentage of time that the CPU has spent in the <code>Idle</code> state over the last 10 seconds.</p>"""
    io_wait: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"
    ]
    """<p>Available on Linux environments only.</p> <p>Percentage of time that the CPU has spent in the <code>I/O Wait</code> state over the last 10 seconds.</p>"""
    irq: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>Available on Linux environments only.</p> <p>Percentage of time that the CPU has spent in the <code>IRQ</code> state over the last 10 seconds.</p>"""
    soft_irq: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"
    ]
    """<p>Available on Linux environments only.</p> <p>Percentage of time that the CPU has spent in the <code>SoftIRQ</code> state over the last 10 seconds.</p>"""
    privileged: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"
    ]
    """<p>Available on Windows environments only.</p> <p>Percentage of time that the CPU has spent in the <code>Privileged</code> state over the last 10 seconds.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CPUUtilization, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user" in value:
        pairs.append((f"{prefix}.User", str(value["user"])))
    if "nice" in value:
        pairs.append((f"{prefix}.Nice", str(value["nice"])))
    if "system" in value:
        pairs.append((f"{prefix}.System", str(value["system"])))
    if "idle" in value:
        pairs.append((f"{prefix}.Idle", str(value["idle"])))
    if "io_wait" in value:
        pairs.append((f"{prefix}.IOWait", str(value["io_wait"])))
    if "irq" in value:
        pairs.append((f"{prefix}.IRQ", str(value["irq"])))
    if "soft_irq" in value:
        pairs.append((f"{prefix}.SoftIRQ", str(value["soft_irq"])))
    if "privileged" in value:
        pairs.append((f"{prefix}.Privileged", str(value["privileged"])))


def deserialize_query(el: Element) -> CPUUtilization:
    out: CPUUtilization = {}  # type: ignore[typeddict-item]
    child_user = el.find("User")
    if child_user is not None:
        out["user"] = float(child_user.text or "")
    child_nice = el.find("Nice")
    if child_nice is not None:
        out["nice"] = float(child_nice.text or "")
    child_system = el.find("System")
    if child_system is not None:
        out["system"] = float(child_system.text or "")
    child_idle = el.find("Idle")
    if child_idle is not None:
        out["idle"] = float(child_idle.text or "")
    child_io_wait = el.find("IOWait")
    if child_io_wait is not None:
        out["io_wait"] = float(child_io_wait.text or "")
    child_irq = el.find("IRQ")
    if child_irq is not None:
        out["irq"] = float(child_irq.text or "")
    child_soft_irq = el.find("SoftIRQ")
    if child_soft_irq is not None:
        out["soft_irq"] = float(child_soft_irq.text or "")
    child_privileged = el.find("Privileged")
    if child_privileged is not None:
        out["privileged"] = float(child_privileged.text or "")
    return out
