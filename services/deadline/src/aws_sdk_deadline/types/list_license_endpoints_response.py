"""Generated from Smithy shape ``com.amazonaws.deadline#ListLicenseEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.license_endpoint_summaries
    import aws_sdk_deadline.types.next_token


class ListLicenseEndpointsResponse(TypedDict, closed=True):
    license_endpoints: (
        "aws_sdk_deadline.types.license_endpoint_summaries.LicenseEndpointSummaries"
    )
    """<p>The license endpoints.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLicenseEndpointsResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.license_endpoint_summaries

    out["licenseEndpoints"] = (
        aws_sdk_deadline.types.license_endpoint_summaries.serialize_json(
            value["license_endpoints"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLicenseEndpointsResponse:
    out: ListLicenseEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "licenseEndpoints" in data:
        import aws_sdk_deadline.types.license_endpoint_summaries

        out["license_endpoints"] = (
            aws_sdk_deadline.types.license_endpoint_summaries.deserialize_json(
                data["licenseEndpoints"]
            )
        )
    else:
        raise DeserializationError(
            "ListLicenseEndpointsResponse.license_endpoints required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
