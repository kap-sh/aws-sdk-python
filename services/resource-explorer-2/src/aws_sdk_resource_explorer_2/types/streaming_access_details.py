"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#StreamingAccessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resource_explorer_2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class StreamingAccessDetails(TypedDict, closed=True):
    service_principal: "str"
    """<p>The service principal of the Amazon Web Services service that has streaming access to your Resource Explorer data. A service principal is a unique identifier for an Amazon Web Services service.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when streaming access was granted to the Amazon Web Services service, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamingAccessDetails) -> dict:
    out: dict = {}
    out["ServicePrincipal"] = value["service_principal"]
    import aws_sdk_resource_explorer_2.types._prelude.timestamp

    out["CreatedAt"] = (
        aws_sdk_resource_explorer_2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> StreamingAccessDetails:
    out: StreamingAccessDetails = {}  # type: ignore[typeddict-item]
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        raise DeserializationError("StreamingAccessDetails.service_principal required")
    if "CreatedAt" in data:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("StreamingAccessDetails.created_at required")
    return out
