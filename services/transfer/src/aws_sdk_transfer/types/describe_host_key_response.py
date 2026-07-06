"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeHostKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.described_host_key


class DescribeHostKeyResponse(TypedDict, closed=True):
    host_key: "aws_sdk_transfer.types.described_host_key.DescribedHostKey"
    """<p>Returns the details for the specified host key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHostKeyResponse) -> dict:
    out: dict = {}
    import aws_sdk_transfer.types.described_host_key

    out["HostKey"] = aws_sdk_transfer.types.described_host_key.serialize_aws_json_1_1(
        value["host_key"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHostKeyResponse:
    out: DescribeHostKeyResponse = {}  # type: ignore[typeddict-item]
    if "HostKey" in data:
        import aws_sdk_transfer.types.described_host_key

        out["host_key"] = (
            aws_sdk_transfer.types.described_host_key.deserialize_aws_json_1_1(
                data["HostKey"]
            )
        )
    else:
        raise DeserializationError("DescribeHostKeyResponse.host_key required")
    return out
