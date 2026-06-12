"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationObjectStorageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.location_arn


class DescribeLocationObjectStorageRequest(TypedDict):
    location_arn: "aws_sdk_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the object storage system location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationObjectStorageRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationObjectStorageRequest:
    out: DescribeLocationObjectStorageRequest = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError(
            "DescribeLocationObjectStorageRequest.location_arn required"
        )
    return out
