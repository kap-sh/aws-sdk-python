"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolCidrFailureReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_pool_cidr_failure_code
    import capo_ec2.types.string


class IpamPoolCidrFailureReason(TypedDict, closed=True):
    code: NotRequired[
        "capo_ec2.types.ipam_pool_cidr_failure_code.IpamPoolCidrFailureCode"
    ]
    """<p>An error code related to why an IPAM pool CIDR failed to be provisioned.</p>"""
    message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message related to why an IPAM pool CIDR failed to be provisioned.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPoolCidrFailureReason, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        import capo_ec2.types.ipam_pool_cidr_failure_code

        capo_ec2.types.ipam_pool_cidr_failure_code.serialize_ec2_query(
            value["code"], pairs, f"{key_prefix}Code"
        )
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> IpamPoolCidrFailureReason:
    out: IpamPoolCidrFailureReason = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import capo_ec2.types.ipam_pool_cidr_failure_code

        out["code"] = capo_ec2.types.ipam_pool_cidr_failure_code.deserialize_ec2_query(
            child_code
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
