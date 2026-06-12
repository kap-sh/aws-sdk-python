"""Generated from Smithy shape ``com.amazonaws.mediatailor#AvailSuppression``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.fill_policy
    import aws_sdk_mediatailor.types.mode


class AvailSuppression(TypedDict):
    mode: NotRequired["aws_sdk_mediatailor.types.mode.Mode"]
    """<p>Sets the ad suppression mode. By default, ad suppression is off and all ad breaks are filled with ads or slate. When Mode is set to <code>BEHIND_LIVE_EDGE</code>, ad suppression is active and MediaTailor won't fill ad breaks on or behind the ad suppression Value time in the manifest lookback window. When Mode is set to <code>AFTER_LIVE_EDGE</code>, ad suppression is active and MediaTailor won't fill ad breaks that are within the live edge plus the avail suppression value.</p>"""
    value: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>A live edge offset time in HH:MM:SS. MediaTailor won't fill ad breaks on or behind this time in the manifest lookback window. If Value is set to 00:00:00, it is in sync with the live edge, and MediaTailor won't fill any ad breaks on or behind the live edge. If you set a Value time, MediaTailor won't fill any ad breaks on or behind this time in the manifest lookback window. For example, if you set 00:45:00, then MediaTailor will fill ad breaks that occur within 45 minutes behind the live edge, but won't fill ad breaks on or behind 45 minutes behind the live edge.</p>"""
    fill_policy: NotRequired["aws_sdk_mediatailor.types.fill_policy.FillPolicy"]
    """<p>Defines the policy to apply to the avail suppression mode. <code>BEHIND_LIVE_EDGE</code> will always use the full avail suppression policy. <code>AFTER_LIVE_EDGE</code> mode can be used to invoke partial ad break fills when a session starts mid-break.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailSuppression) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_mediatailor.types.mode

        out["Mode"] = aws_sdk_mediatailor.types.mode.serialize_json(value["mode"])
    if "value" in value:
        out["Value"] = value["value"]
    if "fill_policy" in value:
        import aws_sdk_mediatailor.types.fill_policy

        out["FillPolicy"] = aws_sdk_mediatailor.types.fill_policy.serialize_json(
            value["fill_policy"]
        )
    return out


def deserialize_json(data: dict) -> AvailSuppression:
    out: AvailSuppression = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import aws_sdk_mediatailor.types.mode

        out["mode"] = aws_sdk_mediatailor.types.mode.deserialize_json(data["Mode"])
    if "Value" in data:
        out["value"] = data["Value"]
    if "FillPolicy" in data:
        import aws_sdk_mediatailor.types.fill_policy

        out["fill_policy"] = aws_sdk_mediatailor.types.fill_policy.deserialize_json(
            data["FillPolicy"]
        )
    return out
