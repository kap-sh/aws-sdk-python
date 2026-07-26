"""Generated from Smithy shape ``com.amazonaws.pi#GetDimensionKeyDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.dimension_key_detail_list


class GetDimensionKeyDetailsResponse(TypedDict, closed=True):
    dimensions: NotRequired[
        "capo_pi.types.dimension_key_detail_list.DimensionKeyDetailList"
    ]
    """<p>The details for the requested dimensions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDimensionKeyDetailsResponse) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_pi.types.dimension_key_detail_list

        out["Dimensions"] = (
            capo_pi.types.dimension_key_detail_list.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDimensionKeyDetailsResponse:
    out: GetDimensionKeyDetailsResponse = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import capo_pi.types.dimension_key_detail_list

        out["dimensions"] = (
            capo_pi.types.dimension_key_detail_list.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    return out
