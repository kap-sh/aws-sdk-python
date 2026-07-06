"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.described_access
    import aws_sdk_transfer.types.server_id


class DescribeAccessResponse(TypedDict, closed=True):
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server that has this access assigned.</p>"""
    access: "aws_sdk_transfer.types.described_access.DescribedAccess"
    """<p>The external identifier of the server that the access is attached to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccessResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    import aws_sdk_transfer.types.described_access

    out["Access"] = aws_sdk_transfer.types.described_access.serialize_aws_json_1_1(
        value["access"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccessResponse:
    out: DescribeAccessResponse = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("DescribeAccessResponse.server_id required")
    if "Access" in data:
        import aws_sdk_transfer.types.described_access

        out["access"] = (
            aws_sdk_transfer.types.described_access.deserialize_aws_json_1_1(
                data["Access"]
            )
        )
    else:
        raise DeserializationError("DescribeAccessResponse.access required")
    return out
