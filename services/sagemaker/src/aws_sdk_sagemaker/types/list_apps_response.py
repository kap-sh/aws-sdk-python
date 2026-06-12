"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAppsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_list
    import aws_sdk_sagemaker.types.next_token


class ListAppsResponse(TypedDict):
    apps: NotRequired["aws_sdk_sagemaker.types.app_list.AppList"]
    """<p>The list of apps.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAppsResponse) -> dict:
    out: dict = {}
    if "apps" in value:
        import aws_sdk_sagemaker.types.app_list

        out["Apps"] = aws_sdk_sagemaker.types.app_list.serialize_aws_json_1_1(
            value["apps"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAppsResponse:
    out: ListAppsResponse = {}  # type: ignore[typeddict-item]
    if "Apps" in data:
        import aws_sdk_sagemaker.types.app_list

        out["apps"] = aws_sdk_sagemaker.types.app_list.deserialize_aws_json_1_1(
            data["Apps"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
