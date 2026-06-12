"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotTwinMakerSourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filters
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class IotTwinMakerSourceConfiguration(TypedDict):
    workspace: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The IoT TwinMaker workspace.</p>"""
    filters: NotRequired[
        "aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filters.IotTwinMakerSourceConfigurationFilters"
    ]
    """<p>The metadata transfer job AWS IoT TwinMaker source configuration filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotTwinMakerSourceConfiguration) -> dict:
    out: dict = {}
    out["workspace"] = value["workspace"]
    if "filters" in value:
        import aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filters

        out["filters"] = (
            aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filters.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> IotTwinMakerSourceConfiguration:
    out: IotTwinMakerSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "workspace" in data:
        out["workspace"] = data["workspace"]
    else:
        raise DeserializationError("IotTwinMakerSourceConfiguration.workspace required")
    if "filters" in data:
        import aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filters

        out["filters"] = (
            aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filters.deserialize_json(
                data["filters"]
            )
        )
    return out
