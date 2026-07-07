"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DeleteSignalCatalogResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.resource_name


class DeleteSignalCatalogResponse(TypedDict, closed=True):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p>The name of the deleted signal catalog.</p>"""
    arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p>The Amazon Resource Name (ARN) of the deleted signal catalog.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteSignalCatalogResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteSignalCatalogResponse:
    out: DeleteSignalCatalogResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteSignalCatalogResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteSignalCatalogResponse.arn required")
    return out
