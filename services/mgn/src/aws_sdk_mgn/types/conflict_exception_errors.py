"""Generated from Smithy shape ``com.amazonaws.mgn#ConflictExceptionErrors``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_mgn.types.error_details

ConflictExceptionErrors: TypeAlias = list["aws_sdk_mgn.types.error_details.ErrorDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictExceptionErrors) -> list:
    import aws_sdk_mgn.types.error_details
    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.error_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConflictExceptionErrors:
    import aws_sdk_mgn.types.error_details
    out: ConflictExceptionErrors = []
    for item in data:
        out.append(aws_sdk_mgn.types.error_details.deserialize_json(item))
    return out