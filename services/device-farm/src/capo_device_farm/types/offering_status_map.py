"""Generated from Smithy shape ``com.amazonaws.devicefarm#OfferingStatusMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.offering_identifier
    import capo_device_farm.types.offering_status

OfferingStatusMap: TypeAlias = dict[
    "capo_device_farm.types.offering_identifier.OfferingIdentifier",
    "capo_device_farm.types.offering_status.OfferingStatus",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: OfferingStatusMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_device_farm.types.offering_status

        out[key] = capo_device_farm.types.offering_status.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> OfferingStatusMap:
    out: OfferingStatusMap = {}
    for key, value in data.items():
        import capo_device_farm.types.offering_status

        out[key] = capo_device_farm.types.offering_status.deserialize_aws_json_1_1(
            value
        )
    return out
