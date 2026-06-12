"""Generated from Smithy shape ``com.amazonaws.timestreamquery#TargetDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.timestream_destination


class TargetDestination(TypedDict):
    timestream_destination: NotRequired[
        "aws_sdk_timestream_query.types.timestream_destination.TimestreamDestination"
    ]
    """<p>Query result destination details for Timestream data source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TargetDestination) -> dict:
    out: dict = {}
    if "timestream_destination" in value:
        import aws_sdk_timestream_query.types.timestream_destination

        out["TimestreamDestination"] = (
            aws_sdk_timestream_query.types.timestream_destination.serialize_aws_json_1_0(
                value["timestream_destination"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TargetDestination:
    out: TargetDestination = {}  # type: ignore[typeddict-item]
    if "TimestreamDestination" in data:
        import aws_sdk_timestream_query.types.timestream_destination

        out["timestream_destination"] = (
            aws_sdk_timestream_query.types.timestream_destination.deserialize_aws_json_1_0(
                data["TimestreamDestination"]
            )
        )
    return out
