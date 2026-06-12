"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateSignalCatalogResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.resource_name


class CreateSignalCatalogResponse(TypedDict):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the created signal catalog. </p>"""
    arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p> The ARN of the created signal catalog. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSignalCatalogResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateSignalCatalogResponse:
    out: CreateSignalCatalogResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSignalCatalogResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateSignalCatalogResponse.arn required")
    return out
