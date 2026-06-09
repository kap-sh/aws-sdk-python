"""Generated from Smithy shape ``com.amazonaws.ec2#SupportedRegionDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class SupportedRegionDetail(TypedDict):
    region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region code.</p>"""
    service_state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The service state. The possible values are <code>Pending</code>, <code>Available</code>, <code>Deleting</code>, <code>Deleted</code>, <code>Failed</code>, and <code>Closed</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SupportedRegionDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "region" in value:
        pairs.append((f"{prefix}.Region", str(value["region"])))
    if "service_state" in value:
        pairs.append((f"{prefix}.ServiceState", str(value["service_state"])))


def deserialize_ec2_query(el: Element) -> SupportedRegionDetail:
    out: SupportedRegionDetail = {}  # type: ignore[typeddict-item]
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_service_state = el.find("ServiceState")
    if child_service_state is not None:
        out["service_state"] = str(child_service_state.text or "")
    return out
