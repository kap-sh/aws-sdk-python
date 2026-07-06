"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptVpcEndpointConnectionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unsuccessful_item_set


class AcceptVpcEndpointConnectionsResult(TypedDict, closed=True):
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_item_set.UnsuccessfulItemSet"
    ]
    """<p>Information about the interface endpoints that were not accepted, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceptVpcEndpointConnectionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "unsuccessful" in value:
        import aws_sdk_ec2.types.unsuccessful_item_set

        aws_sdk_ec2.types.unsuccessful_item_set.serialize_ec2_query(
            value["unsuccessful"], pairs, f"{prefix}.Unsuccessful"
        )


def deserialize_ec2_query(el: Element) -> AcceptVpcEndpointConnectionsResult:
    out: AcceptVpcEndpointConnectionsResult = {}  # type: ignore[typeddict-item]
    if el.find("Unsuccessful") is not None:
        import aws_sdk_ec2.types.unsuccessful_item_set

        out["unsuccessful"] = (
            aws_sdk_ec2.types.unsuccessful_item_set.deserialize_ec2_query(
                el, "Unsuccessful"
            )
        )
    return out
