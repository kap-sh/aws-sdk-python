"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAllowedImagesSettingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.allowed_images_settings_enabled_state


class EnableAllowedImagesSettingsResult(TypedDict, closed=True):
    allowed_images_settings_state: NotRequired[
        "capo_ec2.types.allowed_images_settings_enabled_state.AllowedImagesSettingsEnabledState"
    ]
    """<p>Returns <code>enabled</code> or <code>audit-mode</code> if the request succeeds; otherwise, it returns an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableAllowedImagesSettingsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allowed_images_settings_state" in value:
        import capo_ec2.types.allowed_images_settings_enabled_state

        capo_ec2.types.allowed_images_settings_enabled_state.serialize_ec2_query(
            value["allowed_images_settings_state"],
            pairs,
            f"{key_prefix}AllowedImagesSettingsState",
        )


def deserialize_ec2_query(el: Element) -> EnableAllowedImagesSettingsResult:
    out: EnableAllowedImagesSettingsResult = {}  # type: ignore[typeddict-item]
    child_allowed_images_settings_state = el.find("AllowedImagesSettingsState")
    if child_allowed_images_settings_state is not None:
        import capo_ec2.types.allowed_images_settings_enabled_state

        out["allowed_images_settings_state"] = (
            capo_ec2.types.allowed_images_settings_enabled_state.deserialize_ec2_query(
                child_allowed_images_settings_state
            )
        )
    return out
