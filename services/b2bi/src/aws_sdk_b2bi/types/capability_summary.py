"""Generated from Smithy shape ``com.amazonaws.b2bi#CapabilitySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.capability_id
    import aws_sdk_b2bi.types.capability_name
    import aws_sdk_b2bi.types.capability_type
    import aws_sdk_b2bi.types.created_date
    import aws_sdk_b2bi.types.modified_date


class CapabilitySummary(TypedDict):
    capability_id: "aws_sdk_b2bi.types.capability_id.CapabilityId"
    """<p>Returns a system-assigned unique identifier for the capability.</p>"""
    name: "aws_sdk_b2bi.types.capability_name.CapabilityName"
    """<p>The display name of the capability.</p>"""
    type: "aws_sdk_b2bi.types.capability_type.CapabilityType"
    """<p>Returns the type of the capability. Currently, only <code>edi</code> is supported.</p>"""
    created_at: "aws_sdk_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the capability.</p>"""
    modified_at: NotRequired["aws_sdk_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns a timestamp that identifies the most recent date and time that the capability was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapabilitySummary) -> dict:
    out: dict = {}
    out["capabilityId"] = value["capability_id"]
    out["name"] = value["name"]
    import aws_sdk_b2bi.types.capability_type

    out["type"] = aws_sdk_b2bi.types.capability_type.serialize_aws_json_1_0(
        value["type"]
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


def deserialize_aws_json_1_0(data: dict) -> CapabilitySummary:
    out: CapabilitySummary = {}  # type: ignore[typeddict-item]
    if "capabilityId" in data:
        out["capability_id"] = data["capabilityId"]
    else:
        raise DeserializationError("CapabilitySummary.capability_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CapabilitySummary.name required")
    if "type" in data:
        import aws_sdk_b2bi.types.capability_type

        out["type"] = aws_sdk_b2bi.types.capability_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("CapabilitySummary.type required")
    if "createdAt" in data:
        import aws_sdk_b2bi.types.created_date

        out["created_at"] = aws_sdk_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CapabilitySummary.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_b2bi.types.modified_date

        out["modified_at"] = aws_sdk_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    return out
