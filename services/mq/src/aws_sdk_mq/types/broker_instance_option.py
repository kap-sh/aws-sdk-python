"""Generated from Smithy shape ``com.amazonaws.mq#BrokerInstanceOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__list_of__string
    import aws_sdk_mq.types.__list_of_availability_zone
    import aws_sdk_mq.types.__list_of_deployment_mode
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.broker_storage_type
    import aws_sdk_mq.types.engine_type


class BrokerInstanceOption(TypedDict):
    availability_zones: NotRequired[
        "aws_sdk_mq.types.__list_of_availability_zone.__listOfAvailabilityZone"
    ]
    """<p>The list of available az.</p>"""
    engine_type: NotRequired["aws_sdk_mq.types.engine_type.EngineType"]
    """<p>The broker's engine type.</p>"""
    host_instance_type: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The broker's instance type.</p>"""
    storage_type: NotRequired["aws_sdk_mq.types.broker_storage_type.BrokerStorageType"]
    """<p>The broker's storage type.</p>"""
    supported_deployment_modes: NotRequired[
        "aws_sdk_mq.types.__list_of_deployment_mode.__listOfDeploymentMode"
    ]
    """<p>The list of supported deployment modes.</p>"""
    supported_engine_versions: NotRequired[
        "aws_sdk_mq.types.__list_of__string.__listOf__string"
    ]
    """<p>The list of supported engine versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrokerInstanceOption) -> dict:
    out: dict = {}
    if "availability_zones" in value:
        import aws_sdk_mq.types.__list_of_availability_zone

        out["availabilityZones"] = (
            aws_sdk_mq.types.__list_of_availability_zone.serialize_json(
                value["availability_zones"]
            )
        )
    if "engine_type" in value:
        import aws_sdk_mq.types.engine_type

        out["engineType"] = aws_sdk_mq.types.engine_type.serialize_json(
            value["engine_type"]
        )
    if "host_instance_type" in value:
        out["hostInstanceType"] = value["host_instance_type"]
    if "storage_type" in value:
        import aws_sdk_mq.types.broker_storage_type

        out["storageType"] = aws_sdk_mq.types.broker_storage_type.serialize_json(
            value["storage_type"]
        )
    if "supported_deployment_modes" in value:
        import aws_sdk_mq.types.__list_of_deployment_mode

        out["supportedDeploymentModes"] = (
            aws_sdk_mq.types.__list_of_deployment_mode.serialize_json(
                value["supported_deployment_modes"]
            )
        )
    if "supported_engine_versions" in value:
        import aws_sdk_mq.types.__list_of__string

        out["supportedEngineVersions"] = (
            aws_sdk_mq.types.__list_of__string.serialize_json(
                value["supported_engine_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrokerInstanceOption:
    out: BrokerInstanceOption = {}  # type: ignore[typeddict-item]
    if "availabilityZones" in data:
        import aws_sdk_mq.types.__list_of_availability_zone

        out["availability_zones"] = (
            aws_sdk_mq.types.__list_of_availability_zone.deserialize_json(
                data["availabilityZones"]
            )
        )
    if "engineType" in data:
        import aws_sdk_mq.types.engine_type

        out["engine_type"] = aws_sdk_mq.types.engine_type.deserialize_json(
            data["engineType"]
        )
    if "hostInstanceType" in data:
        out["host_instance_type"] = data["hostInstanceType"]
    if "storageType" in data:
        import aws_sdk_mq.types.broker_storage_type

        out["storage_type"] = aws_sdk_mq.types.broker_storage_type.deserialize_json(
            data["storageType"]
        )
    if "supportedDeploymentModes" in data:
        import aws_sdk_mq.types.__list_of_deployment_mode

        out["supported_deployment_modes"] = (
            aws_sdk_mq.types.__list_of_deployment_mode.deserialize_json(
                data["supportedDeploymentModes"]
            )
        )
    if "supportedEngineVersions" in data:
        import aws_sdk_mq.types.__list_of__string

        out["supported_engine_versions"] = (
            aws_sdk_mq.types.__list_of__string.deserialize_json(
                data["supportedEngineVersions"]
            )
        )
    return out
