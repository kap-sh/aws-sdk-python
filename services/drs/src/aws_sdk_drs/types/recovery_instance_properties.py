"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceProperties``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.cpus
    import aws_sdk_drs.types.identification_hints
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.network_interfaces
    import aws_sdk_drs.types.os
    import aws_sdk_drs.types.positive_integer
    import aws_sdk_drs.types.recovery_instance_disks

class RecoveryInstanceProperties(TypedDict):
    last_updated_date_time: NotRequired["aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"]
    """<p>The date and time the Recovery Instance properties were last updated on.</p>"""
    identification_hints: NotRequired["aws_sdk_drs.types.identification_hints.IdentificationHints"]
    """<p>Hints used to uniquely identify a machine.</p>"""
    network_interfaces: NotRequired["aws_sdk_drs.types.network_interfaces.NetworkInterfaces"]
    """<p>An array of network interfaces.</p>"""
    disks: NotRequired["aws_sdk_drs.types.recovery_instance_disks.RecoveryInstanceDisks"]
    """<p>An array of disks.</p>"""
    cpus: NotRequired["aws_sdk_drs.types.cpus.Cpus"]
    """<p>An array of CPUs.</p>"""
    ram_bytes: "aws_sdk_drs.types.positive_integer.PositiveInteger"
    """<p>The amount of RAM in bytes.</p>"""
    os: NotRequired["aws_sdk_drs.types.os.OS"]
    """<p>Operating system.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceProperties) -> dict:
    out: dict = {}
    if "last_updated_date_time" in value:
        out["lastUpdatedDateTime"] = value["last_updated_date_time"]
    if "identification_hints" in value:
        import aws_sdk_drs.types.identification_hints
        out["identificationHints"] = aws_sdk_drs.types.identification_hints.serialize_json(value["identification_hints"])
    if "network_interfaces" in value:
        import aws_sdk_drs.types.network_interfaces
        out["networkInterfaces"] = aws_sdk_drs.types.network_interfaces.serialize_json(value["network_interfaces"])
    if "disks" in value:
        import aws_sdk_drs.types.recovery_instance_disks
        out["disks"] = aws_sdk_drs.types.recovery_instance_disks.serialize_json(value["disks"])
    if "cpus" in value:
        import aws_sdk_drs.types.cpus
        out["cpus"] = aws_sdk_drs.types.cpus.serialize_json(value["cpus"])
    out["ramBytes"] = value.get("ram_bytes", 0)
    if "os" in value:
        import aws_sdk_drs.types.os
        out["os"] = aws_sdk_drs.types.os.serialize_json(value["os"])
    return out


def deserialize_json(data: dict) -> RecoveryInstanceProperties:
    out: RecoveryInstanceProperties = {}  # type: ignore[typeddict-item]
    if "lastUpdatedDateTime" in data:
        out["last_updated_date_time"] = data["lastUpdatedDateTime"]
    if "identificationHints" in data:
        import aws_sdk_drs.types.identification_hints
        out["identification_hints"] = aws_sdk_drs.types.identification_hints.deserialize_json(data["identificationHints"])
    if "networkInterfaces" in data:
        import aws_sdk_drs.types.network_interfaces
        out["network_interfaces"] = aws_sdk_drs.types.network_interfaces.deserialize_json(data["networkInterfaces"])
    if "disks" in data:
        import aws_sdk_drs.types.recovery_instance_disks
        out["disks"] = aws_sdk_drs.types.recovery_instance_disks.deserialize_json(data["disks"])
    if "cpus" in data:
        import aws_sdk_drs.types.cpus
        out["cpus"] = aws_sdk_drs.types.cpus.deserialize_json(data["cpus"])
    if "ramBytes" in data:
        out["ram_bytes"] = data["ramBytes"]
    else:
        out["ram_bytes"] = 0
    if "os" in data:
        import aws_sdk_drs.types.os
        out["os"] = aws_sdk_drs.types.os.deserialize_json(data["os"])
    return out