"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateServiceFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.entity_description
    import aws_sdk_resiliencehubv2.types.entity_id
    import aws_sdk_resiliencehubv2.types.entity_label
    import aws_sdk_resiliencehubv2.types.service_function_criticality


class UpdateServiceFunctionRequest(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    service_function_id: "aws_sdk_resiliencehubv2.types.entity_id.EntityId"
    """<p>The identifier of the service function to update.</p>"""
    name: NotRequired["aws_sdk_resiliencehubv2.types.entity_label.EntityLabel"]
    description: NotRequired[
        "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    criticality: NotRequired[
        "aws_sdk_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality"
    ]
    """<p>The updated criticality level of the service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceFunctionRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["serviceFunctionId"] = value["service_function_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "criticality" in value:
        import aws_sdk_resiliencehubv2.types.service_function_criticality

        out["criticality"] = (
            aws_sdk_resiliencehubv2.types.service_function_criticality.serialize_json(
                value["criticality"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateServiceFunctionRequest:
    out: UpdateServiceFunctionRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("UpdateServiceFunctionRequest.service_arn required")
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    else:
        raise DeserializationError(
            "UpdateServiceFunctionRequest.service_function_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "criticality" in data:
        import aws_sdk_resiliencehubv2.types.service_function_criticality

        out["criticality"] = (
            aws_sdk_resiliencehubv2.types.service_function_criticality.deserialize_json(
                data["criticality"]
            )
        )
    return out
