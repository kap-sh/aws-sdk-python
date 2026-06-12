"""Generated from Smithy shape ``com.amazonaws.b2bi#GetCapabilityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.capability_configuration
    import aws_sdk_b2bi.types.capability_id
    import aws_sdk_b2bi.types.capability_name
    import aws_sdk_b2bi.types.capability_type
    import aws_sdk_b2bi.types.created_date
    import aws_sdk_b2bi.types.instructions_documents
    import aws_sdk_b2bi.types.modified_date
    import aws_sdk_b2bi.types.resource_arn


class GetCapabilityResponse(TypedDict):
    capability_id: "aws_sdk_b2bi.types.capability_id.CapabilityId"
    """<p>Returns a system-assigned unique identifier for the capability.</p>"""
    capability_arn: "aws_sdk_b2bi.types.resource_arn.ResourceArn"
    """<p>Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>"""
    name: "aws_sdk_b2bi.types.capability_name.CapabilityName"
    """<p>Returns the name of the capability, used to identify it.</p>"""
    type: "aws_sdk_b2bi.types.capability_type.CapabilityType"
    """<p>Returns the type of the capability. Currently, only <code>edi</code> is supported.</p>"""
    configuration: "aws_sdk_b2bi.types.capability_configuration.CapabilityConfiguration"
    """<p>Returns a structure that contains the details for a capability.</p>"""
    instructions_documents: NotRequired[
        "aws_sdk_b2bi.types.instructions_documents.InstructionsDocuments"
    ]
    """<p>Returns one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>"""
    created_at: "aws_sdk_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the capability.</p>"""
    modified_at: NotRequired["aws_sdk_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns a timestamp for last time the capability was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCapabilityResponse) -> dict:
    out: dict = {}
    out["capabilityId"] = value["capability_id"]
    out["capabilityArn"] = value["capability_arn"]
    out["name"] = value["name"]
    import aws_sdk_b2bi.types.capability_type

    out["type"] = aws_sdk_b2bi.types.capability_type.serialize_aws_json_1_0(
        value["type"]
    )
    import aws_sdk_b2bi.types.capability_configuration

    out["configuration"] = (
        aws_sdk_b2bi.types.capability_configuration.serialize_aws_json_1_0(
            value["configuration"]
        )
    )
    if "instructions_documents" in value:
        import aws_sdk_b2bi.types.instructions_documents

        out["instructionsDocuments"] = (
            aws_sdk_b2bi.types.instructions_documents.serialize_aws_json_1_0(
                value["instructions_documents"]
            )
        )
    import aws_sdk_b2bi.types.created_date

    out["createdAt"] = aws_sdk_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "modified_at" in value:
        import aws_sdk_b2bi.types.modified_date

        out["modifiedAt"] = aws_sdk_b2bi.types.modified_date.serialize_aws_json_1_0(
            value["modified_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCapabilityResponse:
    out: GetCapabilityResponse = {}  # type: ignore[typeddict-item]
    if "capabilityId" in data:
        out["capability_id"] = data["capabilityId"]
    else:
        raise DeserializationError("GetCapabilityResponse.capability_id required")
    if "capabilityArn" in data:
        out["capability_arn"] = data["capabilityArn"]
    else:
        raise DeserializationError("GetCapabilityResponse.capability_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetCapabilityResponse.name required")
    if "type" in data:
        import aws_sdk_b2bi.types.capability_type

        out["type"] = aws_sdk_b2bi.types.capability_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("GetCapabilityResponse.type required")
    if "configuration" in data:
        import aws_sdk_b2bi.types.capability_configuration

        out["configuration"] = (
            aws_sdk_b2bi.types.capability_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("GetCapabilityResponse.configuration required")
    if "instructionsDocuments" in data:
        import aws_sdk_b2bi.types.instructions_documents

        out["instructions_documents"] = (
            aws_sdk_b2bi.types.instructions_documents.deserialize_aws_json_1_0(
                data["instructionsDocuments"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_b2bi.types.created_date

        out["created_at"] = aws_sdk_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetCapabilityResponse.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_b2bi.types.modified_date

        out["modified_at"] = aws_sdk_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    return out
