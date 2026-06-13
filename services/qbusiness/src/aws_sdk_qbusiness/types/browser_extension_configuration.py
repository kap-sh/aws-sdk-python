"""Generated from Smithy shape ``com.amazonaws.qbusiness#BrowserExtensionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.browser_extension_list


class BrowserExtensionConfiguration(TypedDict):
    enabled_browser_extensions: (
        "aws_sdk_qbusiness.types.browser_extension_list.BrowserExtensionList"
    )
    """<p>Specify the browser extensions allowed for your Amazon Q web experience.</p> <ul> <li> <p> <code>CHROME</code> — Enables the extension for Chromium-based browsers (Google Chrome, Microsoft Edge, Opera, etc.).</p> </li> <li> <p> <code>FIREFOX</code> — Enables the extension for Mozilla Firefox.</p> </li> <li> <p> <code>CHROME</code> and <code>FIREFOX</code> — Enable the extension for Chromium-based browsers and Mozilla Firefox.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserExtensionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.browser_extension_list

    out["enabledBrowserExtensions"] = (
        aws_sdk_qbusiness.types.browser_extension_list.serialize_json(
            value["enabled_browser_extensions"]
        )
    )
    return out


def deserialize_json(data: dict) -> BrowserExtensionConfiguration:
    out: BrowserExtensionConfiguration = {}  # type: ignore[typeddict-item]
    if "enabledBrowserExtensions" in data:
        import aws_sdk_qbusiness.types.browser_extension_list

        out["enabled_browser_extensions"] = (
            aws_sdk_qbusiness.types.browser_extension_list.deserialize_json(
                data["enabledBrowserExtensions"]
            )
        )
    else:
        raise DeserializationError(
            "BrowserExtensionConfiguration.enabled_browser_extensions required"
        )
    return out
