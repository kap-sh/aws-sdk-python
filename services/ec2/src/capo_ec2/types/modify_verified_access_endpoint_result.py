"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_endpoint


class ModifyVerifiedAccessEndpointResult(TypedDict, closed=True):
    verified_access_endpoint: NotRequired[
        "capo_ec2.types.verified_access_endpoint.VerifiedAccessEndpoint"
    ]
    """<p>Details about the Verified Access endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessEndpointResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_endpoint" in value:
        import capo_ec2.types.verified_access_endpoint

        capo_ec2.types.verified_access_endpoint.serialize_ec2_query(
            value["verified_access_endpoint"],
            pairs,
            f"{key_prefix}VerifiedAccessEndpoint",
        )


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessEndpointResult:
    out: ModifyVerifiedAccessEndpointResult = {}  # type: ignore[typeddict-item]
    child_verified_access_endpoint = el.find("verifiedAccessEndpoint")
    if child_verified_access_endpoint is not None:
        import capo_ec2.types.verified_access_endpoint

        out["verified_access_endpoint"] = (
            capo_ec2.types.verified_access_endpoint.deserialize_ec2_query(
                child_verified_access_endpoint
            )
        )
    return out
