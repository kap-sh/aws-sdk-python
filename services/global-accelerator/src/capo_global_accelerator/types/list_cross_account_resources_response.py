"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCrossAccountResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.cross_account_resources
    import capo_global_accelerator.types.generic_string


class ListCrossAccountResourcesResponse(TypedDict, closed=True):
    cross_account_resources: NotRequired[
        "capo_global_accelerator.types.cross_account_resources.CrossAccountResources"
    ]
    """<p>The cross-account resources used with an accelerator.</p>"""
    next_token: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCrossAccountResourcesResponse) -> dict:
    out: dict = {}
    if "cross_account_resources" in value:
        import capo_global_accelerator.types.cross_account_resources

        out["CrossAccountResources"] = (
            capo_global_accelerator.types.cross_account_resources.serialize_aws_json_1_1(
                value["cross_account_resources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCrossAccountResourcesResponse:
    out: ListCrossAccountResourcesResponse = {}  # type: ignore[typeddict-item]
    if "CrossAccountResources" in data:
        import capo_global_accelerator.types.cross_account_resources

        out["cross_account_resources"] = (
            capo_global_accelerator.types.cross_account_resources.deserialize_aws_json_1_1(
                data["CrossAccountResources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
