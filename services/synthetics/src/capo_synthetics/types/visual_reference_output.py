"""Generated from Smithy shape ``com.amazonaws.synthetics#VisualReferenceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.base_screenshots
    import capo_synthetics.types.browser_type
    import capo_synthetics.types.string


class VisualReferenceOutput(TypedDict, closed=True):
    base_screenshots: NotRequired[
        "capo_synthetics.types.base_screenshots.BaseScreenshots"
    ]
    """<p>An array of screenshots that are used as the baseline for comparisons during visual monitoring.</p>"""
    base_canary_run_id: NotRequired["capo_synthetics.types.string.String"]
    """<p>The ID of the canary run that produced the baseline screenshots that are used for visual monitoring comparisons by this canary.</p>"""
    browser_type: NotRequired["capo_synthetics.types.browser_type.BrowserType"]
    """<p>The browser type associated with this visual reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualReferenceOutput) -> dict:
    out: dict = {}
    if "base_screenshots" in value:
        import capo_synthetics.types.base_screenshots

        out["BaseScreenshots"] = capo_synthetics.types.base_screenshots.serialize_json(
            value["base_screenshots"]
        )
    if "base_canary_run_id" in value:
        out["BaseCanaryRunId"] = value["base_canary_run_id"]
    if "browser_type" in value:
        import capo_synthetics.types.browser_type

        out["BrowserType"] = capo_synthetics.types.browser_type.serialize_json(
            value["browser_type"]
        )
    return out


def deserialize_json(data: dict) -> VisualReferenceOutput:
    out: VisualReferenceOutput = {}  # type: ignore[typeddict-item]
    if "BaseScreenshots" in data:
        import capo_synthetics.types.base_screenshots

        out["base_screenshots"] = (
            capo_synthetics.types.base_screenshots.deserialize_json(
                data["BaseScreenshots"]
            )
        )
    if "BaseCanaryRunId" in data:
        out["base_canary_run_id"] = data["BaseCanaryRunId"]
    if "BrowserType" in data:
        import capo_synthetics.types.browser_type

        out["browser_type"] = capo_synthetics.types.browser_type.deserialize_json(
            data["BrowserType"]
        )
    return out
