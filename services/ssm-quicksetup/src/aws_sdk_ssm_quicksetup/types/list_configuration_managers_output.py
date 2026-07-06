"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ListConfigurationManagersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.configuration_manager_list


class ListConfigurationManagersOutput(TypedDict, closed=True):
    configuration_managers_list: NotRequired[
        "aws_sdk_ssm_quicksetup.types.configuration_manager_list.ConfigurationManagerList"
    ]
    """<p>The configuration managers returned by the request.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use when requesting the next set of configuration managers. If there are no additional operations to return, the string is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationManagersOutput) -> dict:
    out: dict = {}
    if "configuration_managers_list" in value:
        import aws_sdk_ssm_quicksetup.types.configuration_manager_list

        out["ConfigurationManagersList"] = (
            aws_sdk_ssm_quicksetup.types.configuration_manager_list.serialize_json(
                value["configuration_managers_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationManagersOutput:
    out: ListConfigurationManagersOutput = {}  # type: ignore[typeddict-item]
    if "ConfigurationManagersList" in data:
        import aws_sdk_ssm_quicksetup.types.configuration_manager_list

        out["configuration_managers_list"] = (
            aws_sdk_ssm_quicksetup.types.configuration_manager_list.deserialize_json(
                data["ConfigurationManagersList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
