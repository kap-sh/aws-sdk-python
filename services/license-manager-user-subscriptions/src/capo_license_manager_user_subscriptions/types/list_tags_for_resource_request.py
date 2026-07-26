"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_license_manager_user_subscriptions.types.resource_arn.ResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
