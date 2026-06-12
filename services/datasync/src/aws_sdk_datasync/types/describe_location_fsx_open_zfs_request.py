"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationFsxOpenZfsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.location_arn


class DescribeLocationFsxOpenZfsRequest(TypedDict):
    location_arn: "aws_sdk_datasync.types.location_arn.LocationArn"
    """<p>The Amazon Resource Name (ARN) of the FSx for OpenZFS location to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationFsxOpenZfsRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationFsxOpenZfsRequest:
    out: DescribeLocationFsxOpenZfsRequest = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError(
            "DescribeLocationFsxOpenZfsRequest.location_arn required"
        )
    return out
