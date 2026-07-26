"""Generated from Smithy shape ``com.amazonaws.ec2#DisableSerialConsoleAccessResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class DisableSerialConsoleAccessResult(TypedDict, closed=True):
    serial_console_access_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, access to the EC2 serial console of all instances is enabled for your account. If <code>false</code>, access to the EC2 serial console of all instances is disabled for your account.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableSerialConsoleAccessResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serial_console_access_enabled" in value:
        pairs.append(
            (
                f"{prefix}.SerialConsoleAccessEnabled",
                "true" if value["serial_console_access_enabled"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> DisableSerialConsoleAccessResult:
    out: DisableSerialConsoleAccessResult = {}  # type: ignore[typeddict-item]
    child_serial_console_access_enabled = el.find("SerialConsoleAccessEnabled")
    if child_serial_console_access_enabled is not None:
        out["serial_console_access_enabled"] = (
            child_serial_console_access_enabled.text or ""
        ).lower() == "true"
    return out
