"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyManagedResourceVisibilityResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_resource_visibility_settings


class ModifyManagedResourceVisibilityResult(TypedDict):
    visibility: NotRequired[
        "aws_sdk_ec2.types.managed_resource_visibility_settings.ManagedResourceVisibilitySettings"
    ]
    """<p>The updated managed resource visibility settings for the account.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyManagedResourceVisibilityResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "visibility" in value:
        import aws_sdk_ec2.types.managed_resource_visibility_settings

        aws_sdk_ec2.types.managed_resource_visibility_settings.serialize_ec2_query(
            value["visibility"], pairs, f"{prefix}.Visibility"
        )


def deserialize_ec2_query(el: Element) -> ModifyManagedResourceVisibilityResult:
    out: ModifyManagedResourceVisibilityResult = {}  # type: ignore[typeddict-item]
    child_visibility = el.find("Visibility")
    if child_visibility is not None:
        import aws_sdk_ec2.types.managed_resource_visibility_settings

        out["visibility"] = (
            aws_sdk_ec2.types.managed_resource_visibility_settings.deserialize_ec2_query(
                child_visibility
            )
        )
    return out
