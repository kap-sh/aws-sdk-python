"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetSolutionIdFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_set_solution_id_filter_value_list


class OfferSetSolutionIdFilter(TypedDict):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_set_solution_id_filter_value_list.OfferSetSolutionIdFilterValueList"
    ]
    """<p>Allows filtering on the <code>SolutionId</code> of an offer set with list input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetSolutionIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.offer_set_solution_id_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.offer_set_solution_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferSetSolutionIdFilter:
    out: OfferSetSolutionIdFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.offer_set_solution_id_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.offer_set_solution_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
