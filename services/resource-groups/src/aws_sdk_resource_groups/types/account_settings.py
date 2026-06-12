"""Generated from Smithy shape ``com.amazonaws.resourcegroups#AccountSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_lifecycle_events_desired_status
    import aws_sdk_resource_groups.types.group_lifecycle_events_status
    import aws_sdk_resource_groups.types.group_lifecycle_events_status_message


class AccountSettings(TypedDict):
    group_lifecycle_events_desired_status: NotRequired[
        "aws_sdk_resource_groups.types.group_lifecycle_events_desired_status.GroupLifecycleEventsDesiredStatus"
    ]
    """<p>The desired target status of the group lifecycle events feature. If</p>"""
    group_lifecycle_events_status: NotRequired[
        "aws_sdk_resource_groups.types.group_lifecycle_events_status.GroupLifecycleEventsStatus"
    ]
    """<p>The current status of the group lifecycle events feature.</p>"""
    group_lifecycle_events_status_message: NotRequired[
        "aws_sdk_resource_groups.types.group_lifecycle_events_status_message.GroupLifecycleEventsStatusMessage"
    ]
    """<p>The text of any error message occurs during an attempt to turn group lifecycle events on or off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountSettings) -> dict:
    out: dict = {}
    if "group_lifecycle_events_desired_status" in value:
        import aws_sdk_resource_groups.types.group_lifecycle_events_desired_status

        out["GroupLifecycleEventsDesiredStatus"] = (
            aws_sdk_resource_groups.types.group_lifecycle_events_desired_status.serialize_json(
                value["group_lifecycle_events_desired_status"]
            )
        )
    if "group_lifecycle_events_status" in value:
        import aws_sdk_resource_groups.types.group_lifecycle_events_status

        out["GroupLifecycleEventsStatus"] = (
            aws_sdk_resource_groups.types.group_lifecycle_events_status.serialize_json(
                value["group_lifecycle_events_status"]
            )
        )
    if "group_lifecycle_events_status_message" in value:
        out["GroupLifecycleEventsStatusMessage"] = value[
            "group_lifecycle_events_status_message"
        ]
    return out


def deserialize_json(data: dict) -> AccountSettings:
    out: AccountSettings = {}  # type: ignore[typeddict-item]
    if "GroupLifecycleEventsDesiredStatus" in data:
        import aws_sdk_resource_groups.types.group_lifecycle_events_desired_status

        out["group_lifecycle_events_desired_status"] = (
            aws_sdk_resource_groups.types.group_lifecycle_events_desired_status.deserialize_json(
                data["GroupLifecycleEventsDesiredStatus"]
            )
        )
    if "GroupLifecycleEventsStatus" in data:
        import aws_sdk_resource_groups.types.group_lifecycle_events_status

        out["group_lifecycle_events_status"] = (
            aws_sdk_resource_groups.types.group_lifecycle_events_status.deserialize_json(
                data["GroupLifecycleEventsStatus"]
            )
        )
    if "GroupLifecycleEventsStatusMessage" in data:
        out["group_lifecycle_events_status_message"] = data[
            "GroupLifecycleEventsStatusMessage"
        ]
    return out
