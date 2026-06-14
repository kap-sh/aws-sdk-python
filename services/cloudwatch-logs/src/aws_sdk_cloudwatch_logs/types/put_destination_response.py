"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDestinationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.destination


class PutDestinationResponse(TypedDict):
    destination: NotRequired["aws_sdk_cloudwatch_logs.types.destination.Destination"]
    """<p>The destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDestinationResponse) -> dict:
    out: dict = {}
    if "destination" in value:
        import aws_sdk_cloudwatch_logs.types.destination

        out["destination"] = (
            aws_sdk_cloudwatch_logs.types.destination.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDestinationResponse:
    out: PutDestinationResponse = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import aws_sdk_cloudwatch_logs.types.destination

        out["destination"] = (
            aws_sdk_cloudwatch_logs.types.destination.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    return out
