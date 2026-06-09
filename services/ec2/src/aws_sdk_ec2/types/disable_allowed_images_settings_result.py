"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAllowedImagesSettingsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allowed_images_settings_disabled_state


class DisableAllowedImagesSettingsResult(TypedDict):
    allowed_images_settings_state: NotRequired[
        "aws_sdk_ec2.types.allowed_images_settings_disabled_state.AllowedImagesSettingsDisabledState"
    ]
    """<p>Returns <code>disabled</code> if the request succeeds; otherwise, it returns an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableAllowedImagesSettingsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allowed_images_settings_state" in value:
        import aws_sdk_ec2.types.allowed_images_settings_disabled_state

        aws_sdk_ec2.types.allowed_images_settings_disabled_state.serialize_ec2_query(
            value["allowed_images_settings_state"],
            pairs,
            f"{prefix}.AllowedImagesSettingsState",
        )


def deserialize_ec2_query(el: Element) -> DisableAllowedImagesSettingsResult:
    out: DisableAllowedImagesSettingsResult = {}  # type: ignore[typeddict-item]
    child_allowed_images_settings_state = el.find("AllowedImagesSettingsState")
    if child_allowed_images_settings_state is not None:
        import aws_sdk_ec2.types.allowed_images_settings_disabled_state

        out["allowed_images_settings_state"] = (
            aws_sdk_ec2.types.allowed_images_settings_disabled_state.deserialize_ec2_query(
                child_allowed_images_settings_state
            )
        )
    return out
