"""Generated from Smithy shape ``com.amazonaws.ivschat#CloudWatchLogsDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivschat.types.log_group_name


class CloudWatchLogsDestinationConfiguration(TypedDict, closed=True):
    log_group_name: "capo_ivschat.types.log_group_name.LogGroupName"
    """<p>Name of the Amazon Cloudwatch Logs destination where chat activity will be logged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsDestinationConfiguration) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogsDestinationConfiguration:
    out: CloudWatchLogsDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError(
            "CloudWatchLogsDestinationConfiguration.log_group_name required"
        )
    return out
