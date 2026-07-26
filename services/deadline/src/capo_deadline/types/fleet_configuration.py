"""Generated from Smithy shape ``com.amazonaws.deadline#FleetConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_deadline.types.customer_managed_fleet_configuration
    import capo_deadline.types.service_managed_ec2_fleet_configuration


class _FleetConfiguration_customerManaged(TypedDict, closed=True):
    customerManaged: "capo_deadline.types.customer_managed_fleet_configuration.CustomerManagedFleetConfiguration"


class _FleetConfiguration_serviceManagedEc2(TypedDict, closed=True):
    serviceManagedEc2: "capo_deadline.types.service_managed_ec2_fleet_configuration.ServiceManagedEc2FleetConfiguration"


FleetConfiguration: TypeAlias = (
    _FleetConfiguration_customerManaged | _FleetConfiguration_serviceManagedEc2
)


# --- restJson1 ser/de ---
def serialize_json(value: FleetConfiguration) -> dict:
    if "customerManaged" in value:
        import capo_deadline.types.customer_managed_fleet_configuration

        return {
            "customerManaged": capo_deadline.types.customer_managed_fleet_configuration.serialize_json(
                value["customerManaged"]
            )
        }
    elif "serviceManagedEc2" in value:
        import capo_deadline.types.service_managed_ec2_fleet_configuration

        return {
            "serviceManagedEc2": capo_deadline.types.service_managed_ec2_fleet_configuration.serialize_json(
                value["serviceManagedEc2"]
            )
        }
    else:
        raise SerializationError("FleetConfiguration: no variant present")


def deserialize_json(data: dict) -> FleetConfiguration:
    if "customerManaged" in data:
        import capo_deadline.types.customer_managed_fleet_configuration

        return {
            "customerManaged": capo_deadline.types.customer_managed_fleet_configuration.deserialize_json(
                data["customerManaged"]
            )
        }
    elif "serviceManagedEc2" in data:
        import capo_deadline.types.service_managed_ec2_fleet_configuration

        return {
            "serviceManagedEc2": capo_deadline.types.service_managed_ec2_fleet_configuration.deserialize_json(
                data["serviceManagedEc2"]
            )
        }
    else:
        raise DeserializationError("FleetConfiguration: no recognized variant key")
