"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SortObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.sort_by
    import capo_partnercentral_selling.types.sort_order


class SortObject(TypedDict, closed=True):
    sort_by: NotRequired["capo_partnercentral_selling.types.sort_by.SortBy"]
    """<p> Specifies the field by which to sort the resource snapshot jobs. </p>"""
    sort_order: NotRequired["capo_partnercentral_selling.types.sort_order.SortOrder"]
    """<p> Determines the order in which the sorted results are presented. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SortObject) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_partnercentral_selling.types.sort_by

        out["SortBy"] = (
            capo_partnercentral_selling.types.sort_by.serialize_aws_json_1_0(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_partnercentral_selling.types.sort_order

        out["SortOrder"] = (
            capo_partnercentral_selling.types.sort_order.serialize_aws_json_1_0(
                value["sort_order"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SortObject:
    out: SortObject = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import capo_partnercentral_selling.types.sort_by

        out["sort_by"] = (
            capo_partnercentral_selling.types.sort_by.deserialize_aws_json_1_0(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_partnercentral_selling.types.sort_order

        out["sort_order"] = (
            capo_partnercentral_selling.types.sort_order.deserialize_aws_json_1_0(
                data["SortOrder"]
            )
        )
    return out
