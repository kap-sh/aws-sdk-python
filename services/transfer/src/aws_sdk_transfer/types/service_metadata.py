"""Generated from Smithy shape ``com.amazonaws.transfer#ServiceMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.user_details


class ServiceMetadata(TypedDict):
    user_details: "aws_sdk_transfer.types.user_details.UserDetails"
    """<p>The Server ID (<code>ServerId</code>), Session ID (<code>SessionId</code>) and user (<code>UserName</code>) make up the <code>UserDetails</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceMetadata) -> dict:
    out: dict = {}
    import aws_sdk_transfer.types.user_details

    out["UserDetails"] = aws_sdk_transfer.types.user_details.serialize_aws_json_1_1(
        value["user_details"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceMetadata:
    out: ServiceMetadata = {}  # type: ignore[typeddict-item]
    if "UserDetails" in data:
        import aws_sdk_transfer.types.user_details

        out["user_details"] = (
            aws_sdk_transfer.types.user_details.deserialize_aws_json_1_1(
                data["UserDetails"]
            )
        )
    else:
        raise DeserializationError("ServiceMetadata.user_details required")
    return out
