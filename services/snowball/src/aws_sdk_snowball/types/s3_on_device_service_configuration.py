"""Generated from Smithy shape ``com.amazonaws.snowball#S3OnDeviceServiceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.node_fault_tolerance
    import aws_sdk_snowball.types.s3_storage_limit
    import aws_sdk_snowball.types.service_size
    import aws_sdk_snowball.types.storage_unit


class S3OnDeviceServiceConfiguration(TypedDict):
    storage_limit: NotRequired["aws_sdk_snowball.types.s3_storage_limit.S3StorageLimit"]
    """<p>If the specified storage limit value matches storage limit of one of the defined configurations, that configuration will be used. If the specified storage limit value does not match any defined configuration, the request will fail. If more than one configuration has the same storage limit as specified, the other input need to be provided.</p>"""
    storage_unit: NotRequired["aws_sdk_snowball.types.storage_unit.StorageUnit"]
    """<p>Storage unit. Currently the only supported unit is TB.</p>"""
    service_size: NotRequired["aws_sdk_snowball.types.service_size.ServiceSize"]
    """<p>Applicable when creating a cluster. Specifies how many nodes are needed for Amazon S3 compatible storage on Snow family devices. If specified, the other input can be omitted.</p>"""
    fault_tolerance: NotRequired[
        "aws_sdk_snowball.types.node_fault_tolerance.NodeFaultTolerance"
    ]
    """<p>>Fault tolerance level of the cluster. This indicates the number of nodes that can go down without degrading the performance of the cluster. This additional input helps when the specified <code>StorageLimit</code> matches more than one Amazon S3 compatible storage on Snow family devices service configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3OnDeviceServiceConfiguration) -> dict:
    out: dict = {}
    if "storage_limit" in value:
        out["StorageLimit"] = value["storage_limit"]
    if "storage_unit" in value:
        import aws_sdk_snowball.types.storage_unit

        out["StorageUnit"] = aws_sdk_snowball.types.storage_unit.serialize_aws_json_1_1(
            value["storage_unit"]
        )
    if "service_size" in value:
        out["ServiceSize"] = value["service_size"]
    if "fault_tolerance" in value:
        out["FaultTolerance"] = value["fault_tolerance"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3OnDeviceServiceConfiguration:
    out: S3OnDeviceServiceConfiguration = {}  # type: ignore[typeddict-item]
    if "StorageLimit" in data:
        out["storage_limit"] = data["StorageLimit"]
    if "StorageUnit" in data:
        import aws_sdk_snowball.types.storage_unit

        out["storage_unit"] = (
            aws_sdk_snowball.types.storage_unit.deserialize_aws_json_1_1(
                data["StorageUnit"]
            )
        )
    if "ServiceSize" in data:
        out["service_size"] = data["ServiceSize"]
    if "FaultTolerance" in data:
        out["fault_tolerance"] = data["FaultTolerance"]
    return out
