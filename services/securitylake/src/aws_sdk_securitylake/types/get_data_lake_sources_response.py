"""Generated from Smithy shape ``com.amazonaws.securitylake#GetDataLakeSourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.amazon_resource_name
    import aws_sdk_securitylake.types.data_lake_source_list
    import aws_sdk_securitylake.types.next_token


class GetDataLakeSourcesResponse(TypedDict):
    data_lake_arn: NotRequired[
        "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) created by you to provide to the subscriber. For more information about ARNs and how to use them in policies, see the <a href=\"https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html\">Amazon Security Lake User Guide</a>.</p>"""
    data_lake_sources: NotRequired[
        "aws_sdk_securitylake.types.data_lake_source_list.DataLakeSourceList"
    ]
    """<p>The list of enabled accounts and enabled sources.</p>"""
    next_token: NotRequired["aws_sdk_securitylake.types.next_token.NextToken"]
    """<p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataLakeSourcesResponse) -> dict:
    out: dict = {}
    if "data_lake_arn" in value:
        out["dataLakeArn"] = value["data_lake_arn"]
    if "data_lake_sources" in value:
        import aws_sdk_securitylake.types.data_lake_source_list

        out["dataLakeSources"] = (
            aws_sdk_securitylake.types.data_lake_source_list.serialize_json(
                value["data_lake_sources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDataLakeSourcesResponse:
    out: GetDataLakeSourcesResponse = {}  # type: ignore[typeddict-item]
    if "dataLakeArn" in data:
        out["data_lake_arn"] = data["dataLakeArn"]
    if "dataLakeSources" in data:
        import aws_sdk_securitylake.types.data_lake_source_list

        out["data_lake_sources"] = (
            aws_sdk_securitylake.types.data_lake_source_list.deserialize_json(
                data["dataLakeSources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
