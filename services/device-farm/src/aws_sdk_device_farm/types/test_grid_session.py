"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSession``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.date_time
    import aws_sdk_device_farm.types.device_farm_arn
    import aws_sdk_device_farm.types.double
    import aws_sdk_device_farm.types.string
    import aws_sdk_device_farm.types.test_grid_session_status


class TestGridSession(TypedDict):
    arn: NotRequired["aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn"]
    """<p>The ARN of the session.</p>"""
    status: NotRequired[
        "aws_sdk_device_farm.types.test_grid_session_status.TestGridSessionStatus"
    ]
    """<p>The state of the session.</p>"""
    created: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>The time that the session was started.</p>"""
    ended: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>The time the session ended.</p>"""
    billing_minutes: NotRequired["aws_sdk_device_farm.types.double.Double"]
    """<p>The number of billed minutes that were used for this session. </p>"""
    selenium_properties: NotRequired["aws_sdk_device_farm.types.string.String"]
    """<p>A JSON object of options and parameters passed to the Selenium WebDriver.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSession) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        import aws_sdk_device_farm.types.test_grid_session_status

        out["status"] = (
            aws_sdk_device_farm.types.test_grid_session_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created" in value:
        import aws_sdk_device_farm.types.date_time

        out["created"] = aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
            value["created"]
        )
    if "ended" in value:
        import aws_sdk_device_farm.types.date_time

        out["ended"] = aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
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
        import aws_sdk_device_farm.types.test_grid_session_status

        out["status"] = (
            aws_sdk_device_farm.types.test_grid_session_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "created" in data:
        import aws_sdk_device_farm.types.date_time

        out["created"] = aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["created"]
        )
    if "ended" in data:
        import aws_sdk_device_farm.types.date_time

        out["ended"] = aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["ended"]
        )
    if "billingMinutes" in data:
        out["billing_minutes"] = data["billingMinutes"]
    if "seleniumProperties" in data:
        out["selenium_properties"] = data["seleniumProperties"]
    return out
