"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateServiceFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_label
    import capo_resiliencehubv2.types.service_function_criticality


class CreateServiceFunctionRequest(TypedDict, closed=True):
    name: "capo_resiliencehubv2.types.entity_label.EntityLabel"
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    criticality: "capo_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality"
    """<p>The criticality level of the service function.</p>"""
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceFunctionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["serviceArn"] = value["service_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_resiliencehubv2.types.service_function_criticality

    out["criticality"] = (
        capo_resiliencehubv2.types.service_function_criticality.serialize_json(
            value["criticality"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateServiceFunctionRequest:
    out: CreateServiceFunctionRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateServiceFunctionRequest.name required")
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("CreateServiceFunctionRequest.service_arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "criticality" in data:
        import capo_resiliencehubv2.types.service_function_criticality

        out["criticality"] = (
            capo_resiliencehubv2.types.service_function_criticality.deserialize_json(
                data["criticality"]
            )
        )
    else:
        raise DeserializationError("CreateServiceFunctionRequest.criticality required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
