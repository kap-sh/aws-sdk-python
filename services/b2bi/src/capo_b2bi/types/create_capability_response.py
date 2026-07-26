"""Generated from Smithy shape ``com.amazonaws.b2bi#CreateCapabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.capability_configuration
    import capo_b2bi.types.capability_id
    import capo_b2bi.types.capability_name
    import capo_b2bi.types.capability_type
    import capo_b2bi.types.created_date
    import capo_b2bi.types.instructions_documents
    import capo_b2bi.types.resource_arn


class CreateCapabilityResponse(TypedDict, closed=True):
    capability_id: "capo_b2bi.types.capability_id.CapabilityId"
    """<p>Returns a system-assigned unique identifier for the capability.</p>"""
    capability_arn: "capo_b2bi.types.resource_arn.ResourceArn"
    """<p>Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>"""
    name: "capo_b2bi.types.capability_name.CapabilityName"
    """<p>Returns the name of the capability used to identify it.</p>"""
    type: "capo_b2bi.types.capability_type.CapabilityType"
    """<p>Returns the type of the capability. Currently, only <code>edi</code> is supported.</p>"""
    configuration: "capo_b2bi.types.capability_configuration.CapabilityConfiguration"
    """<p>Returns a structure that contains the details for a capability.</p>"""
    instructions_documents: NotRequired[
        "capo_b2bi.types.instructions_documents.InstructionsDocuments"
    ]
    """<p>Returns one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>"""
    created_at: "capo_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the capability.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCapabilityResponse) -> dict:
    out: dict = {}
    out["capabilityId"] = value["capability_id"]
    out["capabilityArn"] = value["capability_arn"]
    out["name"] = value["name"]
    import capo_b2bi.types.capability_type

    out["type"] = capo_b2bi.types.capability_type.serialize_aws_json_1_0(value["type"])
    import capo_b2bi.types.capability_configuration

    out["configuration"] = (
        capo_b2bi.types.capability_configuration.serialize_aws_json_1_0(
            value["configuration"]
        )
    )
    if "instructions_documents" in value:
        import capo_b2bi.types.instructions_documents

        out["instructionsDocuments"] = (
            capo_b2bi.types.instructions_documents.serialize_aws_json_1_0(
                value["instructions_documents"]
            )
        )
    import capo_b2bi.types.created_date

    out["createdAt"] = capo_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCapabilityResponse:
    out: CreateCapabilityResponse = {}  # type: ignore[typeddict-item]
    if "capabilityId" in data:
        out["capability_id"] = data["capabilityId"]
    else:
        raise DeserializationError("CreateCapabilityResponse.capability_id required")
    if "capabilityArn" in data:
        out["capability_arn"] = data["capabilityArn"]
    else:
        raise DeserializationError("CreateCapabilityResponse.capability_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCapabilityResponse.name required")
    if "type" in data:
        import capo_b2bi.types.capability_type

        out["type"] = capo_b2bi.types.capability_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("CreateCapabilityResponse.type required")
    if "configuration" in data:
        import capo_b2bi.types.capability_configuration

        out["configuration"] = (
            capo_b2bi.types.capability_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateCapabilityResponse.configuration required")
    if "instructionsDocuments" in data:
        import capo_b2bi.types.instructions_documents

        out["instructions_documents"] = (
            capo_b2bi.types.instructions_documents.deserialize_aws_json_1_0(
                data["instructionsDocuments"]
            )
        )
    if "createdAt" in data:
        import capo_b2bi.types.created_date

        out["created_at"] = capo_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateCapabilityResponse.created_at required")
    return out
