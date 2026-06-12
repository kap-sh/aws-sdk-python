"""Generated from Smithy shape ``com.amazonaws.b2bi#CreateCapabilityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.capability_configuration
    import aws_sdk_b2bi.types.capability_name
    import aws_sdk_b2bi.types.capability_type
    import aws_sdk_b2bi.types.instructions_documents
    import aws_sdk_b2bi.types.tag_list


class CreateCapabilityRequest(TypedDict):
    name: "aws_sdk_b2bi.types.capability_name.CapabilityName"
    """<p>Specifies the name of the capability, used to identify it.</p>"""
    type: "aws_sdk_b2bi.types.capability_type.CapabilityType"
    """<p>Specifies the type of the capability. Currently, only <code>edi</code> is supported.</p>"""
    configuration: "aws_sdk_b2bi.types.capability_configuration.CapabilityConfiguration"
    """<p>Specifies a structure that contains the details for a capability.</p>"""
    instructions_documents: NotRequired[
        "aws_sdk_b2bi.types.instructions_documents.InstructionsDocuments"
    ]
    """<p>Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>"""
    client_token: NotRequired["str"]
    """<p>Reserved for future use.</p>"""
    tags: NotRequired["aws_sdk_b2bi.types.tag_list.TagList"]
    """<p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCapabilityRequest) -> dict:
    out: dict = {}
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_b2bi.types.tag_list

        out["tags"] = aws_sdk_b2bi.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCapabilityRequest:
    out: CreateCapabilityRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCapabilityRequest.name required")
    if "type" in data:
        import aws_sdk_b2bi.types.capability_type

        out["type"] = aws_sdk_b2bi.types.capability_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("CreateCapabilityRequest.type required")
    if "configuration" in data:
        import aws_sdk_b2bi.types.capability_configuration

        out["configuration"] = (
            aws_sdk_b2bi.types.capability_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateCapabilityRequest.configuration required")
    if "instructionsDocuments" in data:
        import aws_sdk_b2bi.types.instructions_documents

        out["instructions_documents"] = (
            aws_sdk_b2bi.types.instructions_documents.deserialize_aws_json_1_0(
                data["instructionsDocuments"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_b2bi.types.tag_list

        out["tags"] = aws_sdk_b2bi.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    return out
