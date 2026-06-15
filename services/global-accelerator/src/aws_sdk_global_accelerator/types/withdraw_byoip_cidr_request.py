"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#WithdrawByoipCidrRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string


class WithdrawByoipCidrRequest(TypedDict):
    cidr: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    r"""<p>The address range, in CIDR notation.</p> <p> For more information, see <a href=\"https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html\">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WithdrawByoipCidrRequest) -> dict:
    out: dict = {}
    out["Cidr"] = value["cidr"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WithdrawByoipCidrRequest:
    out: WithdrawByoipCidrRequest = {}  # type: ignore[typeddict-item]
    if "Cidr" in data:
        out["cidr"] = data["Cidr"]
    else:
        raise DeserializationError("WithdrawByoipCidrRequest.cidr required")
    return out
