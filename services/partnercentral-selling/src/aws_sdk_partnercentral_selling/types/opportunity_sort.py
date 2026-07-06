"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunitySort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.opportunity_sort_name
    import aws_sdk_partnercentral_selling.types.sort_order


class OpportunitySort(TypedDict, closed=True):
    sort_order: "aws_sdk_partnercentral_selling.types.sort_order.SortOrder"
    """<p>Sort order.</p> <p>Default: <code>Descending</code> </p>"""
    sort_by: (
        "aws_sdk_partnercentral_selling.types.opportunity_sort_name.OpportunitySortName"
    )
    """<p>Field name to sort by.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunitySort) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_selling.types.sort_order

    out["SortOrder"] = (
        aws_sdk_partnercentral_selling.types.sort_order.serialize_aws_json_1_0(
            value["sort_order"]
        )
    )
    import aws_sdk_partnercentral_selling.types.opportunity_sort_name

    out["SortBy"] = (
        aws_sdk_partnercentral_selling.types.opportunity_sort_name.serialize_aws_json_1_0(
            value["sort_by"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpportunitySort:
    out: OpportunitySort = {}  # type: ignore[typeddict-item]
    if "SortOrder" in data:
        import aws_sdk_partnercentral_selling.types.sort_order

        out["sort_order"] = (
            aws_sdk_partnercentral_selling.types.sort_order.deserialize_aws_json_1_0(
                data["SortOrder"]
            )
        )
    else:
        raise DeserializationError("OpportunitySort.sort_order required")
    if "SortBy" in data:
        import aws_sdk_partnercentral_selling.types.opportunity_sort_name

        out["sort_by"] = (
            aws_sdk_partnercentral_selling.types.opportunity_sort_name.deserialize_aws_json_1_0(
                data["SortBy"]
            )
        )
    else:
        raise DeserializationError("OpportunitySort.sort_by required")
    return out
