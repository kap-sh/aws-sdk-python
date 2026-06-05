"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_endpoint


class ModifyVerifiedAccessEndpointResult(TypedDict):
    verified_access_endpoint: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint.VerifiedAccessEndpoint"
    ]
    """<p>Details about the Verified Access endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessEndpointResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "verified_access_endpoint" in value:
        import aws_sdk_ec2.types.verified_access_endpoint

        aws_sdk_ec2.types.verified_access_endpoint.serialize_ec2_query(
            value["verified_access_endpoint"], pairs, f"{prefix}.VerifiedAccessEndpoint"
        )


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessEndpointResult:
    out: ModifyVerifiedAccessEndpointResult = {}  # type: ignore[typeddict-item]
    child_verified_access_endpoint = el.find("VerifiedAccessEndpoint")
    if child_verified_access_endpoint is not None:
        import aws_sdk_ec2.types.verified_access_endpoint

        out["verified_access_endpoint"] = (
            aws_sdk_ec2.types.verified_access_endpoint.deserialize_ec2_query(
                child_verified_access_endpoint
            )
        )
    return out
