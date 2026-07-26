"""Generated from Smithy shape ``com.amazonaws.mq#BrokerInstanceOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__list_of__string
    import capo_mq.types.__list_of_availability_zone
    import capo_mq.types.__list_of_deployment_mode
    import capo_mq.types.__string
    import capo_mq.types.broker_storage_type
    import capo_mq.types.engine_type


class BrokerInstanceOption(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_mq.types.__list_of_availability_zone.__listOfAvailabilityZone"
    ]
    """<p>The list of available az.</p>"""
    engine_type: NotRequired["capo_mq.types.engine_type.EngineType"]
    """<p>The broker's engine type.</p>"""
    host_instance_type: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker's instance type.</p>"""
    storage_type: NotRequired["capo_mq.types.broker_storage_type.BrokerStorageType"]
    """<p>The broker's storage type.</p>"""
    supported_deployment_modes: NotRequired[
        "capo_mq.types.__list_of_deployment_mode.__listOfDeploymentMode"
    ]
    """<p>The list of supported deployment modes.</p>"""
    supported_engine_versions: NotRequired[
        "capo_mq.types.__list_of__string.__listOf__string"
    ]
    """<p>The list of supported engine versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrokerInstanceOption) -> dict:
    out: dict = {}
    if "availability_zones" in value:
        import capo_mq.types.__list_of_availability_zone

        out["availabilityZones"] = (
            capo_mq.types.__list_of_availability_zone.serialize_json(
                value["availability_zones"]
            )
        )
    if "engine_type" in value:
        import capo_mq.types.engine_type

        out["engineType"] = capo_mq.types.engine_type.serialize_json(
            value["engine_type"]
        )
    if "host_instance_type" in value:
        out["hostInstanceType"] = value["host_instance_type"]
    if "storage_type" in value:
        import capo_mq.types.broker_storage_type

        out["storageType"] = capo_mq.types.broker_storage_type.serialize_json(
            value["storage_type"]
        )
    if "supported_deployment_modes" in value:
        import capo_mq.types.__list_of_deployment_mode

        out["supportedDeploymentModes"] = (
            capo_mq.types.__list_of_deployment_mode.serialize_json(
                value["supported_deployment_modes"]
            )
        )
    if "supported_engine_versions" in value:
        import capo_mq.types.__list_of__string

        out["supportedEngineVersions"] = capo_mq.types.__list_of__string.serialize_json(
            value["supported_engine_versions"]
        )
    return out


def deserialize_json(data: dict) -> BrokerInstanceOption:
    out: BrokerInstanceOption = {}  # type: ignore[typeddict-item]
    if "availabilityZones" in data:
        import capo_mq.types.__list_of_availability_zone

        out["availability_zones"] = (
            capo_mq.types.__list_of_availability_zone.deserialize_json(
                data["availabilityZones"]
            )
        )
    if "engineType" in data:
        import capo_mq.types.engine_type

        out["engine_type"] = capo_mq.types.engine_type.deserialize_json(
            data["engineType"]
        )
    if "hostInstanceType" in data:
        out["host_instance_type"] = data["hostInstanceType"]
    if "storageType" in data:
        import capo_mq.types.broker_storage_type

        out["storage_type"] = capo_mq.types.broker_storage_type.deserialize_json(
            data["storageType"]
        )
    if "supportedDeploymentModes" in data:
        import capo_mq.types.__list_of_deployment_mode

        out["supported_deployment_modes"] = (
            capo_mq.types.__list_of_deployment_mode.deserialize_json(
                data["supportedDeploymentModes"]
            )
        )
    if "supportedEngineVersions" in data:
        import capo_mq.types.__list_of__string

        out["supported_engine_versions"] = (
            capo_mq.types.__list_of__string.deserialize_json(
                data["supportedEngineVersions"]
            )
        )
    return out
