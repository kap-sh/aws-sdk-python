"""Generated from Smithy shape ``com.amazonaws.apprunner#TraceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.tracing_vendor


class TraceConfiguration(TypedDict, closed=True):
    vendor: "aws_sdk_apprunner.types.tracing_vendor.TracingVendor"
    """<p>The implementation provider chosen for tracing App Runner services.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TraceConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.tracing_vendor

    out["Vendor"] = aws_sdk_apprunner.types.tracing_vendor.serialize_aws_json_1_0(
        value["vendor"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TraceConfiguration:
    out: TraceConfiguration = {}  # type: ignore[typeddict-item]
    if "Vendor" in data:
        import aws_sdk_apprunner.types.tracing_vendor

        out["vendor"] = aws_sdk_apprunner.types.tracing_vendor.deserialize_aws_json_1_0(
            data["Vendor"]
        )
    else:
        raise DeserializationError("TraceConfiguration.vendor required")
    return out
