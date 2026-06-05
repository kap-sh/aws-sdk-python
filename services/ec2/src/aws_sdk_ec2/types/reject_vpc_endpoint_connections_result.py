"""Generated from Smithy shape ``com.amazonaws.ec2#RejectVpcEndpointConnectionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unsuccessful_item_set


class RejectVpcEndpointConnectionsResult(TypedDict):
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_item_set.UnsuccessfulItemSet"
    ]
    """<p>Information about the endpoints that were not rejected, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RejectVpcEndpointConnectionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "unsuccessful" in value:
        import aws_sdk_ec2.types.unsuccessful_item_set

        aws_sdk_ec2.types.unsuccessful_item_set.serialize_ec2_query(
            value["unsuccessful"], pairs, f"{prefix}.Unsuccessful"
        )


def deserialize_ec2_query(el: Element) -> RejectVpcEndpointConnectionsResult:
    out: RejectVpcEndpointConnectionsResult = {}  # type: ignore[typeddict-item]
    if el.find("Unsuccessful") is not None:
        import aws_sdk_ec2.types.unsuccessful_item_set

        out["unsuccessful"] = (
            aws_sdk_ec2.types.unsuccessful_item_set.deserialize_ec2_query(
                el, "Unsuccessful"
            )
        )
    return out
