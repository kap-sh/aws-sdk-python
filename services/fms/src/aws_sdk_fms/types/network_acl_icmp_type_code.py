"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclIcmpTypeCode``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.integer_object


class NetworkAclIcmpTypeCode(TypedDict):
    code: NotRequired["aws_sdk_fms.types.integer_object.IntegerObject"]
    """<p>ICMP code. </p>"""
    type: NotRequired["aws_sdk_fms.types.integer_object.IntegerObject"]
    """<p>ICMP type. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAclIcmpTypeCode) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkAclIcmpTypeCode:
    out: NetworkAclIcmpTypeCode = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
