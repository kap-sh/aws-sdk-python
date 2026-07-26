"""Generated from Smithy shape ``com.amazonaws.ivs#MultitrackInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.is_multitrack_input_enabled
    import capo_ivs.types.multitrack_maximum_resolution
    import capo_ivs.types.multitrack_policy


class MultitrackInputConfiguration(TypedDict, closed=True):
    enabled: "capo_ivs.types.is_multitrack_input_enabled.IsMultitrackInputEnabled"
    """<p>Indicates whether multitrack input is enabled. Can be set to <code>true</code> only if channel type is <code>STANDARD</code>. Setting <code>enabled</code> to <code>true</code> with any other channel type will cause an exception. If <code>true</code>, then <code>policy</code>, <code>maximumResolution</code>, and <code>containerFormat</code> are required, and <code>containerFormat</code> must be set to <code>FRAGMENTED_MP4</code>. Default: <code>false</code>.</p>"""
    policy: NotRequired["capo_ivs.types.multitrack_policy.MultitrackPolicy"]
    """<p>Indicates whether multitrack input is allowed or required. Required if <code>enabled</code> is <code>true</code>.</p>"""
    maximum_resolution: NotRequired[
        "capo_ivs.types.multitrack_maximum_resolution.MultitrackMaximumResolution"
    ]
    """<p>Maximum resolution for multitrack input. Required if <code>enabled</code> is <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultitrackInputConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "policy" in value:
        import capo_ivs.types.multitrack_policy

        out["policy"] = capo_ivs.types.multitrack_policy.serialize_json(value["policy"])
    if "maximum_resolution" in value:
        import capo_ivs.types.multitrack_maximum_resolution

        out["maximumResolution"] = (
            capo_ivs.types.multitrack_maximum_resolution.serialize_json(
                value["maximum_resolution"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultitrackInputConfiguration:
    out: MultitrackInputConfiguration = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "policy" in data:
        import capo_ivs.types.multitrack_policy

        out["policy"] = capo_ivs.types.multitrack_policy.deserialize_json(
            data["policy"]
        )
    if "maximumResolution" in data:
        import capo_ivs.types.multitrack_maximum_resolution

        out["maximum_resolution"] = (
            capo_ivs.types.multitrack_maximum_resolution.deserialize_json(
                data["maximumResolution"]
            )
        )
    return out
