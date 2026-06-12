"""Generated from Smithy shape ``com.amazonaws.iot#AuditCheckConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.check_custom_configuration
    import aws_sdk_iot.types.enabled


class AuditCheckConfiguration(TypedDict):
    enabled: "aws_sdk_iot.types.enabled.Enabled"
    """<p>True if this audit check is enabled for this account.</p>"""
    configuration: NotRequired[
        "aws_sdk_iot.types.check_custom_configuration.CheckCustomConfiguration"
    ]
    """<p>A structure containing the configName and corresponding configValue for configuring audit checks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditCheckConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "configuration" in value:
        import aws_sdk_iot.types.check_custom_configuration

        out["configuration"] = (
            aws_sdk_iot.types.check_custom_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuditCheckConfiguration:
    out: AuditCheckConfiguration = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "configuration" in data:
        import aws_sdk_iot.types.check_custom_configuration

        out["configuration"] = (
            aws_sdk_iot.types.check_custom_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
