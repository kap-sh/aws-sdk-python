"""Generated from Smithy shape ``com.amazonaws.drs#SourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.cpus
    import capo_drs.types.disks
    import capo_drs.types.ec2_instance_type
    import capo_drs.types.identification_hints
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.network_interfaces
    import capo_drs.types.os
    import capo_drs.types.positive_integer


class SourceProperties(TypedDict, closed=True):
    last_updated_date_time: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time the Source Properties were last updated on.</p>"""
    recommended_instance_type: NotRequired[
        "capo_drs.types.ec2_instance_type.EC2InstanceType"
    ]
    """<p>The recommended EC2 instance type that will be used when recovering the Source Server.</p>"""
    identification_hints: NotRequired[
        "capo_drs.types.identification_hints.IdentificationHints"
    ]
    """<p>Hints used to uniquely identify a machine.</p>"""
    network_interfaces: NotRequired[
        "capo_drs.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>An array of network interfaces.</p>"""
    disks: NotRequired["capo_drs.types.disks.Disks"]
    """<p>An array of disks.</p>"""
    cpus: NotRequired["capo_drs.types.cpus.Cpus"]
    """<p>An array of CPUs.</p>"""
    ram_bytes: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>The amount of RAM in bytes.</p>"""
    os: NotRequired["capo_drs.types.os.OS"]
    """<p>Operating system.</p>"""
    supports_nitro_instances: NotRequired["bool"]
    """<p>Are EC2 nitro instance types supported when recovering the Source Server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceProperties) -> dict:
    out: dict = {}
    if "last_updated_date_time" in value:
        out["lastUpdatedDateTime"] = value["last_updated_date_time"]
    if "recommended_instance_type" in value:
        out["recommendedInstanceType"] = value["recommended_instance_type"]
    if "identification_hints" in value:
        import capo_drs.types.identification_hints

        out["identificationHints"] = capo_drs.types.identification_hints.serialize_json(
            value["identification_hints"]
        )
    if "network_interfaces" in value:
        import capo_drs.types.network_interfaces

        out["networkInterfaces"] = capo_drs.types.network_interfaces.serialize_json(
            value["network_interfaces"]
        )
    if "disks" in value:
        import capo_drs.types.disks

        out["disks"] = capo_drs.types.disks.serialize_json(value["disks"])
    if "cpus" in value:
        import capo_drs.types.cpus

        out["cpus"] = capo_drs.types.cpus.serialize_json(value["cpus"])
    out["ramBytes"] = value.get("ram_bytes", 0)
    if "os" in value:
        import capo_drs.types.os

        out["os"] = capo_drs.types.os.serialize_json(value["os"])
    if "supports_nitro_instances" in value:
        out["supportsNitroInstances"] = value["supports_nitro_instances"]
    return out


def deserialize_json(data: dict) -> SourceProperties:
    out: SourceProperties = {}  # type: ignore[typeddict-item]
    if "lastUpdatedDateTime" in data:
        out["last_updated_date_time"] = data["lastUpdatedDateTime"]
    if "recommendedInstanceType" in data:
        out["recommended_instance_type"] = data["recommendedInstanceType"]
    if "identificationHints" in data:
        import capo_drs.types.identification_hints

        out["identification_hints"] = (
            capo_drs.types.identification_hints.deserialize_json(
                data["identificationHints"]
            )
        )
    if "networkInterfaces" in data:
        import capo_drs.types.network_interfaces

        out["network_interfaces"] = capo_drs.types.network_interfaces.deserialize_json(
            data["networkInterfaces"]
        )
    if "disks" in data:
        import capo_drs.types.disks

        out["disks"] = capo_drs.types.disks.deserialize_json(data["disks"])
    if "cpus" in data:
        import capo_drs.types.cpus

        out["cpus"] = capo_drs.types.cpus.deserialize_json(data["cpus"])
    if "ramBytes" in data:
        out["ram_bytes"] = data["ramBytes"]
    else:
        out["ram_bytes"] = 0
    if "os" in data:
        import capo_drs.types.os

        out["os"] = capo_drs.types.os.deserialize_json(data["os"])
    if "supportsNitroInstances" in data:
        out["supports_nitro_instances"] = data["supportsNitroInstances"]
    return out
