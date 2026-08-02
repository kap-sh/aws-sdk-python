"""Generated from Smithy shape ``com.amazonaws.ec2#TargetGroupsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.target_groups


class TargetGroupsConfig(TypedDict, closed=True):
    target_groups: NotRequired["capo_ec2.types.target_groups.TargetGroups"]
    """<p>One or more target groups.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetGroupsConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_groups" in value:
        import capo_ec2.types.target_groups

        capo_ec2.types.target_groups.serialize_ec2_query(
            value["target_groups"], pairs, f"{key_prefix}TargetGroups"
        )


def deserialize_ec2_query(el: Element) -> TargetGroupsConfig:
    out: TargetGroupsConfig = {}  # type: ignore[typeddict-item]
    if el.find("TargetGroups") is not None:
        import capo_ec2.types.target_groups

        out["target_groups"] = capo_ec2.types.target_groups.deserialize_ec2_query(
            el, "TargetGroups"
        )
    return out
