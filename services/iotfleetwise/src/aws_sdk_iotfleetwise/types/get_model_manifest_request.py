"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetModelManifestRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.resource_name


class GetModelManifestRequest(TypedDict):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the vehicle model to retrieve information about. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetModelManifestRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetModelManifestRequest:
    out: GetModelManifestRequest = {}  # type: ignore[typeddict-item]
    return out
