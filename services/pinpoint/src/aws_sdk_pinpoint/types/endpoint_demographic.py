"""Generated from Smithy shape ``com.amazonaws.pinpoint#EndpointDemographic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class EndpointDemographic(TypedDict, closed=True):
    app_version: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The version of the app that's associated with the endpoint.</p>"""
    locale: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The locale of the endpoint, in the following format: the ISO 639-1 alpha-2 code, followed by an underscore (_), followed by an ISO 3166-1 alpha-2 value.</p>"""
    make: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The manufacturer of the endpoint device, such as apple or samsung.</p>"""
    model: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The model name or number of the endpoint device, such as iPhone or SM-G900F.</p>"""
    model_version: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The model version of the endpoint device.</p>"""
    platform: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The platform of the endpoint device, such as ios.</p>"""
    platform_version: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The platform version of the endpoint device.</p>"""
    timezone: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The time zone of the endpoint, specified as a tz database name value, such as America/Los_Angeles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointDemographic) -> dict:
    out: dict = {}
    if "app_version" in value:
        out["AppVersion"] = value["app_version"]
    if "locale" in value:
        out["Locale"] = value["locale"]
    if "make" in value:
        out["Make"] = value["make"]
    if "model" in value:
        out["Model"] = value["model"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    return out


def deserialize_json(data: dict) -> EndpointDemographic:
    out: EndpointDemographic = {}  # type: ignore[typeddict-item]
    if "AppVersion" in data:
        out["app_version"] = data["AppVersion"]
    if "Locale" in data:
        out["locale"] = data["Locale"]
    if "Make" in data:
        out["make"] = data["Make"]
    if "Model" in data:
        out["model"] = data["Model"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    if "Platform" in data:
        out["platform"] = data["Platform"]
    if "PlatformVersion" in data:
        out["platform_version"] = data["PlatformVersion"]
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    return out
