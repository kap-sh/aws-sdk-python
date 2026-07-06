"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_group


class CreateVerifiedAccessGroupResult(TypedDict, closed=True):
    verified_access_group: NotRequired[
        "aws_sdk_ec2.types.verified_access_group.VerifiedAccessGroup"
    ]
    """<p>Details about the Verified Access group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "verified_access_group" in value:
        import aws_sdk_ec2.types.verified_access_group

        aws_sdk_ec2.types.verified_access_group.serialize_ec2_query(
            value["verified_access_group"], pairs, f"{prefix}.VerifiedAccessGroup"
        )


def deserialize_ec2_query(el: Element) -> CreateVerifiedAccessGroupResult:
    out: CreateVerifiedAccessGroupResult = {}  # type: ignore[typeddict-item]
    child_verified_access_group = el.find("VerifiedAccessGroup")
    if child_verified_access_group is not None:
        import aws_sdk_ec2.types.verified_access_group

        out["verified_access_group"] = (
            aws_sdk_ec2.types.verified_access_group.deserialize_ec2_query(
                child_verified_access_group
            )
        )
    return out
