"""Generated from Smithy shape ``com.amazonaws.quicksight#ServiceNowParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.site_base_url


class ServiceNowParameters(TypedDict, closed=True):
    site_base_url: "aws_sdk_quicksight.types.site_base_url.SiteBaseUrl"
    """<p>URL of the base site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowParameters) -> dict:
    out: dict = {}
    out["SiteBaseUrl"] = value["site_base_url"]
    return out


def deserialize_json(data: dict) -> ServiceNowParameters:
    out: ServiceNowParameters = {}  # type: ignore[typeddict-item]
    if "SiteBaseUrl" in data:
        out["site_base_url"] = data["SiteBaseUrl"]
    else:
        raise DeserializationError("ServiceNowParameters.site_base_url required")
    return out
