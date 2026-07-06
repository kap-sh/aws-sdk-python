"""Generated from Smithy shape ``com.amazonaws.storagegateway#AddCacheInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.disk_ids
    import aws_sdk_storage_gateway.types.gateway_arn


class AddCacheInput(TypedDict, closed=True):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    disk_ids: "aws_sdk_storage_gateway.types.disk_ids.DiskIds"
    """<p>An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the <a>ListLocalDisks</a> API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddCacheInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    import aws_sdk_storage_gateway.types.disk_ids

    out["DiskIds"] = aws_sdk_storage_gateway.types.disk_ids.serialize_aws_json_1_1(
        value["disk_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddCacheInput:
    out: AddCacheInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("AddCacheInput.gateway_arn required")
    if "DiskIds" in data:
        import aws_sdk_storage_gateway.types.disk_ids

        out["disk_ids"] = (
            aws_sdk_storage_gateway.types.disk_ids.deserialize_aws_json_1_1(
                data["DiskIds"]
            )
        )
    else:
        raise DeserializationError("AddCacheInput.disk_ids required")
    return out
