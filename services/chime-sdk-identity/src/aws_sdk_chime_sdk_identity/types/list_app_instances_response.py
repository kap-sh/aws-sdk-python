"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_list
    import aws_sdk_chime_sdk_identity.types.next_token


class ListAppInstancesResponse(TypedDict, closed=True):
    app_instances: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance_list.AppInstanceList"
    ]
    """<p>The information for each <code>AppInstance</code>.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API requests until the maximum number of <code>AppInstance</code>s is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstancesResponse) -> dict:
    out: dict = {}
    if "app_instances" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance_list

        out["AppInstances"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_list.serialize_json(
                value["app_instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInstancesResponse:
    out: ListAppInstancesResponse = {}  # type: ignore[typeddict-item]
    if "AppInstances" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_list

        out["app_instances"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_list.deserialize_json(
                data["AppInstances"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
