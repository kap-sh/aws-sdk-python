"""Generated from Smithy shape ``com.amazonaws.timestreamquery#CancelQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.string


class CancelQueryResponse(TypedDict, closed=True):
    cancellation_message: NotRequired["aws_sdk_timestream_query.types.string.String"]
    """<p> A <code>CancellationMessage</code> is returned when a <code>CancelQuery</code> request for the query specified by <code>QueryId</code> has already been issued. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelQueryResponse) -> dict:
    out: dict = {}
    if "cancellation_message" in value:
        out["CancellationMessage"] = value["cancellation_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelQueryResponse:
    out: CancelQueryResponse = {}  # type: ignore[typeddict-item]
    if "CancellationMessage" in data:
        out["cancellation_message"] = data["CancellationMessage"]
    return out
