"""Generated from Smithy shape ``com.amazonaws.xray#BackendConnectionErrors``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_integer


class BackendConnectionErrors(TypedDict, closed=True):
    timeout_count: NotRequired["aws_sdk_xray.types.nullable_integer.NullableInteger"]
    """<p></p>"""
    connection_refused_count: NotRequired[
        "aws_sdk_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    http_code4_xx_count: NotRequired[
        "aws_sdk_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    http_code5_xx_count: NotRequired[
        "aws_sdk_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    unknown_host_count: NotRequired[
        "aws_sdk_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    other_count: NotRequired["aws_sdk_xray.types.nullable_integer.NullableInteger"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendConnectionErrors) -> dict:
    out: dict = {}
    if "timeout_count" in value:
        out["TimeoutCount"] = value["timeout_count"]
    if "connection_refused_count" in value:
        out["ConnectionRefusedCount"] = value["connection_refused_count"]
    if "http_code4_xx_count" in value:
        out["HTTPCode4XXCount"] = value["http_code4_xx_count"]
    if "http_code5_xx_count" in value:
        out["HTTPCode5XXCount"] = value["http_code5_xx_count"]
    if "unknown_host_count" in value:
        out["UnknownHostCount"] = value["unknown_host_count"]
    if "other_count" in value:
        out["OtherCount"] = value["other_count"]
    return out


def deserialize_json(data: dict) -> BackendConnectionErrors:
    out: BackendConnectionErrors = {}  # type: ignore[typeddict-item]
    if "TimeoutCount" in data:
        out["timeout_count"] = data["TimeoutCount"]
    if "ConnectionRefusedCount" in data:
        out["connection_refused_count"] = data["ConnectionRefusedCount"]
    if "HTTPCode4XXCount" in data:
        out["http_code4_xx_count"] = data["HTTPCode4XXCount"]
    if "HTTPCode5XXCount" in data:
        out["http_code5_xx_count"] = data["HTTPCode5XXCount"]
    if "UnknownHostCount" in data:
        out["unknown_host_count"] = data["UnknownHostCount"]
    if "OtherCount" in data:
        out["other_count"] = data["OtherCount"]
    return out
