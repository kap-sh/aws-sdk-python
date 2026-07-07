"""Generated from Smithy shape ``com.amazonaws.acm#ResourceRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_acm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.record_type
    import aws_sdk_acm.types.string


class ResourceRecord(TypedDict, closed=True):
    name: "aws_sdk_acm.types.string.String"
    """<p>The name of the DNS record to create in your domain. This is supplied by ACM.</p>"""
    type: "aws_sdk_acm.types.record_type.RecordType"
    """<p>The type of DNS record. Currently this can be <code>CNAME</code>.</p>"""
    value: "aws_sdk_acm.types.string.String"
    """<p>The value of the CNAME record to add to your DNS database. This is supplied by ACM.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceRecord) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_acm.types.record_type

    out["Type"] = aws_sdk_acm.types.record_type.serialize_aws_json_1_1(value["type"])
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceRecord:
    out: ResourceRecord = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ResourceRecord.name required")
    if "Type" in data:
        import aws_sdk_acm.types.record_type

        out["type"] = aws_sdk_acm.types.record_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("ResourceRecord.type required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ResourceRecord.value required")
    return out
