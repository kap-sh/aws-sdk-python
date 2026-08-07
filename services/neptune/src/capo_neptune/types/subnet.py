"""Generated from Smithy shape ``com.amazonaws.neptune#Subnet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.availability_zone
    import capo_neptune.types.string


class Subnet(TypedDict, closed=True):
    subnet_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the identifier of the subnet.</p>"""
    subnet_availability_zone: NotRequired[
        "capo_neptune.types.availability_zone.AvailabilityZone"
    ]
    """<p>Specifies the EC2 Availability Zone that the subnet is in.</p>"""
    subnet_status: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the status of the subnet.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Subnet, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subnet_identifier" in value:
        pairs.append((f"{key_prefix}SubnetIdentifier", str(value["subnet_identifier"])))
    if "subnet_availability_zone" in value:
        import capo_neptune.types.availability_zone

        capo_neptune.types.availability_zone.serialize_query(
            value["subnet_availability_zone"],
            pairs,
            f"{key_prefix}SubnetAvailabilityZone",
        )
    if "subnet_status" in value:
        pairs.append((f"{key_prefix}SubnetStatus", str(value["subnet_status"])))


def deserialize_query(el: Element) -> Subnet:
    out: Subnet = {}  # type: ignore[typeddict-item]
    child_subnet_identifier = el.find("SubnetIdentifier")
    if child_subnet_identifier is not None:
        out["subnet_identifier"] = str(child_subnet_identifier.text or "")
    child_subnet_availability_zone = el.find("SubnetAvailabilityZone")
    if child_subnet_availability_zone is not None:
        import capo_neptune.types.availability_zone

        out["subnet_availability_zone"] = (
            capo_neptune.types.availability_zone.deserialize_query(
                child_subnet_availability_zone
            )
        )
    child_subnet_status = el.find("SubnetStatus")
    if child_subnet_status is not None:
        out["subnet_status"] = str(child_subnet_status.text or "")
    return out
