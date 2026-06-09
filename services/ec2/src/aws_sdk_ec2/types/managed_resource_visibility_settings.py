"""Generated from Smithy shape ``com.amazonaws.ec2#ManagedResourceVisibilitySettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_resource_default_visibility


class ManagedResourceVisibilitySettings(TypedDict):
    default_visibility: NotRequired[
        "aws_sdk_ec2.types.managed_resource_default_visibility.ManagedResourceDefaultVisibility"
    ]
    """<p>The default visibility setting for managed resources. A value of <code>hidden</code> indicates that managed resources are not included in Describe operation responses by default. A value of <code>visible</code> indicates that managed resources are included by default.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ManagedResourceVisibilitySettings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "default_visibility" in value:
        import aws_sdk_ec2.types.managed_resource_default_visibility

        aws_sdk_ec2.types.managed_resource_default_visibility.serialize_ec2_query(
            value["default_visibility"], pairs, f"{prefix}.DefaultVisibility"
        )


def deserialize_ec2_query(el: Element) -> ManagedResourceVisibilitySettings:
    out: ManagedResourceVisibilitySettings = {}  # type: ignore[typeddict-item]
    child_default_visibility = el.find("DefaultVisibility")
    if child_default_visibility is not None:
        import aws_sdk_ec2.types.managed_resource_default_visibility

        out["default_visibility"] = (
            aws_sdk_ec2.types.managed_resource_default_visibility.deserialize_ec2_query(
                child_default_visibility
            )
        )
    return out
