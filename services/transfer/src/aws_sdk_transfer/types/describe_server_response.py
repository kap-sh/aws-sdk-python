"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeServerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.described_server


class DescribeServerResponse(TypedDict):
    server: "aws_sdk_transfer.types.described_server.DescribedServer"
    """<p>An array containing the properties of a server with the <code>ServerID</code> you specified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServerResponse) -> dict:
    out: dict = {}
    import aws_sdk_transfer.types.described_server

    out["Server"] = aws_sdk_transfer.types.described_server.serialize_aws_json_1_1(
        value["server"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServerResponse:
    out: DescribeServerResponse = {}  # type: ignore[typeddict-item]
    if "Server" in data:
        import aws_sdk_transfer.types.described_server

        out["server"] = (
            aws_sdk_transfer.types.described_server.deserialize_aws_json_1_1(
                data["Server"]
            )
        )
    else:
        raise DeserializationError("DescribeServerResponse.server required")
    return out
