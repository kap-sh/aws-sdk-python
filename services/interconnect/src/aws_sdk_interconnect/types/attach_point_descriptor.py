"""Generated from Smithy shape ``com.amazonaws.interconnect#AttachPointDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.attach_point_type


class AttachPointDescriptor(TypedDict, closed=True):
    type: "aws_sdk_interconnect.types.attach_point_type.AttachPointType"
    """<p>The type of this AttachPoint, which will dictate the syntax of the identifier.</p> <p>Current types include:</p> <ul> <li> <p>ARN</p> </li> <li> <p>DirectConnect Gateway</p> </li> </ul>"""
    identifier: "str"
    """<p>The identifier for the specific type of the AttachPoint.</p>"""
    name: "str"
    """<p>The descriptive name of the identifier attach point.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachPointDescriptor) -> dict:
    out: dict = {}
    import aws_sdk_interconnect.types.attach_point_type

    out["type"] = aws_sdk_interconnect.types.attach_point_type.serialize_aws_json_1_0(
        value["type"]
    )
    out["identifier"] = value["identifier"]
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AttachPointDescriptor:
    out: AttachPointDescriptor = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_interconnect.types.attach_point_type

        out["type"] = (
            aws_sdk_interconnect.types.attach_point_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        raise DeserializationError("AttachPointDescriptor.type required")
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("AttachPointDescriptor.identifier required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AttachPointDescriptor.name required")
    return out
