"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AdvertiseByoipCidrResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.byoip_cidr


class AdvertiseByoipCidrResponse(TypedDict):
    byoip_cidr: NotRequired["aws_sdk_global_accelerator.types.byoip_cidr.ByoipCidr"]
    """<p>Information about the address range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdvertiseByoipCidrResponse) -> dict:
    out: dict = {}
    if "byoip_cidr" in value:
        import aws_sdk_global_accelerator.types.byoip_cidr

        out["ByoipCidr"] = (
            aws_sdk_global_accelerator.types.byoip_cidr.serialize_aws_json_1_1(
                value["byoip_cidr"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdvertiseByoipCidrResponse:
    out: AdvertiseByoipCidrResponse = {}  # type: ignore[typeddict-item]
    if "ByoipCidr" in data:
        import aws_sdk_global_accelerator.types.byoip_cidr

        out["byoip_cidr"] = (
            aws_sdk_global_accelerator.types.byoip_cidr.deserialize_aws_json_1_1(
                data["ByoipCidr"]
            )
        )
    return out
