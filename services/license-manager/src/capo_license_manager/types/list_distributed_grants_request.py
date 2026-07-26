"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListDistributedGrantsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn_list
    import capo_license_manager.types.filter_list
    import capo_license_manager.types.max_size100
    import capo_license_manager.types.string


class ListDistributedGrantsRequest(TypedDict, closed=True):
    grant_arns: NotRequired["capo_license_manager.types.arn_list.ArnList"]
    """<p>Amazon Resource Names (ARNs) of the grants.</p>"""
    filters: NotRequired["capo_license_manager.types.filter_list.FilterList"]
    """<p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>LicenseArn</code> </p> </li> <li> <p> <code>GrantStatus</code> </p> </li> <li> <p> <code>GranteePrincipalARN</code> </p> </li> <li> <p> <code>ProductSKU</code> </p> </li> <li> <p> <code>LicenseIssuerName</code> </p> </li> </ul>"""
    next_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""
    max_results: NotRequired["capo_license_manager.types.max_size100.MaxSize100"]
    """<p>Maximum number of results to return in a single call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDistributedGrantsRequest) -> dict:
    out: dict = {}
    if "grant_arns" in value:
        import capo_license_manager.types.arn_list

        out["GrantArns"] = capo_license_manager.types.arn_list.serialize_aws_json_1_1(
            value["grant_arns"]
        )
    if "filters" in value:
        import capo_license_manager.types.filter_list

        out["Filters"] = capo_license_manager.types.filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDistributedGrantsRequest:
    out: ListDistributedGrantsRequest = {}  # type: ignore[typeddict-item]
    if "GrantArns" in data:
        import capo_license_manager.types.arn_list

        out["grant_arns"] = (
            capo_license_manager.types.arn_list.deserialize_aws_json_1_1(
                data["GrantArns"]
            )
        )
    if "Filters" in data:
        import capo_license_manager.types.filter_list

        out["filters"] = (
            capo_license_manager.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
