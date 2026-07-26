"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class AvailabilityZoneMessage(TypedDict, closed=True):
    message: NotRequired["capo_ec2.types.string.String"]
    """<p>The message about the Availability Zone, Local Zone, or Wavelength Zone.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> AvailabilityZoneMessage:
    out: AvailabilityZoneMessage = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
