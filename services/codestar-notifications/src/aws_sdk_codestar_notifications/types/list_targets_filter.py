"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListTargetsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.list_targets_filter_name
    import aws_sdk_codestar_notifications.types.list_targets_filter_value


class ListTargetsFilter(TypedDict):
    name: "aws_sdk_codestar_notifications.types.list_targets_filter_name.ListTargetsFilterName"
    """<p>The name of the attribute you want to use to filter the returned targets.</p>"""
    value: "aws_sdk_codestar_notifications.types.list_targets_filter_value.ListTargetsFilterValue"
    """<p>The value of the attribute you want to use to filter the returned targets. For example, if you specify <code>SNS</code> for the Target type, you could specify an Amazon Resource Name (ARN) for a topic as the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsFilter) -> dict:
    out: dict = {}
    import aws_sdk_codestar_notifications.types.list_targets_filter_name

    out["Name"] = (
        aws_sdk_codestar_notifications.types.list_targets_filter_name.serialize_json(
            value["name"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ListTargetsFilter:
    out: ListTargetsFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_codestar_notifications.types.list_targets_filter_name

        out["name"] = (
            aws_sdk_codestar_notifications.types.list_targets_filter_name.deserialize_json(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("ListTargetsFilter.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ListTargetsFilter.value required")
    return out
