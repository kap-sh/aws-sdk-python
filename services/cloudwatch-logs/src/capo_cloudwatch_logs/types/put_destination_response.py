"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.destination


class PutDestinationResponse(TypedDict, closed=True):
    destination: NotRequired["capo_cloudwatch_logs.types.destination.Destination"]
    """<p>The destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDestinationResponse) -> dict:
    out: dict = {}
    if "destination" in value:
        import capo_cloudwatch_logs.types.destination

        out["destination"] = (
            capo_cloudwatch_logs.types.destination.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDestinationResponse:
    out: PutDestinationResponse = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import capo_cloudwatch_logs.types.destination

        out["destination"] = (
            capo_cloudwatch_logs.types.destination.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    return out
