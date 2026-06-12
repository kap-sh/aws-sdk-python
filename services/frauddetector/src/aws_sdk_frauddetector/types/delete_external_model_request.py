"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteExternalModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.sage_maker_endpoint_identifier


class DeleteExternalModelRequest(TypedDict):
    model_endpoint: "aws_sdk_frauddetector.types.sage_maker_endpoint_identifier.sageMakerEndpointIdentifier"
    """<p>The endpoint of the Amazon Sagemaker model to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteExternalModelRequest) -> dict:
    out: dict = {}
    out["modelEndpoint"] = value["model_endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteExternalModelRequest:
    out: DeleteExternalModelRequest = {}  # type: ignore[typeddict-item]
    if "modelEndpoint" in data:
        out["model_endpoint"] = data["modelEndpoint"]
    else:
        raise DeserializationError("DeleteExternalModelRequest.model_endpoint required")
    return out
