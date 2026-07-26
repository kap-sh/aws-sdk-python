"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConformancePacksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_detail_list
    import capo_config_service.types.next_token


class DescribeConformancePacksResponse(TypedDict, closed=True):
    conformance_pack_details: NotRequired[
        "capo_config_service.types.conformance_pack_detail_list.ConformancePackDetailList"
    ]
    """<p>Returns a list of <code>ConformancePackDetail</code> objects.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConformancePacksResponse) -> dict:
    out: dict = {}
    if "conformance_pack_details" in value:
        import capo_config_service.types.conformance_pack_detail_list

        out["ConformancePackDetails"] = (
            capo_config_service.types.conformance_pack_detail_list.serialize_aws_json_1_1(
                value["conformance_pack_details"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConformancePacksResponse:
    out: DescribeConformancePacksResponse = {}  # type: ignore[typeddict-item]
    if "ConformancePackDetails" in data:
        import capo_config_service.types.conformance_pack_detail_list

        out["conformance_pack_details"] = (
            capo_config_service.types.conformance_pack_detail_list.deserialize_aws_json_1_1(
                data["ConformancePackDetails"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
