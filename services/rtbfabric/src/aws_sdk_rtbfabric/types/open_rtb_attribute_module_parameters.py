"""Generated from Smithy shape ``com.amazonaws.rtbfabric#OpenRtbAttributeModuleParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.action
    import aws_sdk_rtbfabric.types.filter_configuration
    import aws_sdk_rtbfabric.types.filter_type


class OpenRtbAttributeModuleParameters(TypedDict):
    filter_type: "aws_sdk_rtbfabric.types.filter_type.FilterType"
    """<p>The filter type.</p>"""
    filter_configuration: (
        "aws_sdk_rtbfabric.types.filter_configuration.FilterConfiguration"
    )
    """<p>Describes the configuration of a filter.</p>"""
    action: "aws_sdk_rtbfabric.types.action.Action"
    """<p>Describes a bid action.</p>"""
    holdback_percentage: "float"
    """<p>The hold back percentage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenRtbAttributeModuleParameters) -> dict:
    out: dict = {}
    import aws_sdk_rtbfabric.types.filter_type

    out["filterType"] = aws_sdk_rtbfabric.types.filter_type.serialize_json(
        value["filter_type"]
    )
    import aws_sdk_rtbfabric.types.filter_configuration

    out["filterConfiguration"] = (
        aws_sdk_rtbfabric.types.filter_configuration.serialize_json(
            value["filter_configuration"]
        )
    )
    import aws_sdk_rtbfabric.types.action

    out["action"] = aws_sdk_rtbfabric.types.action.serialize_json(value["action"])
    out["holdbackPercentage"] = value["holdback_percentage"]
    return out


def deserialize_json(data: dict) -> OpenRtbAttributeModuleParameters:
    out: OpenRtbAttributeModuleParameters = {}  # type: ignore[typeddict-item]
    if "filterType" in data:
        import aws_sdk_rtbfabric.types.filter_type

        out["filter_type"] = aws_sdk_rtbfabric.types.filter_type.deserialize_json(
            data["filterType"]
        )
    else:
        raise DeserializationError(
            "OpenRtbAttributeModuleParameters.filter_type required"
        )
    if "filterConfiguration" in data:
        import aws_sdk_rtbfabric.types.filter_configuration

        out["filter_configuration"] = (
            aws_sdk_rtbfabric.types.filter_configuration.deserialize_json(
                data["filterConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "OpenRtbAttributeModuleParameters.filter_configuration required"
        )
    if "action" in data:
        import aws_sdk_rtbfabric.types.action

        out["action"] = aws_sdk_rtbfabric.types.action.deserialize_json(data["action"])
    else:
        raise DeserializationError("OpenRtbAttributeModuleParameters.action required")
    if "holdbackPercentage" in data:
        out["holdback_percentage"] = data["holdbackPercentage"]
    else:
        raise DeserializationError(
            "OpenRtbAttributeModuleParameters.holdback_percentage required"
        )
    return out
