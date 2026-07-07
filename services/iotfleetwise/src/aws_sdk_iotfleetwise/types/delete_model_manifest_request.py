"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DeleteModelManifestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.resource_name


class DeleteModelManifestRequest(TypedDict, closed=True):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the model manifest to delete. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteModelManifestRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteModelManifestRequest:
    out: DeleteModelManifestRequest = {}  # type: ignore[typeddict-item]
    return out
