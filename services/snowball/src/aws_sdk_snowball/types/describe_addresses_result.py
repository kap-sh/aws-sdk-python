"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeAddressesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.address_list
    import aws_sdk_snowball.types.string


class DescribeAddressesResult(TypedDict):
    addresses: NotRequired["aws_sdk_snowball.types.address_list.AddressList"]
    """<p>The Snow device shipping addresses that were created for this account.</p>"""
    next_token: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>HTTP requests are stateless. If you use the automatically generated <code>NextToken</code> value in your next <code>DescribeAddresses</code> call, your list of returned addresses will start from this point in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAddressesResult) -> dict:
    out: dict = {}
    if "addresses" in value:
        import aws_sdk_snowball.types.address_list

        out["Addresses"] = aws_sdk_snowball.types.address_list.serialize_aws_json_1_1(
            value["addresses"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAddressesResult:
    out: DescribeAddressesResult = {}  # type: ignore[typeddict-item]
    if "Addresses" in data:
        import aws_sdk_snowball.types.address_list

        out["addresses"] = aws_sdk_snowball.types.address_list.deserialize_aws_json_1_1(
            data["Addresses"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
