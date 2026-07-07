"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ImportSignalCatalogResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.resource_name


class ImportSignalCatalogResponse(TypedDict, closed=True):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the imported signal catalog. </p>"""
    arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of the imported signal catalog.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportSignalCatalogResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportSignalCatalogResponse:
    out: ImportSignalCatalogResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ImportSignalCatalogResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ImportSignalCatalogResponse.arn required")
    return out
