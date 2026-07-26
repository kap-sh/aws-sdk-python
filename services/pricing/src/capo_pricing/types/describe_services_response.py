"""Generated from Smithy shape ``com.amazonaws.pricing#DescribeServicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pricing.types.format_version
    import capo_pricing.types.service_list
    import capo_pricing.types.string


class DescribeServicesResponse(TypedDict, closed=True):
    services: NotRequired["capo_pricing.types.service_list.ServiceList"]
    """<p>The service metadata for the service or services in the response.</p>"""
    format_version: NotRequired["capo_pricing.types.format_version.FormatVersion"]
    """<p>The format version of the response. For example, <code>aws_v1</code>.</p>"""
    next_token: NotRequired["capo_pricing.types.string.String"]
    """<p>The pagination token for the next set of retrievable results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServicesResponse) -> dict:
    out: dict = {}
    if "services" in value:
        import capo_pricing.types.service_list

        out["Services"] = capo_pricing.types.service_list.serialize_aws_json_1_1(
            value["services"]
        )
    if "format_version" in value:
        out["FormatVersion"] = value["format_version"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServicesResponse:
    out: DescribeServicesResponse = {}  # type: ignore[typeddict-item]
    if "Services" in data:
        import capo_pricing.types.service_list

        out["services"] = capo_pricing.types.service_list.deserialize_aws_json_1_1(
            data["Services"]
        )
    if "FormatVersion" in data:
        out["format_version"] = data["FormatVersion"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
