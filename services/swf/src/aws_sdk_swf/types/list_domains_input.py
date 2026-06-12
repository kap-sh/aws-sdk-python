"""Generated from Smithy shape ``com.amazonaws.swf#ListDomainsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.page_size
    import aws_sdk_swf.types.page_token
    import aws_sdk_swf.types.registration_status
    import aws_sdk_swf.types.reverse_order


class ListDomainsInput(TypedDict):
    next_page_token: NotRequired["aws_sdk_swf.types.page_token.PageToken"]
    """<p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: \"<code>Specified token has exceeded its maximum lifetime</code>\". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>"""
    registration_status: "aws_sdk_swf.types.registration_status.RegistrationStatus"
    """<p>Specifies the registration status of the domains to list.</p>"""
    maximum_page_size: "aws_sdk_swf.types.page_size.PageSize"
    """<p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>"""
    reverse_order: "aws_sdk_swf.types.reverse_order.ReverseOrder"
    """<p>When set to <code>true</code>, returns the results in reverse order. By default, the results are returned in ascending alphabetical order by <code>name</code> of the domains.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDomainsInput) -> dict:
    out: dict = {}
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    import aws_sdk_swf.types.registration_status

    out["registrationStatus"] = (
        aws_sdk_swf.types.registration_status.serialize_aws_json_1_0(
            value["registration_status"]
        )
    )
    out["maximumPageSize"] = value.get("maximum_page_size", 0)
    out["reverseOrder"] = value.get("reverse_order", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDomainsInput:
    out: ListDomainsInput = {}  # type: ignore[typeddict-item]
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    if "registrationStatus" in data:
        import aws_sdk_swf.types.registration_status

        out["registration_status"] = (
            aws_sdk_swf.types.registration_status.deserialize_aws_json_1_0(
                data["registrationStatus"]
            )
        )
    else:
        raise DeserializationError("ListDomainsInput.registration_status required")
    if "maximumPageSize" in data:
        out["maximum_page_size"] = data["maximumPageSize"]
    else:
        out["maximum_page_size"] = 0
    if "reverseOrder" in data:
        out["reverse_order"] = data["reverseOrder"]
    else:
        out["reverse_order"] = False
    return out
