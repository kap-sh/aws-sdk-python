"""Generated from Smithy shape ``com.amazonaws.forecast#TestWindowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.error_message
    import capo_forecast.types.status
    import capo_forecast.types.timestamp


class TestWindowSummary(TypedDict, closed=True):
    test_window_start: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The time at which the test began.</p>"""
    test_window_end: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The time at which the test ended.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the test. Possible status values are:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>CREATE_FAILED</code> </p> </li> </ul>"""
    message: NotRequired["capo_forecast.types.error_message.ErrorMessage"]
    """<p>If the test failed, the reason why it failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestWindowSummary) -> dict:
    out: dict = {}
    if "test_window_start" in value:
        import capo_forecast.types.timestamp

        out["TestWindowStart"] = capo_forecast.types.timestamp.serialize_aws_json_1_1(
            value["test_window_start"]
        )
    if "test_window_end" in value:
        import capo_forecast.types.timestamp

        out["TestWindowEnd"] = capo_forecast.types.timestamp.serialize_aws_json_1_1(
            value["test_window_end"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestWindowSummary:
    out: TestWindowSummary = {}  # type: ignore[typeddict-item]
    if "TestWindowStart" in data:
        import capo_forecast.types.timestamp

        out["test_window_start"] = (
            capo_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["TestWindowStart"]
            )
        )
    if "TestWindowEnd" in data:
        import capo_forecast.types.timestamp

        out["test_window_end"] = capo_forecast.types.timestamp.deserialize_aws_json_1_1(
            data["TestWindowEnd"]
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
