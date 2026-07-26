"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAllowedImagesSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.allowed_images_settings_enabled_state
    import capo_ec2.types.boolean


class EnableAllowedImagesSettingsRequest(TypedDict, closed=True):
    allowed_images_settings_state: NotRequired[
        "capo_ec2.types.allowed_images_settings_enabled_state.AllowedImagesSettingsEnabledState"
    ]
    """<p>Specify <code>enabled</code> to apply the image criteria specified by the Allowed AMIs settings. Specify <code>audit-mode</code> so that you can check which AMIs will be allowed or not allowed by the image criteria.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableAllowedImagesSettingsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allowed_images_settings_state" in value:
        import capo_ec2.types.allowed_images_settings_enabled_state

        capo_ec2.types.allowed_images_settings_enabled_state.serialize_ec2_query(
            value["allowed_images_settings_state"],
            pairs,
            f"{prefix}.AllowedImagesSettingsState",
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> EnableAllowedImagesSettingsRequest:
    out: EnableAllowedImagesSettingsRequest = {}  # type: ignore[typeddict-item]
    child_allowed_images_settings_state = el.find("AllowedImagesSettingsState")
    if child_allowed_images_settings_state is not None:
        import capo_ec2.types.allowed_images_settings_enabled_state

        out["allowed_images_settings_state"] = (
            capo_ec2.types.allowed_images_settings_enabled_state.deserialize_ec2_query(
                child_allowed_images_settings_state
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
