"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeDirectoryConfigsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.directory_config_list
    import aws_sdk_appstream.types.string


class DescribeDirectoryConfigsResult(TypedDict, closed=True):
    directory_configs: NotRequired[
        "aws_sdk_appstream.types.directory_config_list.DirectoryConfigList"
    ]
    """<p>Information about the directory configurations. Note that although the response syntax in this topic includes the account password, this password is not returned in the actual response. </p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectoryConfigsResult) -> dict:
    out: dict = {}
    if "directory_configs" in value:
        import aws_sdk_appstream.types.directory_config_list

        out["DirectoryConfigs"] = (
            aws_sdk_appstream.types.directory_config_list.serialize_aws_json_1_1(
                value["directory_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectoryConfigsResult:
    out: DescribeDirectoryConfigsResult = {}  # type: ignore[typeddict-item]
    if "DirectoryConfigs" in data:
        import aws_sdk_appstream.types.directory_config_list

        out["directory_configs"] = (
            aws_sdk_appstream.types.directory_config_list.deserialize_aws_json_1_1(
                data["DirectoryConfigs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
