"""Generated from Smithy shape ``com.amazonaws.securitylake#LogSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.log_source

LogSourceList: TypeAlias = list["aws_sdk_securitylake.types.log_source.LogSource"]


# --- restJson1 ser/de ---
def serialize_json(value: LogSourceList) -> list:
    import aws_sdk_securitylake.types.log_source

    out: list = []
    for item in value:
        out.append(aws_sdk_securitylake.types.log_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogSourceList:
    import aws_sdk_securitylake.types.log_source

    out: LogSourceList = []
    for item in data:
        out.append(aws_sdk_securitylake.types.log_source.deserialize_json(item))
    return out
