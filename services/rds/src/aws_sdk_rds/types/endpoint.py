"""Generated from Smithy shape ``com.amazonaws.rds#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.integer
    import aws_sdk_rds.types.string


class Endpoint(TypedDict, closed=True):
    address: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Specifies the DNS address of the DB instance.</p>"""
    port: NotRequired["aws_sdk_rds.types.integer.Integer"]
    """<p>Specifies the port that the database engine is listening on.</p>"""
    hosted_zone_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Endpoint, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "address" in value:
        pairs.append((f"{prefix}.Address", str(value["address"])))
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "hosted_zone_id" in value:
        pairs.append((f"{prefix}.HostedZoneId", str(value["hosted_zone_id"])))


def deserialize_query(el: Element) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    child_address = el.find("Address")
    if child_address is not None:
        out["address"] = str(child_address.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    return out
