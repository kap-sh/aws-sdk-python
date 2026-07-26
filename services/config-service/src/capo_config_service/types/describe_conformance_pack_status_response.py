"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConformancePackStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_status_details_list
    import capo_config_service.types.next_token


class DescribeConformancePackStatusResponse(TypedDict, closed=True):
    conformance_pack_status_details: NotRequired[
        "capo_config_service.types.conformance_pack_status_details_list.ConformancePackStatusDetailsList"
    ]
    """<p>A list of <code>ConformancePackStatusDetail</code> objects.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConformancePackStatusResponse) -> dict:
    out: dict = {}
    if "conformance_pack_status_details" in value:
        import capo_config_service.types.conformance_pack_status_details_list

        out["ConformancePackStatusDetails"] = (
            capo_config_service.types.conformance_pack_status_details_list.serialize_aws_json_1_1(
                value["conformance_pack_status_details"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConformancePackStatusResponse:
    out: DescribeConformancePackStatusResponse = {}  # type: ignore[typeddict-item]
    if "ConformancePackStatusDetails" in data:
        import capo_config_service.types.conformance_pack_status_details_list

        out["conformance_pack_status_details"] = (
            capo_config_service.types.conformance_pack_status_details_list.deserialize_aws_json_1_1(
                data["ConformancePackStatusDetails"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
