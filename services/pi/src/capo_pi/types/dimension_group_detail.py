"""Generated from Smithy shape ``com.amazonaws.pi#DimensionGroupDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.dimension_detail_list
    import capo_pi.types.string


class DimensionGroupDetail(TypedDict, closed=True):
    group: NotRequired["capo_pi.types.string.String"]
    """<p>The name of the dimension group.</p>"""
    dimensions: NotRequired["capo_pi.types.dimension_detail_list.DimensionDetailList"]
    """<p>The dimensions within a dimension group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionGroupDetail) -> dict:
    out: dict = {}
    if "group" in value:
        out["Group"] = value["group"]
    if "dimensions" in value:
        import capo_pi.types.dimension_detail_list

        out["Dimensions"] = capo_pi.types.dimension_detail_list.serialize_aws_json_1_1(
            value["dimensions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DimensionGroupDetail:
    out: DimensionGroupDetail = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        out["group"] = data["Group"]
    if "Dimensions" in data:
        import capo_pi.types.dimension_detail_list

        out["dimensions"] = (
            capo_pi.types.dimension_detail_list.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    return out
