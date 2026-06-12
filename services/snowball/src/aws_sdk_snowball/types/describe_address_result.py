"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeAddressResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.address


class DescribeAddressResult(TypedDict):
    address: NotRequired["aws_sdk_snowball.types.address.Address"]
    """<p>The address that you want the Snow device(s) associated with a specific job to be shipped to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAddressResult) -> dict:
    out: dict = {}
    if "address" in value:
        import aws_sdk_snowball.types.address

        out["Address"] = aws_sdk_snowball.types.address.serialize_aws_json_1_1(
            value["address"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAddressResult:
    out: DescribeAddressResult = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        import aws_sdk_snowball.types.address

        out["address"] = aws_sdk_snowball.types.address.deserialize_aws_json_1_1(
            data["Address"]
        )
    return out
