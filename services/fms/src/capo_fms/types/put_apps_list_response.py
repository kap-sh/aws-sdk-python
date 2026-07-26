"""Generated from Smithy shape ``com.amazonaws.fms#PutAppsListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.apps_list_data
    import capo_fms.types.resource_arn


class PutAppsListResponse(TypedDict, closed=True):
    apps_list: NotRequired["capo_fms.types.apps_list_data.AppsListData"]
    """<p>The details of the Firewall Manager applications list.</p>"""
    apps_list_arn: NotRequired["capo_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the applications list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAppsListResponse) -> dict:
    out: dict = {}
    if "apps_list" in value:
        import capo_fms.types.apps_list_data

        out["AppsList"] = capo_fms.types.apps_list_data.serialize_aws_json_1_1(
            value["apps_list"]
        )
    if "apps_list_arn" in value:
        out["AppsListArn"] = value["apps_list_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAppsListResponse:
    out: PutAppsListResponse = {}  # type: ignore[typeddict-item]
    if "AppsList" in data:
        import capo_fms.types.apps_list_data

        out["apps_list"] = capo_fms.types.apps_list_data.deserialize_aws_json_1_1(
            data["AppsList"]
        )
    if "AppsListArn" in data:
        out["apps_list_arn"] = data["AppsListArn"]
    return out
