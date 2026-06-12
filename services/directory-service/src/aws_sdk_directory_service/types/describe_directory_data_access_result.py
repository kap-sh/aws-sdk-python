"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeDirectoryDataAccessResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.data_access_status


class DescribeDirectoryDataAccessResult(TypedDict):
    data_access_status: NotRequired[
        "aws_sdk_directory_service.types.data_access_status.DataAccessStatus"
    ]
    """<p>The current status of data access through the Directory Service Data API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectoryDataAccessResult) -> dict:
    out: dict = {}
    if "data_access_status" in value:
        import aws_sdk_directory_service.types.data_access_status

        out["DataAccessStatus"] = (
            aws_sdk_directory_service.types.data_access_status.serialize_aws_json_1_1(
                value["data_access_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectoryDataAccessResult:
    out: DescribeDirectoryDataAccessResult = {}  # type: ignore[typeddict-item]
    if "DataAccessStatus" in data:
        import aws_sdk_directory_service.types.data_access_status

        out["data_access_status"] = (
            aws_sdk_directory_service.types.data_access_status.deserialize_aws_json_1_1(
                data["DataAccessStatus"]
            )
        )
    return out
