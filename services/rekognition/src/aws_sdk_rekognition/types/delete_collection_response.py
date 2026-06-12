"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteCollectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.u_integer


class DeleteCollectionResponse(TypedDict):
    status_code: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>HTTP status code that indicates the result of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCollectionResponse) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["StatusCode"] = value["status_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCollectionResponse:
    out: DeleteCollectionResponse = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        out["status_code"] = data["StatusCode"]
    return out
