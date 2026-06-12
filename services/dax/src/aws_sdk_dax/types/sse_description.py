"""Generated from Smithy shape ``com.amazonaws.dax#SSEDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.sse_status


class SSEDescription(TypedDict):
    status: NotRequired["aws_sdk_dax.types.sse_status.SSEStatus"]
    """<p>The current state of server-side encryption:</p> <ul> <li> <p> <code>ENABLING</code> - Server-side encryption is being enabled.</p> </li> <li> <p> <code>ENABLED</code> - Server-side encryption is enabled.</p> </li> <li> <p> <code>DISABLING</code> - Server-side encryption is being disabled.</p> </li> <li> <p> <code>DISABLED</code> - Server-side encryption is disabled.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SSEDescription) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_dax.types.sse_status

        out["Status"] = aws_sdk_dax.types.sse_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SSEDescription:
    out: SSEDescription = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_dax.types.sse_status

        out["status"] = aws_sdk_dax.types.sse_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
