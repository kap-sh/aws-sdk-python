"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteContactMethodRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.contact_protocol


class DeleteContactMethodRequest(TypedDict):
    protocol: "aws_sdk_lightsail.types.contact_protocol.ContactProtocol"
    """<p>The protocol that will be deleted, such as <code>Email</code> or <code>SMS</code> (text messaging).</p> <note> <p>To delete an <code>Email</code> and an <code>SMS</code> contact method if you added both, you must run separate <code>DeleteContactMethod</code> actions to delete each protocol.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteContactMethodRequest) -> dict:
    out: dict = {}
    import aws_sdk_lightsail.types.contact_protocol

    out["protocol"] = aws_sdk_lightsail.types.contact_protocol.serialize_aws_json_1_1(
        value["protocol"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteContactMethodRequest:
    out: DeleteContactMethodRequest = {}  # type: ignore[typeddict-item]
    if "protocol" in data:
        import aws_sdk_lightsail.types.contact_protocol

        out["protocol"] = (
            aws_sdk_lightsail.types.contact_protocol.deserialize_aws_json_1_1(
                data["protocol"]
            )
        )
    else:
        raise DeserializationError("DeleteContactMethodRequest.protocol required")
    return out
