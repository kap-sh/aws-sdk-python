"""Generated from Smithy shape ``com.amazonaws.xray#ResponseTimeRootCause``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_boolean
    import aws_sdk_xray.types.response_time_root_cause_services


class ResponseTimeRootCause(TypedDict, closed=True):
    services: NotRequired[
        "aws_sdk_xray.types.response_time_root_cause_services.ResponseTimeRootCauseServices"
    ]
    """<p>A list of corresponding services. A service identifies a segment and contains a name, account ID, type, and inferred flag.</p>"""
    client_impacting: NotRequired["aws_sdk_xray.types.nullable_boolean.NullableBoolean"]
    """<p>A flag that denotes that the root cause impacts the trace client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseTimeRootCause) -> dict:
    out: dict = {}
    if "services" in value:
        import aws_sdk_xray.types.response_time_root_cause_services

        out["Services"] = (
            aws_sdk_xray.types.response_time_root_cause_services.serialize_json(
                value["services"]
            )
        )
    if "client_impacting" in value:
        out["ClientImpacting"] = value["client_impacting"]
    return out


def deserialize_json(data: dict) -> ResponseTimeRootCause:
    out: ResponseTimeRootCause = {}  # type: ignore[typeddict-item]
    if "Services" in data:
        import aws_sdk_xray.types.response_time_root_cause_services

        out["services"] = (
            aws_sdk_xray.types.response_time_root_cause_services.deserialize_json(
                data["Services"]
            )
        )
    if "ClientImpacting" in data:
        out["client_impacting"] = data["ClientImpacting"]
    return out
