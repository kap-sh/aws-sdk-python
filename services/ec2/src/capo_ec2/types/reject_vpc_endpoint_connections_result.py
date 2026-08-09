"""Generated from Smithy shape ``com.amazonaws.ec2#RejectVpcEndpointConnectionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.unsuccessful_item_set


class RejectVpcEndpointConnectionsResult(TypedDict, closed=True):
    unsuccessful: NotRequired[
        "capo_ec2.types.unsuccessful_item_set.UnsuccessfulItemSet"
    ]
    """<p>Information about the endpoints that were not rejected, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RejectVpcEndpointConnectionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "unsuccessful" in value:
        import capo_ec2.types.unsuccessful_item_set

        capo_ec2.types.unsuccessful_item_set.serialize_ec2_query(
            value["unsuccessful"], pairs, f"{key_prefix}Unsuccessful"
        )


def deserialize_ec2_query(el: Element) -> RejectVpcEndpointConnectionsResult:
    out: RejectVpcEndpointConnectionsResult = {}  # type: ignore[typeddict-item]
    child_unsuccessful = el.find("unsuccessful")
    if child_unsuccessful is not None:
        import capo_ec2.types.unsuccessful_item_set

        out["unsuccessful"] = (
            capo_ec2.types.unsuccessful_item_set.deserialize_ec2_query(
                child_unsuccessful
            )
        )
    return out
