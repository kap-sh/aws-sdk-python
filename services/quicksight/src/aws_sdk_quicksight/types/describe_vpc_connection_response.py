"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeVPCConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.vpc_connection


class DescribeVPCConnectionResponse(TypedDict):
    vpc_connection: NotRequired["aws_sdk_quicksight.types.vpc_connection.VPCConnection"]
    """<p>A response object that provides information for the specified VPC connection.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVPCConnectionResponse) -> dict:
    out: dict = {}
    if "vpc_connection" in value:
        import aws_sdk_quicksight.types.vpc_connection

        out["VPCConnection"] = aws_sdk_quicksight.types.vpc_connection.serialize_json(
            value["vpc_connection"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    out["Status"] = value.get("status", 0)
    return out


def deserialize_json(data: dict) -> DescribeVPCConnectionResponse:
    out: DescribeVPCConnectionResponse = {}  # type: ignore[typeddict-item]
    if "VPCConnection" in data:
        import aws_sdk_quicksight.types.vpc_connection

        out["vpc_connection"] = (
            aws_sdk_quicksight.types.vpc_connection.deserialize_json(
                data["VPCConnection"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    return out
