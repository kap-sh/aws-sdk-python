"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRouteTableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_table
    import capo_ec2.types.string


class CreateRouteTableResult(TypedDict, closed=True):
    route_table: NotRequired["capo_ec2.types.route_table.RouteTable"]
    """<p>Information about the route table.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateRouteTableResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_table" in value:
        import capo_ec2.types.route_table

        capo_ec2.types.route_table.serialize_ec2_query(
            value["route_table"], pairs, f"{key_prefix}RouteTable"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateRouteTableResult:
    out: CreateRouteTableResult = {}  # type: ignore[typeddict-item]
    child_route_table = el.find("RouteTable")
    if child_route_table is not None:
        import capo_ec2.types.route_table

        out["route_table"] = capo_ec2.types.route_table.deserialize_ec2_query(
            child_route_table
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
