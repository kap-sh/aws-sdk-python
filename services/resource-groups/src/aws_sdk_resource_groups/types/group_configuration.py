"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_configuration_failure_reason
    import aws_sdk_resource_groups.types.group_configuration_list
    import aws_sdk_resource_groups.types.group_configuration_status


class GroupConfiguration(TypedDict):
    configuration: NotRequired[
        "aws_sdk_resource_groups.types.group_configuration_list.GroupConfigurationList"
    ]
    """<p>The configuration currently associated with the group and in effect.</p>"""
    proposed_configuration: NotRequired[
        "aws_sdk_resource_groups.types.group_configuration_list.GroupConfigurationList"
    ]
    """<p>If present, the new configuration that is in the process of being applied to the group.</p>"""
    status: NotRequired[
        "aws_sdk_resource_groups.types.group_configuration_status.GroupConfigurationStatus"
    ]
    """<p>The current status of an attempt to update the group configuration.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_resource_groups.types.group_configuration_failure_reason.GroupConfigurationFailureReason"
    ]
    """<p>If present, the reason why a request to update the group configuration failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupConfiguration) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_resource_groups.types.group_configuration_list

        out["Configuration"] = (
            aws_sdk_resource_groups.types.group_configuration_list.serialize_json(
                value["configuration"]
            )
        )
    if "proposed_configuration" in value:
        import aws_sdk_resource_groups.types.group_configuration_list

        out["ProposedConfiguration"] = (
            aws_sdk_resource_groups.types.group_configuration_list.serialize_json(
                value["proposed_configuration"]
            )
        )
    if "status" in value:
        import aws_sdk_resource_groups.types.group_configuration_status

        out["Status"] = (
            aws_sdk_resource_groups.types.group_configuration_status.serialize_json(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> GroupConfiguration:
    out: GroupConfiguration = {}  # type: ignore[typeddict-item]
    if "Configuration" in data:
        import aws_sdk_resource_groups.types.group_configuration_list

        out["configuration"] = (
            aws_sdk_resource_groups.types.group_configuration_list.deserialize_json(
                data["Configuration"]
            )
        )
    if "ProposedConfiguration" in data:
        import aws_sdk_resource_groups.types.group_configuration_list

        out["proposed_configuration"] = (
            aws_sdk_resource_groups.types.group_configuration_list.deserialize_json(
                data["ProposedConfiguration"]
            )
        )
    if "Status" in data:
        import aws_sdk_resource_groups.types.group_configuration_status

        out["status"] = (
            aws_sdk_resource_groups.types.group_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
