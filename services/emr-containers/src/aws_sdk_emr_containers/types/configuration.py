"""Generated from Smithy shape ``com.amazonaws.emrcontainers#Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.configuration_list
    import aws_sdk_emr_containers.types.sensitive_properties_map
    import aws_sdk_emr_containers.types.string1024


class Configuration(TypedDict):
    classification: "aws_sdk_emr_containers.types.string1024.String1024"
    """<p>The classification within a configuration.</p>"""
    properties: NotRequired[
        "aws_sdk_emr_containers.types.sensitive_properties_map.SensitivePropertiesMap"
    ]
    """<p>A set of properties specified within a configuration classification.</p>"""
    configurations: NotRequired[
        "aws_sdk_emr_containers.types.configuration_list.ConfigurationList"
    ]
    """<p>A list of additional configurations to apply within a configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    out: dict = {}
    out["classification"] = value["classification"]
    if "properties" in value:
        import aws_sdk_emr_containers.types.sensitive_properties_map

        out["properties"] = (
            aws_sdk_emr_containers.types.sensitive_properties_map.serialize_json(
                value["properties"]
            )
        )
    if "configurations" in value:
        import aws_sdk_emr_containers.types.configuration_list

        out["configurations"] = (
            aws_sdk_emr_containers.types.configuration_list.serialize_json(
                value["configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if "classification" in data:
        out["classification"] = data["classification"]
    else:
        raise DeserializationError("Configuration.classification required")
    if "properties" in data:
        import aws_sdk_emr_containers.types.sensitive_properties_map

        out["properties"] = (
            aws_sdk_emr_containers.types.sensitive_properties_map.deserialize_json(
                data["properties"]
            )
        )
    if "configurations" in data:
        import aws_sdk_emr_containers.types.configuration_list

        out["configurations"] = (
            aws_sdk_emr_containers.types.configuration_list.deserialize_json(
                data["configurations"]
            )
        )
    return out
