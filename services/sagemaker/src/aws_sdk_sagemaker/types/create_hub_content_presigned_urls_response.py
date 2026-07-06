"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateHubContentPresignedUrlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.authorized_url_configs
    import aws_sdk_sagemaker.types.next_token


class CreateHubContentPresignedUrlsResponse(TypedDict, closed=True):
    authorized_url_configs: NotRequired[
        "aws_sdk_sagemaker.types.authorized_url_configs.AuthorizedUrlConfigs"
    ]
    """<p>An array of authorized URL configurations, each containing a presigned URL and its corresponding local file path for proper file organization during download.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token for pagination. If present, indicates that more presigned URLs are available. Use this token in a subsequent request to retrieve additional URLs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHubContentPresignedUrlsResponse) -> dict:
    out: dict = {}
    if "authorized_url_configs" in value:
        import aws_sdk_sagemaker.types.authorized_url_configs

        out["AuthorizedUrlConfigs"] = (
            aws_sdk_sagemaker.types.authorized_url_configs.serialize_aws_json_1_1(
                value["authorized_url_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHubContentPresignedUrlsResponse:
    out: CreateHubContentPresignedUrlsResponse = {}  # type: ignore[typeddict-item]
    if "AuthorizedUrlConfigs" in data:
        import aws_sdk_sagemaker.types.authorized_url_configs

        out["authorized_url_configs"] = (
            aws_sdk_sagemaker.types.authorized_url_configs.deserialize_aws_json_1_1(
                data["AuthorizedUrlConfigs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
