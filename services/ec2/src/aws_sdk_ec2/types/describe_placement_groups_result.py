"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePlacementGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_list


class DescribePlacementGroupsResult(TypedDict):
    placement_groups: NotRequired[
        "aws_sdk_ec2.types.placement_group_list.PlacementGroupList"
    ]
    """<p>Information about the placement groups.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribePlacementGroupsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "placement_groups" in value:
        import aws_sdk_ec2.types.placement_group_list

        aws_sdk_ec2.types.placement_group_list.serialize_ec2_query(
            value["placement_groups"], pairs, f"{prefix}.PlacementGroupSet"
        )


def deserialize_ec2_query(el: Element) -> DescribePlacementGroupsResult:
    out: DescribePlacementGroupsResult = {}  # type: ignore[typeddict-item]
    if el.find("PlacementGroupSet") is not None:
        import aws_sdk_ec2.types.placement_group_list

        out["placement_groups"] = (
            aws_sdk_ec2.types.placement_group_list.deserialize_ec2_query(
                el, "PlacementGroupSet"
            )
        )
    return out
