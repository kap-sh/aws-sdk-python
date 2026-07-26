"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.date_time
    import capo_device_farm.types.long
    import capo_device_farm.types.string


class TestGridSessionAction(TypedDict, closed=True):
    action: NotRequired["capo_device_farm.types.string.String"]
    """<p>The action taken by the session.</p>"""
    started: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The time that the session invoked the action.</p>"""
    duration: NotRequired["capo_device_farm.types.long.Long"]
    """<p>The time, in milliseconds, that the action took to complete in the browser.</p>"""
    status_code: NotRequired["capo_device_farm.types.string.String"]
    """<p>HTTP status code returned to the browser when the action was taken.</p>"""
    request_method: NotRequired["capo_device_farm.types.string.String"]
    """<p>HTTP method that the browser used to make the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSessionAction) -> dict:
    out: dict = {}
    if "action" in value:
        out["action"] = value["action"]
    if "started" in value:
        import capo_device_farm.types.date_time

        out["started"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["started"]
        )
    if "duration" in value:
        out["duration"] = value["duration"]
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "request_method" in value:
        out["requestMethod"] = value["request_method"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestGridSessionAction:
    out: TestGridSessionAction = {}  # type: ignore[typeddict-item]
    if "action" in data:
        out["action"] = data["action"]
    if "started" in data:
        import capo_device_farm.types.date_time

        out["started"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["started"]
        )
    if "duration" in data:
        out["duration"] = data["duration"]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    if "requestMethod" in data:
        out["request_method"] = data["requestMethod"]
    return out
