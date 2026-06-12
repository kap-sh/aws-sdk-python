"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetAutoDeploymentTargetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.organizational_unit_id
    import aws_sdk_cloudformation.types.region_list


class StackSetAutoDeploymentTargetSummary(TypedDict):
    organizational_unit_id: NotRequired[
        "aws_sdk_cloudformation.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The organization root ID or organizational unit (OU) IDs where the StackSet is targeted.</p>"""
    regions: NotRequired["aws_sdk_cloudformation.types.region_list.RegionList"]
    """<p>The list of Regions targeted for this organization or OU.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetAutoDeploymentTargetSummary,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "organizational_unit_id" in value:
        pairs.append(
            (f"{prefix}.OrganizationalUnitId", str(value["organizational_unit_id"]))
        )
    if "regions" in value:
        import aws_sdk_cloudformation.types.region_list

        aws_sdk_cloudformation.types.region_list.serialize_query(
            value["regions"], pairs, f"{prefix}.Regions"
        )


def deserialize_query(el: Element) -> StackSetAutoDeploymentTargetSummary:
    out: StackSetAutoDeploymentTargetSummary = {}  # type: ignore[typeddict-item]
    child_organizational_unit_id = el.find("OrganizationalUnitId")
    if child_organizational_unit_id is not None:
        out["organizational_unit_id"] = str(child_organizational_unit_id.text or "")
    child_regions = el.find("Regions")
    if child_regions is not None:
        import aws_sdk_cloudformation.types.region_list

        out["regions"] = aws_sdk_cloudformation.types.region_list.deserialize_query(
            child_regions
        )
    return out
