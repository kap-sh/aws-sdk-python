"""Generated from Smithy shape ``com.amazonaws.imagebuilder#AdditionalInstanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.systems_manager_agent
    import aws_sdk_imagebuilder.types.user_data_override


class AdditionalInstanceConfiguration(TypedDict, closed=True):
    systems_manager_agent: NotRequired[
        "aws_sdk_imagebuilder.types.systems_manager_agent.SystemsManagerAgent"
    ]
    """<p>Contains settings for the Systems Manager agent on your build instance.</p>"""
    user_data_override: NotRequired[
        "aws_sdk_imagebuilder.types.user_data_override.UserDataOverride"
    ]
    """<p>Use this property to provide commands or a command script to run when you launch your build instance.</p> <p>The userDataOverride property replaces any commands that Image Builder might have added to ensure that Systems Manager is installed on your Linux build instance. If you override the user data, make sure that you add commands to install Systems Manager, if it is not pre-installed on your base image.</p> <note> <p>The user data is always base 64 encoded. For example, the following commands are encoded as <code>IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhci$</code>:</p> <p> <i>#!/bin/bash</i> </p> <p>mkdir -p /var/bb/</p> <p>touch /var</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalInstanceConfiguration) -> dict:
    out: dict = {}
    if "systems_manager_agent" in value:
        import aws_sdk_imagebuilder.types.systems_manager_agent

        out["systemsManagerAgent"] = (
            aws_sdk_imagebuilder.types.systems_manager_agent.serialize_json(
                value["systems_manager_agent"]
            )
        )
    if "user_data_override" in value:
        out["userDataOverride"] = value["user_data_override"]
    return out


def deserialize_json(data: dict) -> AdditionalInstanceConfiguration:
    out: AdditionalInstanceConfiguration = {}  # type: ignore[typeddict-item]
    if "systemsManagerAgent" in data:
        import aws_sdk_imagebuilder.types.systems_manager_agent

        out["systems_manager_agent"] = (
            aws_sdk_imagebuilder.types.systems_manager_agent.deserialize_json(
                data["systemsManagerAgent"]
            )
        )
    if "userDataOverride" in data:
        out["user_data_override"] = data["userDataOverride"]
    return out
