"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.tag_list
    import capo_ec2.types.transit_gateway_id
    import capo_ec2.types.transit_gateway_policy_table_id
    import capo_ec2.types.transit_gateway_policy_table_state


class TransitGatewayPolicyTable(TypedDict, closed=True):
    transit_gateway_policy_table_id: NotRequired[
        "capo_ec2.types.transit_gateway_policy_table_id.TransitGatewayPolicyTableId"
    ]
    """<p>The ID of the transit gateway policy table.</p>"""
    transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_policy_table_state.TransitGatewayPolicyTableState"
    ]
    """<p>The state of the transit gateway policy table</p>"""
    creation_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The timestamp when the transit gateway policy table was created.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>he key-value pairs associated with the transit gateway policy table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPolicyTable, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_policy_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayPolicyTableId",
                str(value["transit_gateway_policy_table_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "state" in value:
        import capo_ec2.types.transit_gateway_policy_table_state

        capo_ec2.types.transit_gateway_policy_table_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "creation_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayPolicyTable:
    out: TransitGatewayPolicyTable = {}  # type: ignore[typeddict-item]
    child_transit_gateway_policy_table_id = el.find("TransitGatewayPolicyTableId")
    if child_transit_gateway_policy_table_id is not None:
        out["transit_gateway_policy_table_id"] = str(
            child_transit_gateway_policy_table_id.text or ""
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_policy_table_state

        out["state"] = (
            capo_ec2.types.transit_gateway_policy_table_state.deserialize_ec2_query(
                child_state
            )
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import capo_ec2.types.date_time

        out["creation_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
