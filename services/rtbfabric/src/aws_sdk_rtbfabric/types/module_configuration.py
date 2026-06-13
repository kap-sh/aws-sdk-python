"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ModuleConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.flow_module_name
    import aws_sdk_rtbfabric.types.flow_module_name_list
    import aws_sdk_rtbfabric.types.module_parameters
    import aws_sdk_rtbfabric.types.version


class ModuleConfiguration(TypedDict):
    version: NotRequired["aws_sdk_rtbfabric.types.version.Version"]
    """<p>The version of the module.</p>"""
    name: "aws_sdk_rtbfabric.types.flow_module_name.FlowModuleName"
    """<p>The name of the module.</p>"""
    depends_on: NotRequired[
        "aws_sdk_rtbfabric.types.flow_module_name_list.FlowModuleNameList"
    ]
    """<p>The dependencies of the module.</p>"""
    module_parameters: NotRequired[
        "aws_sdk_rtbfabric.types.module_parameters.ModuleParameters"
    ]
    """<p>Describes the parameters of a module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModuleConfiguration) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    out["name"] = value["name"]
    if "depends_on" in value:
        import aws_sdk_rtbfabric.types.flow_module_name_list

        out["dependsOn"] = aws_sdk_rtbfabric.types.flow_module_name_list.serialize_json(
            value["depends_on"]
        )
    if "module_parameters" in value:
        import aws_sdk_rtbfabric.types.module_parameters

        out["moduleParameters"] = (
            aws_sdk_rtbfabric.types.module_parameters.serialize_json(
                value["module_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModuleConfiguration:
    out: ModuleConfiguration = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ModuleConfiguration.name required")
    if "dependsOn" in data:
        import aws_sdk_rtbfabric.types.flow_module_name_list

        out["depends_on"] = (
            aws_sdk_rtbfabric.types.flow_module_name_list.deserialize_json(
                data["dependsOn"]
            )
        )
    if "moduleParameters" in data:
        import aws_sdk_rtbfabric.types.module_parameters

        out["module_parameters"] = (
            aws_sdk_rtbfabric.types.module_parameters.deserialize_json(
                data["moduleParameters"]
            )
        )
    return out
