"""Generated from Smithy shape ``com.amazonaws.ec2#GetSerialConsoleAccessStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.managed_by


class GetSerialConsoleAccessStatusResult(TypedDict, closed=True):
    serial_console_access_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, access to the EC2 serial console of all instances is enabled for your account. If <code>false</code>, access to the EC2 serial console of all instances is disabled for your account.</p>"""
    managed_by: NotRequired["capo_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages access to the serial console. Possible values include:</p> <ul> <li> <p> <code>account</code> - Access is managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - Access is managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetSerialConsoleAccessStatusResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "serial_console_access_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}SerialConsoleAccessEnabled",
                "true" if value["serial_console_access_enabled"] else "false",
            )
        )
    if "managed_by" in value:
        import capo_ec2.types.managed_by

        capo_ec2.types.managed_by.serialize_ec2_query(
            value["managed_by"], pairs, f"{key_prefix}ManagedBy"
        )


def deserialize_ec2_query(el: Element) -> GetSerialConsoleAccessStatusResult:
    out: GetSerialConsoleAccessStatusResult = {}  # type: ignore[typeddict-item]
    child_serial_console_access_enabled = el.find("serialConsoleAccessEnabled")
    if child_serial_console_access_enabled is not None:
        out["serial_console_access_enabled"] = (
            child_serial_console_access_enabled.text or ""
        ).lower() == "true"
    child_managed_by = el.find("managedBy")
    if child_managed_by is not None:
        import capo_ec2.types.managed_by

        out["managed_by"] = capo_ec2.types.managed_by.deserialize_ec2_query(
            child_managed_by
        )
    return out
