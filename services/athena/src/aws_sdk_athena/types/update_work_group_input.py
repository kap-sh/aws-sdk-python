"""Generated from Smithy shape ``com.amazonaws.athena#UpdateWorkGroupInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.work_group_configuration_updates
    import aws_sdk_athena.types.work_group_description_string
    import aws_sdk_athena.types.work_group_name
    import aws_sdk_athena.types.work_group_state


class UpdateWorkGroupInput(TypedDict):
    work_group: "aws_sdk_athena.types.work_group_name.WorkGroupName"
    """<p>The specified workgroup that will be updated.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.work_group_description_string.WorkGroupDescriptionString"
    ]
    """<p>The workgroup description.</p>"""
    configuration_updates: NotRequired[
        "aws_sdk_athena.types.work_group_configuration_updates.WorkGroupConfigurationUpdates"
    ]
    """<p>Contains configuration updates for an Athena SQL workgroup.</p>"""
    state: NotRequired["aws_sdk_athena.types.work_group_state.WorkGroupState"]
    """<p>The workgroup state that will be updated for the given workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkGroupInput) -> dict:
    out: dict = {}
    out["WorkGroup"] = value["work_group"]
    if "description" in value:
        out["Description"] = value["description"]
    if "configuration_updates" in value:
        import aws_sdk_athena.types.work_group_configuration_updates

        out["ConfigurationUpdates"] = (
            aws_sdk_athena.types.work_group_configuration_updates.serialize_aws_json_1_1(
                value["configuration_updates"]
            )
        )
    if "state" in value:
        import aws_sdk_athena.types.work_group_state

        out["State"] = aws_sdk_athena.types.work_group_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkGroupInput:
    out: UpdateWorkGroupInput = {}  # type: ignore[typeddict-item]
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    else:
        raise DeserializationError("UpdateWorkGroupInput.work_group required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ConfigurationUpdates" in data:
        import aws_sdk_athena.types.work_group_configuration_updates

        out["configuration_updates"] = (
            aws_sdk_athena.types.work_group_configuration_updates.deserialize_aws_json_1_1(
                data["ConfigurationUpdates"]
            )
        )
    if "State" in data:
        import aws_sdk_athena.types.work_group_state

        out["state"] = aws_sdk_athena.types.work_group_state.deserialize_aws_json_1_1(
            data["State"]
        )
    return out
