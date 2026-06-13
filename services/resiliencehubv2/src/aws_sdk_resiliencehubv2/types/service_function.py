"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceFunction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.entity_description
    import aws_sdk_resiliencehubv2.types.entity_id
    import aws_sdk_resiliencehubv2.types.entity_label
    import aws_sdk_resiliencehubv2.types.service_function_criticality
    import aws_sdk_resiliencehubv2.types.service_function_source


class ServiceFunction(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    service_function_id: "aws_sdk_resiliencehubv2.types.entity_id.EntityId"
    """<p>The unique identifier of the service function.</p>"""
    name: "aws_sdk_resiliencehubv2.types.entity_label.EntityLabel"
    description: NotRequired[
        "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    criticality: "aws_sdk_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality"
    """<p>The criticality level of the service function.</p>"""
    resource_count: NotRequired["int"]
    """<p>The number of resources associated with the service function.</p>"""
    source: NotRequired[
        "aws_sdk_resiliencehubv2.types.service_function_source.ServiceFunctionSource"
    ]
    """<p>The source of the service function.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service function was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service function was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFunction) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["serviceFunctionId"] = value["service_function_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_resiliencehubv2.types.service_function_criticality

    out["criticality"] = (
        aws_sdk_resiliencehubv2.types.service_function_criticality.serialize_json(
            value["criticality"]
        )
    )
    if "resource_count" in value:
        out["resourceCount"] = value["resource_count"]
    if "source" in value:
        import aws_sdk_resiliencehubv2.types.service_function_source

        out["source"] = (
            aws_sdk_resiliencehubv2.types.service_function_source.serialize_json(
                value["source"]
            )
        )
    if "created_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceFunction:
    out: ServiceFunction = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("ServiceFunction.service_arn required")
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    else:
        raise DeserializationError("ServiceFunction.service_function_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ServiceFunction.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "criticality" in data:
        import aws_sdk_resiliencehubv2.types.service_function_criticality

        out["criticality"] = (
            aws_sdk_resiliencehubv2.types.service_function_criticality.deserialize_json(
                data["criticality"]
            )
        )
    else:
        raise DeserializationError("ServiceFunction.criticality required")
    if "resourceCount" in data:
        out["resource_count"] = data["resourceCount"]
    if "source" in data:
        import aws_sdk_resiliencehubv2.types.service_function_source

        out["source"] = (
            aws_sdk_resiliencehubv2.types.service_function_source.deserialize_json(
                data["source"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
