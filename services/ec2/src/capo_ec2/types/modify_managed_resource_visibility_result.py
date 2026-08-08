"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyManagedResourceVisibilityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.managed_resource_visibility_settings


class ModifyManagedResourceVisibilityResult(TypedDict, closed=True):
    visibility: NotRequired[
        "capo_ec2.types.managed_resource_visibility_settings.ManagedResourceVisibilitySettings"
    ]
    """<p>The updated managed resource visibility settings for the account.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyManagedResourceVisibilityResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "visibility" in value:
        import capo_ec2.types.managed_resource_visibility_settings

        capo_ec2.types.managed_resource_visibility_settings.serialize_ec2_query(
            value["visibility"], pairs, f"{key_prefix}Visibility"
        )


def deserialize_ec2_query(el: Element) -> ModifyManagedResourceVisibilityResult:
    out: ModifyManagedResourceVisibilityResult = {}  # type: ignore[typeddict-item]
    child_visibility = el.find("visibility")
    if child_visibility is not None:
        import capo_ec2.types.managed_resource_visibility_settings

        out["visibility"] = (
            capo_ec2.types.managed_resource_visibility_settings.deserialize_ec2_query(
                child_visibility
            )
        )
    return out
