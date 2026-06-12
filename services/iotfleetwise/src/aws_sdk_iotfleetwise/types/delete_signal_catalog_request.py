"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DeleteSignalCatalogRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.resource_name


class DeleteSignalCatalogRequest(TypedDict):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the signal catalog to delete. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteSignalCatalogRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteSignalCatalogRequest:
    out: DeleteSignalCatalogRequest = {}  # type: ignore[typeddict-item]
    return out
