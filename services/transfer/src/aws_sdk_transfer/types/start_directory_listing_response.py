"""Generated from Smithy shape ``com.amazonaws.transfer#StartDirectoryListingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listing_id
    import aws_sdk_transfer.types.output_file_name


class StartDirectoryListingResponse(TypedDict):
    listing_id: "aws_sdk_transfer.types.listing_id.ListingId"
    """<p>Returns a unique identifier for the directory listing call.</p>"""
    output_file_name: "aws_sdk_transfer.types.output_file_name.OutputFileName"
    """<p>Returns the file name where the results are stored. This is a combination of the connector ID and the listing ID: <code>&lt;connector-id&gt;-&lt;listing-id&gt;.json</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDirectoryListingResponse) -> dict:
    out: dict = {}
    out["ListingId"] = value["listing_id"]
    out["OutputFileName"] = value["output_file_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDirectoryListingResponse:
    out: StartDirectoryListingResponse = {}  # type: ignore[typeddict-item]
    if "ListingId" in data:
        out["listing_id"] = data["ListingId"]
    else:
        raise DeserializationError("StartDirectoryListingResponse.listing_id required")
    if "OutputFileName" in data:
        out["output_file_name"] = data["OutputFileName"]
    else:
        raise DeserializationError(
            "StartDirectoryListingResponse.output_file_name required"
        )
    return out
