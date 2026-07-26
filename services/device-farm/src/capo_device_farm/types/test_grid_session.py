"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.date_time
    import capo_device_farm.types.device_farm_arn
    import capo_device_farm.types.double
    import capo_device_farm.types.string
    import capo_device_farm.types.test_grid_session_status


class TestGridSession(TypedDict, closed=True):
    arn: NotRequired["capo_device_farm.types.device_farm_arn.DeviceFarmArn"]
    """<p>The ARN of the session.</p>"""
    status: NotRequired[
        "capo_device_farm.types.test_grid_session_status.TestGridSessionStatus"
    ]
    """<p>The state of the session.</p>"""
    created: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The time that the session was started.</p>"""
    ended: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The time the session ended.</p>"""
    billing_minutes: NotRequired["capo_device_farm.types.double.Double"]
    """<p>The number of billed minutes that were used for this session. </p>"""
    selenium_properties: NotRequired["capo_device_farm.types.string.String"]
    """<p>A JSON object of options and parameters passed to the Selenium WebDriver.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSession) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        import capo_device_farm.types.test_grid_session_status

        out["status"] = (
            capo_device_farm.types.test_grid_session_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created" in value:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["created"]
        )
    if "ended" in value:
        import capo_device_farm.types.date_time

        out["ended"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["ended"]
        )
    if "billing_minutes" in value:
        out["billingMinutes"] = value["billing_minutes"]
    if "selenium_properties" in value:
        out["seleniumProperties"] = value["selenium_properties"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestGridSession:
    out: TestGridSession = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import capo_device_farm.types.test_grid_session_status

        out["status"] = (
            capo_device_farm.types.test_grid_session_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "created" in data:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["created"]
        )
    if "ended" in data:
        import capo_device_farm.types.date_time

        out["ended"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["ended"]
        )
    if "billingMinutes" in data:
        out["billing_minutes"] = data["billingMinutes"]
    if "seleniumProperties" in data:
        out["selenium_properties"] = data["seleniumProperties"]
    return out
