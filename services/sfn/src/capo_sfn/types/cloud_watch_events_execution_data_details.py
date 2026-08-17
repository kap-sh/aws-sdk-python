"""Generated from Smithy shape ``com.amazonaws.sfn#CloudWatchEventsExecutionDataDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.included_details


class CloudWatchEventsExecutionDataDetails(TypedDict, closed=True):
    included: "capo_sfn.types.included_details.includedDetails"
    """<p>Indicates whether input or output was included in the response. Always <code>true</code> for API calls. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudWatchEventsExecutionDataDetails) -> dict:
    out: dict = {}
    out["included"] = value.get("included", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> CloudWatchEventsExecutionDataDetails:
    out: CloudWatchEventsExecutionDataDetails = {}  # type: ignore[typeddict-item]
    if data.get("included") is not None:
        out["included"] = data["included"]
    else:
        out["included"] = False
    return out
