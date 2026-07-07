"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationFsxOntapRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.location_arn


class DescribeLocationFsxOntapRequest(TypedDict, closed=True):
    location_arn: "aws_sdk_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the FSx for ONTAP file system location that you want information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationFsxOntapRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationFsxOntapRequest:
    out: DescribeLocationFsxOntapRequest = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError(
            "DescribeLocationFsxOntapRequest.location_arn required"
        )
    return out
