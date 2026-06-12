"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DescribeTableResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.table


class DescribeTableResponse(TypedDict):
    table: NotRequired["aws_sdk_timestream_write.types.table.Table"]
    """<p>The Timestream table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeTableResponse) -> dict:
    out: dict = {}
    if "table" in value:
        import aws_sdk_timestream_write.types.table

        out["Table"] = aws_sdk_timestream_write.types.table.serialize_aws_json_1_0(
            value["table"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeTableResponse:
    out: DescribeTableResponse = {}  # type: ignore[typeddict-item]
    if "Table" in data:
        import aws_sdk_timestream_write.types.table

        out["table"] = aws_sdk_timestream_write.types.table.deserialize_aws_json_1_0(
            data["Table"]
        )
    return out
