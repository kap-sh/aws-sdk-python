"""Generated from Smithy shape ``com.amazonaws.dlm#EventParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.description_regex
    import aws_sdk_dlm.types.event_type_values
    import aws_sdk_dlm.types.snapshot_owner_list


class EventParameters(TypedDict, closed=True):
    event_type: NotRequired["aws_sdk_dlm.types.event_type_values.EventTypeValues"]
    """<p>The type of event. Currently, only snapshot sharing events are supported.</p>"""
    snapshot_owner: NotRequired[
        "aws_sdk_dlm.types.snapshot_owner_list.SnapshotOwnerList"
    ]
    """<p>The IDs of the Amazon Web Services accounts that can trigger policy by sharing snapshots with your account. The policy only runs if one of the specified Amazon Web Services accounts shares a snapshot with your account.</p>"""
    description_regex: NotRequired[
        "aws_sdk_dlm.types.description_regex.DescriptionRegex"
    ]
    """<p>The snapshot description that can trigger the policy. The description pattern is specified using a regular expression. The policy runs only if a snapshot with a description that matches the specified pattern is shared with your account.</p> <p>For example, specifying <code>^.*Created for policy: policy-1234567890abcdef0.*$</code> configures the policy to run only if snapshots created by policy <code>policy-1234567890abcdef0</code> are shared with your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventParameters) -> dict:
    out: dict = {}
    if "event_type" in value:
        import aws_sdk_dlm.types.event_type_values

        out["EventType"] = aws_sdk_dlm.types.event_type_values.serialize_json(
            value["event_type"]
        )
    if "snapshot_owner" in value:
        import aws_sdk_dlm.types.snapshot_owner_list

        out["SnapshotOwner"] = aws_sdk_dlm.types.snapshot_owner_list.serialize_json(
            value["snapshot_owner"]
        )
    if "description_regex" in value:
        out["DescriptionRegex"] = value["description_regex"]
    return out


def deserialize_json(data: dict) -> EventParameters:
    out: EventParameters = {}  # type: ignore[typeddict-item]
    if "EventType" in data:
        import aws_sdk_dlm.types.event_type_values

        out["event_type"] = aws_sdk_dlm.types.event_type_values.deserialize_json(
            data["EventType"]
        )
    if "SnapshotOwner" in data:
        import aws_sdk_dlm.types.snapshot_owner_list

        out["snapshot_owner"] = aws_sdk_dlm.types.snapshot_owner_list.deserialize_json(
            data["SnapshotOwner"]
        )
    if "DescriptionRegex" in data:
        out["description_regex"] = data["DescriptionRegex"]
    return out
