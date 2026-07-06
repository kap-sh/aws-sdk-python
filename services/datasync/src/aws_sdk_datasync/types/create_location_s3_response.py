"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationS3Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.location_arn


class CreateLocationS3Response(TypedDict, closed=True):
    location_arn: NotRequired["aws_sdk_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the S3 location that you created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationS3Response) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationS3Response:
    out: CreateLocationS3Response = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    return out
