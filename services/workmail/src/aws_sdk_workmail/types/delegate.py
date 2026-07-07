"""Generated from Smithy shape ``com.amazonaws.workmail#Delegate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.member_type
    import aws_sdk_workmail.types.string


class Delegate(TypedDict, closed=True):
    id: "aws_sdk_workmail.types.string.String"
    """<p>The identifier for the user or group associated as the resource's delegate.</p>"""
    type: "aws_sdk_workmail.types.member_type.MemberType"
    """<p>The type of the delegate: user or group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Delegate) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_workmail.types.member_type

    out["Type"] = aws_sdk_workmail.types.member_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Delegate:
    out: Delegate = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Delegate.id required")
    if "Type" in data:
        import aws_sdk_workmail.types.member_type

        out["type"] = aws_sdk_workmail.types.member_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("Delegate.type required")
    return out
