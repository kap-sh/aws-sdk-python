"""Generated from Smithy shape ``com.amazonaws.transfer#ServiceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.user_details


class ServiceMetadata(TypedDict, closed=True):
    user_details: "capo_transfer.types.user_details.UserDetails"
    """<p>The Server ID (<code>ServerId</code>), Session ID (<code>SessionId</code>) and user (<code>UserName</code>) make up the <code>UserDetails</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceMetadata) -> dict:
    out: dict = {}
    import capo_transfer.types.user_details

    out["UserDetails"] = capo_transfer.types.user_details.serialize_aws_json_1_1(
        value["user_details"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceMetadata:
    out: ServiceMetadata = {}  # type: ignore[typeddict-item]
    if "UserDetails" in data:
        import capo_transfer.types.user_details

        out["user_details"] = capo_transfer.types.user_details.deserialize_aws_json_1_1(
            data["UserDetails"]
        )
    else:
        raise DeserializationError("ServiceMetadata.user_details required")
    return out
