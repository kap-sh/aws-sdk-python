"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBucketsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.account_level_bpa_sync
    import aws_sdk_lightsail.types.bucket_list
    import aws_sdk_lightsail.types.string


class GetBucketsResult(TypedDict):
    buckets: NotRequired["aws_sdk_lightsail.types.bucket_list.BucketList"]
    """<p>An array of objects that describe buckets.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetBuckets</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""
    account_level_bpa_sync: NotRequired[
        "aws_sdk_lightsail.types.account_level_bpa_sync.AccountLevelBpaSync"
    ]
    """<p>An object that describes the synchronization status of the Amazon S3 account-level block public access feature for your Lightsail buckets.</p> <p>For more information about this feature and how it affects Lightsail buckets, see <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-block-public-access-for-buckets\">Block public access for buckets in Amazon Lightsail</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBucketsResult) -> dict:
    out: dict = {}
    if "buckets" in value:
        import aws_sdk_lightsail.types.bucket_list

        out["buckets"] = aws_sdk_lightsail.types.bucket_list.serialize_aws_json_1_1(
            value["buckets"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    if "account_level_bpa_sync" in value:
        import aws_sdk_lightsail.types.account_level_bpa_sync

        out["accountLevelBpaSync"] = (
            aws_sdk_lightsail.types.account_level_bpa_sync.serialize_aws_json_1_1(
                value["account_level_bpa_sync"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBucketsResult:
    out: GetBucketsResult = {}  # type: ignore[typeddict-item]
    if "buckets" in data:
        import aws_sdk_lightsail.types.bucket_list

        out["buckets"] = aws_sdk_lightsail.types.bucket_list.deserialize_aws_json_1_1(
            data["buckets"]
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    if "accountLevelBpaSync" in data:
        import aws_sdk_lightsail.types.account_level_bpa_sync

        out["account_level_bpa_sync"] = (
            aws_sdk_lightsail.types.account_level_bpa_sync.deserialize_aws_json_1_1(
                data["accountLevelBpaSync"]
            )
        )
    return out
