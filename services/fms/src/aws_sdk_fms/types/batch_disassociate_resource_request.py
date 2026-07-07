"""Generated from Smithy shape ``com.amazonaws.fms#BatchDisassociateResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.identifier
    import aws_sdk_fms.types.identifier_list


class BatchDisassociateResourceRequest(TypedDict, closed=True):
    resource_set_identifier: "aws_sdk_fms.types.identifier.Identifier"
    """<p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>"""
    items: "aws_sdk_fms.types.identifier_list.IdentifierList"
    """<p>The uniform resource identifiers (URI) of resources that should be disassociated from the resource set. The URIs must be Amazon Resource Names (ARNs).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDisassociateResourceRequest) -> dict:
    out: dict = {}
    out["ResourceSetIdentifier"] = value["resource_set_identifier"]
    import aws_sdk_fms.types.identifier_list

    out["Items"] = aws_sdk_fms.types.identifier_list.serialize_aws_json_1_1(
        value["items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDisassociateResourceRequest:
    out: BatchDisassociateResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceSetIdentifier" in data:
        out["resource_set_identifier"] = data["ResourceSetIdentifier"]
    else:
        raise DeserializationError(
            "BatchDisassociateResourceRequest.resource_set_identifier required"
        )
    if "Items" in data:
        import aws_sdk_fms.types.identifier_list

        out["items"] = aws_sdk_fms.types.identifier_list.deserialize_aws_json_1_1(
            data["Items"]
        )
    else:
        raise DeserializationError("BatchDisassociateResourceRequest.items required")
    return out
