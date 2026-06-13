"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteServiceFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.entity_id


class DeleteServiceFunctionRequest(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    service_function_id: "aws_sdk_resiliencehubv2.types.entity_id.EntityId"
    """<p>The identifier of the service function to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceFunctionRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["serviceFunctionId"] = value["service_function_id"]
    return out


def deserialize_json(data: dict) -> DeleteServiceFunctionRequest:
    out: DeleteServiceFunctionRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("DeleteServiceFunctionRequest.service_arn required")
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    else:
        raise DeserializationError(
            "DeleteServiceFunctionRequest.service_function_id required"
        )
    return out
