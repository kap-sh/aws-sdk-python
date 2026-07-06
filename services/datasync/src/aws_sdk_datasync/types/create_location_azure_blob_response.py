"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationAzureBlobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.location_arn


class CreateLocationAzureBlobResponse(TypedDict, closed=True):
    location_arn: NotRequired["aws_sdk_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the Azure Blob Storage transfer location that you created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationAzureBlobResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationAzureBlobResponse:
    out: CreateLocationAzureBlobResponse = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    return out
