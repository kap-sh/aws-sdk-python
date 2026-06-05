"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessGroupResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_group


class ModifyVerifiedAccessGroupResult(TypedDict):
    verified_access_group: NotRequired[
        "aws_sdk_ec2.types.verified_access_group.VerifiedAccessGroup"
    ]
    """<p>Details about the Verified Access group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "verified_access_group" in value:
        import aws_sdk_ec2.types.verified_access_group

        aws_sdk_ec2.types.verified_access_group.serialize_ec2_query(
            value["verified_access_group"], pairs, f"{prefix}.VerifiedAccessGroup"
        )


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessGroupResult:
    out: ModifyVerifiedAccessGroupResult = {}  # type: ignore[typeddict-item]
    child_verified_access_group = el.find("VerifiedAccessGroup")
    if child_verified_access_group is not None:
        import aws_sdk_ec2.types.verified_access_group

        out["verified_access_group"] = (
            aws_sdk_ec2.types.verified_access_group.deserialize_ec2_query(
                child_verified_access_group
            )
        )
    return out
