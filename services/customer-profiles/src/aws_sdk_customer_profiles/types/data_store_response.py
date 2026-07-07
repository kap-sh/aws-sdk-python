"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DataStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.optional_boolean
    import aws_sdk_customer_profiles.types.readiness


class DataStoreResponse(TypedDict, closed=True):
    enabled: NotRequired[
        "aws_sdk_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>True if data store is enabled for this domain</p>"""
    readiness: NotRequired["aws_sdk_customer_profiles.types.readiness.Readiness"]


# --- restJson1 ser/de ---
def serialize_json(value: DataStoreResponse) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "readiness" in value:
        import aws_sdk_customer_profiles.types.readiness

        out["Readiness"] = aws_sdk_customer_profiles.types.readiness.serialize_json(
            value["readiness"]
        )
    return out


def deserialize_json(data: dict) -> DataStoreResponse:
    out: DataStoreResponse = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Readiness" in data:
        import aws_sdk_customer_profiles.types.readiness

        out["readiness"] = aws_sdk_customer_profiles.types.readiness.deserialize_json(
            data["Readiness"]
        )
    return out
