"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#WithdrawByoipCidrResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.byoip_cidr


class WithdrawByoipCidrResponse(TypedDict, closed=True):
    byoip_cidr: NotRequired["capo_global_accelerator.types.byoip_cidr.ByoipCidr"]
    """<p>Information about the BYOIP address pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WithdrawByoipCidrResponse) -> dict:
    out: dict = {}
    if "byoip_cidr" in value:
        import capo_global_accelerator.types.byoip_cidr

        out["ByoipCidr"] = (
            capo_global_accelerator.types.byoip_cidr.serialize_aws_json_1_1(
                value["byoip_cidr"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WithdrawByoipCidrResponse:
    out: WithdrawByoipCidrResponse = {}  # type: ignore[typeddict-item]
    if "ByoipCidr" in data:
        import capo_global_accelerator.types.byoip_cidr

        out["byoip_cidr"] = (
            capo_global_accelerator.types.byoip_cidr.deserialize_aws_json_1_1(
                data["ByoipCidr"]
            )
        )
    return out
