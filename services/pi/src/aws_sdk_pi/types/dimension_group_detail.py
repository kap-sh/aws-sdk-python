"""Generated from Smithy shape ``com.amazonaws.pi#DimensionGroupDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pi.types.dimension_detail_list
    import aws_sdk_pi.types.string


class DimensionGroupDetail(TypedDict):
    group: NotRequired["aws_sdk_pi.types.string.String"]
    """<p>The name of the dimension group.</p>"""
    dimensions: NotRequired[
        "aws_sdk_pi.types.dimension_detail_list.DimensionDetailList"
    ]
    """<p>The dimensions within a dimension group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionGroupDetail) -> dict:
    out: dict = {}
    if "group" in value:
        out["Group"] = value["group"]
    if "dimensions" in value:
        import aws_sdk_pi.types.dimension_detail_list

        out["Dimensions"] = (
            aws_sdk_pi.types.dimension_detail_list.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DimensionGroupDetail:
    out: DimensionGroupDetail = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        out["group"] = data["Group"]
    if "Dimensions" in data:
        import aws_sdk_pi.types.dimension_detail_list

        out["dimensions"] = (
            aws_sdk_pi.types.dimension_detail_list.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    return out
