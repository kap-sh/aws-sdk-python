"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateTestGridUrlResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.date_time
    import aws_sdk_device_farm.types.sensitive_string


class CreateTestGridUrlResult(TypedDict):
    url: NotRequired["aws_sdk_device_farm.types.sensitive_string.SensitiveString"]
    """<p>A signed URL, expiring in <a>CreateTestGridUrlRequest$expiresInSeconds</a> seconds, to be passed to a <code>RemoteWebDriver</code>. </p>"""
    expires: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>The number of seconds the URL from <a>CreateTestGridUrlResult$url</a> stays active.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTestGridUrlResult) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    if "expires" in value:
        import aws_sdk_device_farm.types.date_time

        out["expires"] = aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
            value["expires"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTestGridUrlResult:
    out: CreateTestGridUrlResult = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    if "expires" in data:
        import aws_sdk_device_farm.types.date_time

        out["expires"] = aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["expires"]
        )
    return out
