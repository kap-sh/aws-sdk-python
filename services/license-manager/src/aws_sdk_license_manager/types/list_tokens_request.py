"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListTokensRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.filter_list
    import aws_sdk_license_manager.types.max_size100
    import aws_sdk_license_manager.types.string
    import aws_sdk_license_manager.types.string_list


class ListTokensRequest(TypedDict, closed=True):
    token_ids: NotRequired["aws_sdk_license_manager.types.string_list.StringList"]
    """<p>Token IDs.</p>"""
    filters: NotRequired["aws_sdk_license_manager.types.filter_list.FilterList"]
    """<p>Filters to scope the results. The following filter is supported:</p> <ul> <li> <p> <code>LicenseArns</code> </p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_license_manager.types.max_size100.MaxSize100"]
    """<p>Maximum number of results to return in a single call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTokensRequest) -> dict:
    out: dict = {}
    if "token_ids" in value:
        import aws_sdk_license_manager.types.string_list

        out["TokenIds"] = (
            aws_sdk_license_manager.types.string_list.serialize_aws_json_1_1(
                value["token_ids"]
            )
        )
    if "filters" in value:
        import aws_sdk_license_manager.types.filter_list

        out["Filters"] = (
            aws_sdk_license_manager.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTokensRequest:
    out: ListTokensRequest = {}  # type: ignore[typeddict-item]
    if "TokenIds" in data:
        import aws_sdk_license_manager.types.string_list

        out["token_ids"] = (
            aws_sdk_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["TokenIds"]
            )
        )
    if "Filters" in data:
        import aws_sdk_license_manager.types.filter_list

        out["filters"] = (
            aws_sdk_license_manager.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
