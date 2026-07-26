"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_group


class ModifyVerifiedAccessGroupResult(TypedDict, closed=True):
    verified_access_group: NotRequired[
        "capo_ec2.types.verified_access_group.VerifiedAccessGroup"
    ]
    """<p>Details about the Verified Access group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "verified_access_group" in value:
        import capo_ec2.types.verified_access_group

        capo_ec2.types.verified_access_group.serialize_ec2_query(
            value["verified_access_group"], pairs, f"{prefix}.VerifiedAccessGroup"
        )


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessGroupResult:
    out: ModifyVerifiedAccessGroupResult = {}  # type: ignore[typeddict-item]
    child_verified_access_group = el.find("VerifiedAccessGroup")
    if child_verified_access_group is not None:
        import capo_ec2.types.verified_access_group

        out["verified_access_group"] = (
            capo_ec2.types.verified_access_group.deserialize_ec2_query(
                child_verified_access_group
            )
        )
    return out
