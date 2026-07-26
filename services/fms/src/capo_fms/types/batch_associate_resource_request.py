"""Generated from Smithy shape ``com.amazonaws.fms#BatchAssociateResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.identifier
    import capo_fms.types.identifier_list


class BatchAssociateResourceRequest(TypedDict, closed=True):
    resource_set_identifier: "capo_fms.types.identifier.Identifier"
    """<p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>"""
    items: "capo_fms.types.identifier_list.IdentifierList"
    """<p>The uniform resource identifiers (URIs) of resources that should be associated to the resource set. The URIs must be Amazon Resource Names (ARNs).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAssociateResourceRequest) -> dict:
    out: dict = {}
    out["ResourceSetIdentifier"] = value["resource_set_identifier"]
    import capo_fms.types.identifier_list

    out["Items"] = capo_fms.types.identifier_list.serialize_aws_json_1_1(value["items"])
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchAssociateResourceRequest:
    out: BatchAssociateResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceSetIdentifier" in data:
        out["resource_set_identifier"] = data["ResourceSetIdentifier"]
    else:
        raise DeserializationError(
            "BatchAssociateResourceRequest.resource_set_identifier required"
        )
    if "Items" in data:
        import capo_fms.types.identifier_list

        out["items"] = capo_fms.types.identifier_list.deserialize_aws_json_1_1(
            data["Items"]
        )
    else:
        raise DeserializationError("BatchAssociateResourceRequest.items required")
    return out
