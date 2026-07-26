"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateHubContentPresignedUrlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.authorized_url_configs
    import capo_sagemaker.types.next_token


class CreateHubContentPresignedUrlsResponse(TypedDict, closed=True):
    authorized_url_configs: NotRequired[
        "capo_sagemaker.types.authorized_url_configs.AuthorizedUrlConfigs"
    ]
    """<p>An array of authorized URL configurations, each containing a presigned URL and its corresponding local file path for proper file organization during download.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token for pagination. If present, indicates that more presigned URLs are available. Use this token in a subsequent request to retrieve additional URLs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHubContentPresignedUrlsResponse) -> dict:
    out: dict = {}
    if "authorized_url_configs" in value:
        import capo_sagemaker.types.authorized_url_configs

        out["AuthorizedUrlConfigs"] = (
            capo_sagemaker.types.authorized_url_configs.serialize_aws_json_1_1(
                value["authorized_url_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHubContentPresignedUrlsResponse:
    out: CreateHubContentPresignedUrlsResponse = {}  # type: ignore[typeddict-item]
    if "AuthorizedUrlConfigs" in data:
        import capo_sagemaker.types.authorized_url_configs

        out["authorized_url_configs"] = (
            capo_sagemaker.types.authorized_url_configs.deserialize_aws_json_1_1(
                data["AuthorizedUrlConfigs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
