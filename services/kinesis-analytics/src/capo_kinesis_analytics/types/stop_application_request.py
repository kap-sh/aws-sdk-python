"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#StopApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_name


class StopApplicationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of the running application to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopApplicationRequest:
    out: StopApplicationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError("StopApplicationRequest.application_name required")
    return out
