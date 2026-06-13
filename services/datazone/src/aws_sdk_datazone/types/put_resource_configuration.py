"""Generated from Smithy shape ``com.amazonaws.datazone#PutResourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.region_name
    import aws_sdk_datazone.types.resource_configuration_parameter_map


class PutResourceConfiguration(TypedDict):
    name: "str"
    """<p>The name of the resource configuration.</p>"""
    description: NotRequired["str"]
    """<p>The description of the resource configuration.</p>"""
    region: "aws_sdk_datazone.types.region_name.RegionName"
    """<p>The Amazon Web Services Region of the resource configuration.</p>"""
    parameters: "aws_sdk_datazone.types.resource_configuration_parameter_map.ResourceConfigurationParameterMap"
    """<p>The parameters of the resource configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourceConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["region"] = value["region"]
    import aws_sdk_datazone.types.resource_configuration_parameter_map

    out["parameters"] = (
        aws_sdk_datazone.types.resource_configuration_parameter_map.serialize_json(
            value["parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutResourceConfiguration:
    out: PutResourceConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PutResourceConfiguration.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError("PutResourceConfiguration.region required")
    if "parameters" in data:
        import aws_sdk_datazone.types.resource_configuration_parameter_map

        out["parameters"] = (
            aws_sdk_datazone.types.resource_configuration_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    else:
        raise DeserializationError("PutResourceConfiguration.parameters required")
    return out
