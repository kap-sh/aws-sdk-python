"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.tags


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_license_manager_user_subscriptions.types.tags.Tags"]
    """<p>The tags for the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_license_manager_user_subscriptions.types.tags

        out["Tags"] = (
            aws_sdk_license_manager_user_subscriptions.types.tags.serialize_json(
                value["tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_license_manager_user_subscriptions.types.tags

        out["tags"] = (
            aws_sdk_license_manager_user_subscriptions.types.tags.deserialize_json(
                data["Tags"]
            )
        )
    return out
