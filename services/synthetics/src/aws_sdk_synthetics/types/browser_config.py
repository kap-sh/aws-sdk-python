"""Generated from Smithy shape ``com.amazonaws.synthetics#BrowserConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.browser_type


class BrowserConfig(TypedDict):
    browser_type: NotRequired["aws_sdk_synthetics.types.browser_type.BrowserType"]
    """<p>The browser type associated with this browser configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserConfig) -> dict:
    out: dict = {}
    if "browser_type" in value:
        import aws_sdk_synthetics.types.browser_type

        out["BrowserType"] = aws_sdk_synthetics.types.browser_type.serialize_json(
            value["browser_type"]
        )
    return out


def deserialize_json(data: dict) -> BrowserConfig:
    out: BrowserConfig = {}  # type: ignore[typeddict-item]
    if "BrowserType" in data:
        import aws_sdk_synthetics.types.browser_type

        out["browser_type"] = aws_sdk_synthetics.types.browser_type.deserialize_json(
            data["BrowserType"]
        )
    return out
