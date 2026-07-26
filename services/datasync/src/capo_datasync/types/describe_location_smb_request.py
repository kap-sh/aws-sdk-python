"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationSmbRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.location_arn


class DescribeLocationSmbRequest(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the SMB location that you want information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationSmbRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationSmbRequest:
    out: DescribeLocationSmbRequest = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError("DescribeLocationSmbRequest.location_arn required")
    return out
