"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.address_id


class DescribeAddressRequest(TypedDict):
    address_id: "aws_sdk_snowball.types.address_id.AddressId"
    """<p>The automatically generated ID for a specific address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAddressRequest) -> dict:
    out: dict = {}
    out["AddressId"] = value["address_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAddressRequest:
    out: DescribeAddressRequest = {}  # type: ignore[typeddict-item]
    if "AddressId" in data:
        out["address_id"] = data["AddressId"]
    else:
        raise DeserializationError("DescribeAddressRequest.address_id required")
    return out
